#!/usr/bin/env bash
# Install nginx and prepare web server for static code deloyment

# nginx installation
sudo apt-get update
sudo apt-get -y install nginx

# create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# create index.html and symlink
sudo echo -e "Hello World" | sudo tee "/data/web_static/releases/test/index.html"
sudo ln -sf "/data/web_static/current" "/data/web_static/releases/test/"

# change owners and alter config file, then restart nginx
sudo chown -R ubuntu:ubuntu "/data/"
sudo sed -i "29i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}" "/etc/nginx/sites-available/default"
sudo service nginx restart
