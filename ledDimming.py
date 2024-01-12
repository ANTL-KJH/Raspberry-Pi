import RPi.GPIO as GPIO


class LEDDimmingController:
    def __init__(self):
        self.redLedPin = 12  # PWM0 red
        self.greenLedPin = 32  # PWM0 green
        self.blueLedPin = 33  # PWM0 blue
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.redLedPin, GPIO.OUT)
        GPIO.setup(self.greenLedPin, GPIO.OUT)
        GPIO.setup(self.blueLedPin, GPIO.OUT)
        self.pwmRedLed = GPIO.PWM(self.redLedPin, 500)
        self.pwmRedLed.start(100)
        self.pwmGreenLed = GPIO.PWM(self.greenLedPin, 500)
        self.pwmGreenLed.start(100)
        self.pwmBlueLed = GPIO.PWM(self.blueLedPin, 500)
        self.pwmBlueLed.start(100)

    def setLedDuty(self, color, duty):
        if color == 'R':
            self.pwmRedLed.ChangeDutyCycle(duty)
        elif color == 'G':
            self.pwmGreenLed.ChangeDutyCycle(duty)
        elif color == 'B':
            self.pwmBlueLed.ChangeDutyCycle(duty)

    def runLedDimming(self):
        while True:
            c, d = input("color, duty").split()
            self.setLedDuty(c, int(d))


def main():
    LEDController = LEDDimmingController()
    LEDController.runLedDimming()


if __name__ == "__main__":
    main()
