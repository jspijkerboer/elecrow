import RPi.GPIO as GPIO
import time


class Buzzer(object):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.buzzer_pin = 17
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        print("Buzzer ready")

    def buzz(self, pitch: int, duration: float):
        if (pitch == 0):
            time.sleep(duration)
            return

        period = 1.0 / pitch
        delay = period / 2
        cycles = int(duration * pitch)

        for _ in range(cycles):
            GPIO.output(self.buzzer_pin, True)
            time.sleep(delay)
            GPIO.output(self.buzzer_pin, False)
            time.sleep(delay)

    def play(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

        pitches = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1047]
        duration = 0.1
        for p in pitches:
            self.buzz(p, duration)
            time.sleep(duration * 0.5)
        for p in reversed(pitches):
            self.buzz(p, duration)
            time.sleep(duration * 0.5)


if __name__ == "__main__":
    buzzer = Buzzer()
    buzzer.play()
