# Utilities for capturing images

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup of the GPIO pins
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def turn_lamp_on():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.HIGH)

def turn_lamp_off():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    
def test_camera():
    camera = PiCamera()
    camera.start_preview()
    sleep(10)
    camera.stop_preview()

if __name__ == "__main__":
    turn_lamp_on()
    sleep(10)
    test_camera()
    turn_lamp_off()


    
# def capture(save_dir):
    
