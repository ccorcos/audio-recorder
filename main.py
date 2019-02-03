import RPi.GPIO as GPIO
import datetime
import time
import subprocess
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

class Recorder:    
    def wait(self):
        print "Waiting..."
        GPIO.output(18, False)
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
                GPIO.output(18, True)
                time.sleep(0.2)
            else:
                break

        GPIO.output(18, False)
        process.kill()
        
        print "Uploading " + fileName
        os.system("./dropbox_uploader.sh upload " + fileName + " " + fileName)

        for i in range(6):
            GPIO.output(18, i % 2 == 0)
            time.sleep(0.3)

        wait()

recorder = Recorder()
recorder.wait()