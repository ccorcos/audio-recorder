#!/usr/bin/env bash

sudo apt-get install lame

curl "https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh" -o dropbox_uploader.sh;
chmod +x dropbox_uploader.sh;

# Setup wizard
./dropbox_uploader.sh;