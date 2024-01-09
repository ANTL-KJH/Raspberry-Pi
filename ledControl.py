import RPi.GPIO as GPIO
import time


class piLED:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36, GPIO.OUT)    # blue
        GPIO.setup(38, GPIO.OUT)    # green
        GPIO.setup(40, GPIO.OUT)    # red
        self.redLedState = False
        self.greenLedState = False
        self.blueLedState = False

def main():
    piLEdD = piLED()
    while (True):
        GPIO.output(40, False)
        time.sleep(1)
        GPIO.output(40, True)
        time.sleep(1)

if __name__ == "__main__":
    main()

