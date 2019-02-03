import RPi.GPIO as GPIO
import datetime
import time
import subprocess
import signal
import os

# Change directory to the current file.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

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
    time.sleep(0.1)
    ledOff()
    time.sleep(0.1)
    ledOn()
    time.sleep(0.1)
    ledOff()
    time.sleep(0.1)
    ledOn()
    time.sleep(0.1)
    ledOff()
    time.sleep(0.1)

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
        cmd = "arecord --quiet --device plughw:USB --format cd | lame -x - " + fileName

        # https://stackoverflow.com/a/4791612/1191551
        process = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 

        while True:
            if GPIO.input(25):
                ledOn()
                time.sleep(0.1)
            else:
                break

        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        
        blink()
        ledOn()
        
        print "Uploading " + fileName
        os.system("./dropbox_uploader.sh -f /home/pi/.dropbox_uploader upload " + fileName + " recordings/" + fileName)
        os.system("rm -f " + fileName)

        blink()
        ledOff()
        
        self.wait()

recorder = Recorder()
blink()
ledOff()
recorder.wait()
