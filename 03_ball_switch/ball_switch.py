import RPi.GPIO as GPIO
import time

switch_pin = 17

try:

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(switch_pin, GPIO.IN)

  while True:
    if GPIO.input(switch_pin):
      print("Ball is HIGH")
    else:
      print("Ball is LOW")

    time.sleep(0.1)

except KeyboardInterrupt:
  print("Keyboard interrupt")
finally:
  GPIO.cleanup()