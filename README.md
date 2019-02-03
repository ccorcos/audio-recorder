# Audio Recorder

A simple script for recording on the Raspberry Pi and uploading to Dropbox.

## Getting Started

Clone this repo into your Pi. Install and setup Dropbox:

```sh
./install.sh
```

Setup your timezone!

```sh
dpkg-reconfigure tzdata
```

Run the program to test it out

```sh
python main.py
```

Setup to run on boot.

```sh
./autostart.sh
```