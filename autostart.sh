#!/usr/bin/env bash

sudo cp recorder.service /lib/systemd/system/recorder.service
sudo systemctl daemon-reload
sudo systemctl enable recorder.service

echo "Reboot with 'sudo reboot'."
