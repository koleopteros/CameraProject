import RPi.GPIO as GPIO
import booth_class
import time

booth = Booth()

def button_callback(channel):
	booth.take_photo(5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)