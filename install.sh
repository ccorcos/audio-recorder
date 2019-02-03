#!/usr/bin/env bash

# Install mp3 compression
sudo apt-get install lame

# Setup dropbox
curl "https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh" -o dropbox_uploader.sh;
chmod +x dropbox_uploader.sh;
./dropbox_uploader.sh;