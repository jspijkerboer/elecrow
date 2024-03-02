import RPi.GPIO as GPIO
import time

button_pin = 17

def button_press(channel):
  if GPIO.input(channel):
    print("Button pressed")
  else:
    print("Button released")

try:

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=button_press)

  while True:
    time.sleep(0.1)

except:
  print("")
finally:
  GPIO.cleanup()