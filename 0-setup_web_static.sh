#!/usr/bin/env bash
# making the needed directories
if [ ! -x /usr/sbin/nginx ]; then
        sudo apt-get -y update
        sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
fakehtml="this is fake yall"
echo "$fakehtml" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
static="\\\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}"
sudo sed -i "36i $static" /etc/nginx/sites-enabled/default
sudo service nginx restart
