import RPi.GPIO as GPIO
import datetime
import time
import subprocess
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

def ledOn():
    GPIO.output(18, False)

def ledOff():
    GPIO.output(18, True)

def blink():
    ledOn()
    time.sleep(0.2)
    ledOff()
    time.sleep(0.2)
    ledOn()
    time.sleep(0.2)
    ledOff()
    time.sleep(0.2)

class Recorder:    
    def wait(self):
        print "Waiting..."
        ledOff()
        while True:
            if GPIO.input(25):
                time.sleep(0.2)
                break
            else:
                time.sleep(0.2)
        self.record()

    def record(self):
        fileName = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + ".mp3"
        print "Recording " + fileName
        
        cmd = "arecord --quiet --device plughw:USB --format cd " + fileName
        process = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True)

        while True:
            if GPIO.input(25):
                ledOn()
                time.sleep(0.1)
            else:
                break

        process.kill()

        
        blink()
        
        print "Uploading " + fileName
        os.system("./dropbox_uploader.sh -f /home/pi/.dropbox_uploader upload " + fileName + " " + fileName)
        os.system("rm -f " + fileName)

        blink()
        
        self.wait()

recorder = Recorder()
blink()
recorder.wait()
