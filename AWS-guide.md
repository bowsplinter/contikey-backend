# Agile Devops

This is a simple guide to get your Django application hosted on AWS for free. Note: this is not a guide to deploy an application to production, check out [this link](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/) for that. Rather, this is to setup a server on AWS quickly and efficiently for prototyping and testing purposes (agile!).


This is a list of all the services and packages you will need:
##### From AWS:
- **Relational Database Services (RDS)**
The basic building block of Amazon RDS is the DB instance. A DB instance is an isolated database environment in the cloud.  A DB instance can contain multiple user-created databases, and you can access it by using the same tools that you use with a stand-alone database instance.
- **Elastic Compute Cloud (EC2)**
EC2 is an Amazon web service that rents out Virtual Machine space so developers can run their applications on a cloud server.

##### Others:
- **python-pip (to manage dependencies)**
PIP is a tool for installing and managing Python packages.
It comes with a command-line interface, which makes installing Python software packages as easy as issuing one command - 'pip install <package>'
Pip has a feature to manage full lists of packages and corresponding version numbers through a "requirements" file. This permits the efficient re-creation of an entire group of packages in a
separate environment (e.g. another computer) or virtual environment.
This can be achieved with a properly formatted requirements.txt file
- **virtualenv (to localize python versions)**
Many developers uses virtualenv (virtual environment) on their computer, which is useful when you want to run several applications on the same computer.
Virtualenv will manage all dependencies and enables multiple side-by-side installations of Python, one for each project.
- **mysql (to manage database functions)**
The most important part of any project!!! Data needs to be stored and accessed properly.
- **nginx (to handle server loads)**
Nginx is an efficient web server, or proxy server that handles application protocols (eg HTTP) and distributes the load to different processes. It will handle many requests for images and static resources. Requests that need to be dynamically generated will then be passed on to the application server (Gunicorn in your example). It is also asynchronous, so this way Nginx enhances the virtually shared resources without being dedicated and blocked to one connection.
- **gunicorn (to deploy to servers)**
Gunicorn takes in only fowarded dynamic HTTP requests from proxies like Nginx and translates it to a [Webserver Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) compatible request and calls the web framework's handler requests. In this way, Gunicorn is light and rapid as it doesn't have to deal with slow clients and
<https://vxlabs.com/2015/12/08/gunicorn-as-your-django-development-server/>
- **tmux (to handle parallel and background processes)**
tmux is a software application that can be used to multiplex several virtual consoles, allowing a user to access multiple separate terminal sessions inside a single terminal window or remote terminal session. These sessions can also be kept running as background sessions in parallel, which is a requirement in many web application deployments.

Here are some helpful references and tutorials
https://gist.github.com/Atem18/4696071
https://vxlabs.com/2015/12/08/gunicorn-as-your-django-development-server/


###### Creating the database

Create an account with AWS

We will be using RDS to host our database. Create a MariaDB instance in the RDS console. Choose ap-southeast-1b as the Region.

In the navigation pane, launch a DB Instance and select MariaDB as the engine, with the most supported version (10.0.32).

Check the Publicly Accessible Box, and set Storage Size to 20GB. Choose Yes for Multi-AZ Deployment.
Enter your DB name, DB instance identifier, master username and password.
Leave the other settings as default.

Once the database is created, go to RDS Console > Parameter Groups > Create Parameter Group. Select MariaDB 10.0 as the parameter group family and give it a name and description. Select Create.

In Parameter Groups, select your newly created group and filter for the parameter 'log_bin_trust_function_creators'. Select 'Edit Parameters' and set the value to 1.

Go back to RDS Console > Instances > YourInstance. In the Details pane, note your DB name, username, password, and host endpoint. Remember this for later.

Now to connect to the database, if you have a mysql client such as SequelPro or MySQLWorkbench you can simply input the DB name, username, password, port=3306 and host endpoint into the input fields.

Otherwise, on command line you can run

`mysql -h <host endpoint> -P 3306 -u <username> -p <password>`

Make sure you have MariaDB installed. Otherwise, run

`sudo apt update -y`

`sudo apt install -y mariadb-server`

Start the MariaDB service

`sudo systemctl start mariadb.service`

`sudo systemctl enable mariadb.service`

Secure the installation of MariaDB

`sudo /usr/bin/mysql_secure_installation`

Then login to the MySQL shell:

`mysql -h <host endpoint> -P 3306 -u <username> -p <password>`

You should then be inside the MariaDB monitor. Congrats you are connected to your database!


###### Configuring the cloud host server

We will be using EC2 to host our application. Create an EC2 instance. Choose Ubuntu Server 16.04 LTS as the Amazon Machine Image. The free tier is good enough for our needs.

Under security group, make sure to open the ports for SSH (22) and HTTP (80)

Make sure to save the private key given by AWS (we will need it later to login to the server)

Before we configure our ssh settings, lets assign a IP to our AWS instance. By default, AWS will assign any available IP to the instance when it is started. The IP might change is shutdown and started again. We will associate an IP with the instance, which allows us to reserve the IP for that instance.

Go to EC2 Dashboard > Elastic IPs > Allocate new address > Allocate. You will now have a Elastic IP reserved for you use.

Go to Instances, click on your instance. Under Actions > Network > Associate Elastic IP address

At this point, if you have a domain registered you can also point the domain/subdomain to your Elastic IP. Check your domain registrar for more instructions. (I use [Namecheap](https://www.namecheap.com/))

Before we connect to the server we need to configure the permission of the private key to prevent it being accessed by other users. Move the private key to the `~/.ssh` folder and execute the following command.

`$ chmod 600 ~/.ssh/your_private_key`

Now to connect to ur server. Go to your command line and type

`$ ssh -i ~/.ssh/your_private_key ubuntu@your_elasticip`

Alternatively create a file named `config` in the `~/.ssh` folder and populate it with the following.

```
Host your_elastic_ip
  Port 22
  IndentityFile ~/.ssh/your_private_key
```
If you have a domain add another record for your domain.

```
Host your_domain
  Port 22
  IndentityFile ~/.ssh/your_private_key
```

Now you can `$ ssh ubuntu@your_elasticip` or `$ ssh ubuntu@your_domain` to connect to your server!


Setup server

`$ sudo apt update`

`$ sudo apt upgrade`

Install python packages. `virtualenv` is manage your python environments, while `virtualenvwrapper` (optional) is a really convenient wrapper to easily setup virtual environments.

`$ sudo apt install python-pip`

`$ sudo apt install python3-dev`

`$ sudo apt install libmysqlclient-dev`

`$ sudo pip install virtualenv virtualenvwrapper`

Add the following lines to your `~/.bashrc` file

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

And restart it

`$ source ~/.bashrc`

Now create ur virtualenv (assuming python3)

`$ mkvirtualenv --python=/usr/bin/python3 your_app`

Download your application and install your requirements

`$ git clone your_app`

`$ cd your_app`

`$ pip install -r path/to/requirements/file`

Test your server (make sure to change ur settings for your database to the one hosted on aws)

`$ python manage.py runserver`

Now install nginx

`$ sudo apt install nginx`

Configure nginx

`$ sudo rm /etc/nginx/sites-enabled/default`

`$ sudo vim /etc/nginx/sites-available/your_app`

Paste in the below. DNS name is either your elastic IP or the domain that points to your elastic IP.

```
server {
    listen       80;
    server_name  your_dnsname_here;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

If your backend is communicating with a frontend, you need to enable cors headers for the domain of your frontend

```
server {
       listen 80;
       server_name api.contikey.com;

       location / {

           set $cors '';
           if ($http_origin ~ '^https?://(localhost|www\.<domain>\.com|<domain>\.com)') {
                   set $cors 'true';
           }

          if ($cors = 'true') {
                  add_header 'Access-Control-Allow-Origin' "$http_origin" always;
                  # add_header 'Access-Control-Allow-Credentials' 'true';
                  add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, OPTIONS' always;
                  add_header 'Access-Control-Allow-Headers' 'Accept,Authorization,Cache-Control,Content-Type,DNT,If-Mo    fied-Since,Keep-Alive,Origin,User-Agent,X-Requested-With' always;
                  # required to be able to read Authorization header in frontend
                  #add_header 'Access-Control-Expose-Headers' 'Authorization' always;
          }

          proxy_pass http://127.0.0.1:8000;
      }
  }
```

`$ sudo ln -s /etc/nginx/sites-available/your_app /etc/nginx/sites-enabled/`

`$ sudo nginx -t`

`$ sudo systemctl restart nginx`

Install gunicorn and run application (Make sure wsgi.py file is serving your production database)

`$ pip install guincorn`

`$ gunicorn dboard.wsgi:application - bind 127.0.0.1`

If you visit your Elastic IP/domain you should now see your application running!

However this requires you to be connected to the server to run it. To solve, this we use `tmux`. Tmux is a package which turns your command line into a terminal. However, the feature we will be using today is the ability of it to run sessions. It allows you leave a session running that you can detach from, but the session will still continue executing its tasks. This allows you to easily spin up servers/execute long running tasks (eg. running a ML model). `Cntrl-C` to stop the application that is running and open up `tmux`

`$ tmux`

`$ gunicorn dboard.wsgi:application - bind 127.0.0.1`

`<Cntrl-B d>`

And you are done! The application is running the same way as before, but you can log out of your server and the application will still be running. Cool!

If you ever want to attach back to the tmux session:

`tmux attach -t <session>`

Check out more commands for tmux [here](http://www.dayid.org/comp/tm.html)

Thats all from us here at contikey, if you liked it and want to see what we cooked up this term - check it out [here](http://www.contikey.com)

If you have any questions - feel free to ask to us!

Joe Ng, Pammela Ng, Stanley Nguyen, Teo Si-Yan, Vivek Kalyan
