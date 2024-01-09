import RPi.GPIO as GPIO
import time

REDPIN = 40
GREENPIN = 38
BLUEPIN = 36


class LEDController:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(36, GPIO.OUT)  # blue
        GPIO.setup(38, GPIO.OUT)  # green
        GPIO.setup(40, GPIO.OUT)  # red
        self.redLedState = False
        self.greenLedState = False
        self.blueLedState = False

    def changeRedState(self):
        if self.redLedState == False:
            self.redLedState = True
            GPIO.output(REDPIN, True)
        else:
            self.redLedState = False
            GPIO.output(REDPIN, False)

    def changeGreenState(self):
        if self.greenLedState == False:
            self.greenLedState = True
            GPIO.output(GREENPIN, True)
        else:
            self.greenLedState = False
            GPIO.output(GREENPIN, False)

    def changeBlueState(self):
        if self.blueLedState == False:
            self.blueLedState = True
            GPIO.output(BLUEPIN, True)
        else:
            self.blueLedState = False
            GPIO.output(BLUEPIN, False)

    def changeAllState(self, color):
        if color == 'R':
            self.changeRedState()
        elif color == 'G':
            self.changeGreenState()
        elif color == 'B':
            self.changeBlueState()


def main():
    ledControl = LEDController()



if __name__ == "__main__":
    main()
