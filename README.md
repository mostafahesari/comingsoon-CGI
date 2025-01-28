# comingsoon-CGI
todo:

- [ ] using databse instead of writing to file
- [ ] sending subscription email 
- [ ] considering security!
- [ ] use env var istead of hardcode config

## Setting up CGI Python with Nginx on Ubuntu Server

clone this directory
```bash
git clone https://github.com/mostafahesari/comingsoon-CGI.git
cd comingsoon-CGI
```
the follow the steps.
### 1. Install Required Packages
```bash
sudo apt update
sudo apt install nginx python3 fcgiwrap
```

### 2. Configure Nginx

Nginx configuration:

Option1:

change the server name/IP in the config regarding your IP/domain
```bash
sudo cp ./comingsoon /etc/nginx/sites-available/
sudo vim /etc/nginx/sites-available/comingsoon
```
enable and test it
```bash
sudo ls -s /etc/nginx/sites-available/comingsoon /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Option2:

Or,
set it as your default Nginx config (I did it!) no further change needed( careful may cause conflict)

```bash
sudo cp ./comingsoon /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl restart nginx
   ```


### 3. Set Up CGI 

```bash
sudo mkdir -p /var/www/cgi-bin
sudo chown www-data:www-data /var/www/cgi-bin
sudo chmod 755 /var/www/cgi-bin
```

Python script:
```bash
sudo cp subscribe.cgi /var/www/cgi-bin/
sudo chmod +x /var/www/cgi-bin/subscribe.cgi
```


Start fcgiwrap :
```bash
sudo systemctl start fcgiwrap
sudo systemctl enable fcgiwrap
```

Create files:
```bash
sudo mkdir /var/www/comingsoon
cp index.html /var/www/comingsoon/
sudo touch /var/www/comingsoon/emails.txt /var/www/comingsoon/ips.txt
sudo chmod 666 /var/www/comingsoon/emails.txt /var/www/comingsoon/ips.txt
```

Test it in a web browser 

