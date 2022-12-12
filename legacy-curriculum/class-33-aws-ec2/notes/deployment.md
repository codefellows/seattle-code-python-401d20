# Deploying a containerized Django application to AWS EC2
The application we're deploying today consists of three separate containers, all being built and configured with Docker Compose. We'll be configuring an EC2 instance to continuously run these containers (Django Web App, PostgreSQL, Redis) when the EC2 instance starts/reboots. In addition, we'll be using Nginx as a proxy server for providing access to our static resources on the EC2 instance.

_NOTE:_ These steps assume that you've already configured a containerized application using `docker-compose.yml`. You already have a functional Django application that utilizes Redis for caching and PostgreSQL for data persistence.

## On AWS
_You can skip some of these steps if you already have the instances created._

1. Create a new EC2 instance.
     - Choose the Ubuntu Server 18.04 from the free tier 
        - You may choose whichever AMI you prefer, though, depending on the Linux distribution, your commands may differ than those in this file.
     - Continue through the launch pages to the the security group settings
     - Use a security group with access to SSH and HTTP, preferably one that's specific to this application
        - _Note: You should usually NOT reuse security groups between different projects._
     - Launch the instance
        - When launching, create a new key pair (name it appropriate for this project) and download it to your machine

1. Set up SSH shortcut for the EC2 instance.
     - Move the downloaded key pair `.pem` file to `~/.ssh` on your machine
     - Change the permissions for the `.pem` file to remove public access
        ```sh
        $ chmod 400 ~/.ssh/(key name).pem
        ```

     - Create a `config` file in `~/.ssh` (if you don't already have one) and add the instance details for this project.

        ```ini
        # config
        
        Host (shortcut name)
            Hostname (EC2 public DNS)
            User ubuntu
            IdentityFile ~/.ssh/(key name).pem
        ```


1. SSH into EC2 instance using `ssh (shortcut name)`
    - You will need to confirm the prompt and add this instance to your `known hosts` before the connecting will succeed

## Set up your EC2 Instance
1. Update the `apt-get` package registry on this machine using `sudo apt-get update`

### Install & Configure Nginx
1. Install the Nginx software on your instance using `sudo apt-get install nginx -y` 

#### Nginx Restart Fix
1. _NOTE: The following steps are a fix which allow us to successfully restart Nginx on the instance after updating the configuration files. Without this fix, a full reboot of the instance is required to successfully restart Nginx._
```bash
sudo mkdir /etc/systemd/system/nginx.service.d
sudo nano /etc/systemd/system/nginx.service.d/override.conf
```
Then add the following line to that file. Save and close.
```
[Service]
ExecStartPost=/bin/sleep 0.1
```
Then run:
```bash
sudo systemctl daemon-reload
```

#### Nginx Proxy Configuration
1. Add `default` Nginx config to `/etc/nginx/sites-enabled/default`, save and close
```nginx
server {
    listen 80;
    server_name ~^(.+)$;
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    location /static {
        autoindex on;
        root /static;
    }

    location / {
        proxy_pass http://0.0.0.0:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-for $proxy_add_x_forwarded_for;
    }
}
```
    
1. Update the primary Nginx configuration file using `sudo nano /etc/nginx/nginx.conf`
    - Uncomment the `server_names_hash_bucket_size` directive, and change the value from 64 to 128
    - Save and close
1. Restart Nginx using `sudo systemctl restart nginx`
1. Verify that Nginx has restarted and is "Started" using`sudo systemctl status nginx`
```sh
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
  Drop-In: /etc/systemd/system/nginx.service.d
           └─override.conf
   Active: active (running) since Thu 2018-11-15 18:35:10 UTC; 53min ago
     Docs: man:nginx(8)
  Process: 2439 ExecStop=/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid (co
  Process: 2495 ExecStartPost=/bin/sleep 0.1 (code=exited, status=0/SUCCESS)
  Process: 2489 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
  Process: 2476 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/
 Main PID: 2494 (nginx)
    Tasks: 2 (limit: 1152)
   CGroup: /system.slice/nginx.service
           ├─2494 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─2496 nginx: worker process

Nov 15 18:35:10 ip-172-31-39-178 systemd[1]: Stopped A high performance web server and a reverse proxy serv...
Nov 15 18:35:10 ip-172-31-39-178 systemd[1]: Starting A high performance web server and a reverse proxy ser...
Nov 15 18:35:10 ip-172-31-39-178 systemd[1]: Started A high performance web server and a reverse proxy serv...
lines 1-20/20 (END)
```


### Clone Project from GitHub
1. Clone repo from GH (have username and password handy)
    - `git clone <URL.git> src`
    - `cd src`
    - add a `.env` to this directory (copy pasta the same ENV file we've used locally) using `sudo nano .env` 
        - _Note: Add EC2 DNS to `ALLOWED_HOSTS` in .env_
        - Save and close

### Install & Configure Docker
1. Install Docker using `sudo apt-get install docker.io -y`
1. Start the Docker daemon using `sudo systemctl start docker`
1. Enable the Docker service using `sudo systemctl enable docker`
1. Check that Docker is installed and returns valid information using `docker --version`
```sh
~$ sudo docker --version
Docker version 18.06.1-ce, build e68fc7a
```

### Install & Configure Docker Compose
1. Install [Docker Compose](https://docs.docker.com/compose/install/#install-compose)
    - We build this from source to ensure we have the most recent version
    - Select the Linux installation and copy the installation command to the shell on EC2 
        - _Example:_ `sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
1. Change Docker Compose permissions using `sudo chmod +x /usr/local/bin/docker-compose`
1. Check that Docker Compose is installed and returns valid information using `sudo docker-compose --version`
```sh
~$ sudo docker-compose --version
docker-compose version 1.23.1, build b02f1306
```

### Setup Crontab Job
The following steps will set up a Cron job for building and running your Docker Compose configuration:

1. Issue a Cron job event-based script using `crontab -e`
1. Select Nano as your editor at the next prompt
1. Add `@reboot /home/ubuntu/compose_run.sh` to the file, then save and close
1. From `/home/ubuntu/` run `sudo nano compose_run.sh`, and add the following to this file, save and close:
```bash
#! /bin/bash

set -e

cd /src
git checkout class33 &&
git pull origin class33

sudo docker-compose up --build
```

1. `exit` SSH connection
1. Reboot the EC2 instance from the AWS EC2 console to trigger the build process
1. Once the build is complete, you may see the following when you load the EC2 DNS in your browser window:
    - This is dependent on how your Django application is built...

-----

## Not Found
The requested URL / was not found on this server.

-----
_NOTE: This means that the web application is up and running, but we have not loaded any records into the DB yet._ 

### (Optional) Seed the Database from your .csv file
1. Shell into your Docker Web App container using `sudo docker exec -it <name> bash` 
    - _NOTE:_ You need to use the name of your container in this command
1. Run a script to load your database using `python load_db.py` (You need to write this script. I use a SQLAlchemy engine to connect to the DB)
1. `exit` to return to your EC2 SSH shell
1. Refresh the browser window and you should see your application data rendering on the page
    - Also make note that your styles are loading from the static assets directory 
    
# REJOICE!
