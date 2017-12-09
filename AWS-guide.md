# Agile Devops

This is a simple guide to get your Django application hosted on AWS for free. Note: this is not a guide to deploy an application to production, check out [this link](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/) for that. Rather, this is to setup a server on AWS quickly and efficiently for prototyping and testing purposes (agile!).

Create an account with AWS

<DB INSTRUCTIONS>

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
