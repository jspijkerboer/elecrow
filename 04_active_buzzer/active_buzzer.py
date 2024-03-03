import RPi.GPIO as GPIO
import time

buzzer_channel = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_channel, GPIO.OUT)

GPIO.output(buzzer_channel, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(buzzer_channel, GPIO.LOW)

GPIO.cleanup()