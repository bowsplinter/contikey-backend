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

Now to connect to ur server. Go to your command line and type

`ssh -i /path/to/privatekey ubuntu@your_elasticip`

Alternatively move the private key to `~/.ssh` and create a file named `config` in that folder. Add the following to it

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

Now you can `ssh ubuntu@your_elasticip` or `ssh ubuntu@your_domain` to connect to your server!
