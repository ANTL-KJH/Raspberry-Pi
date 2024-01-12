import RPi.GPIO as GPIO


class LEDDimmingController:
    def __init__(self):
        self.redLedPin = 12  # PWM0 red
        self.redLedPin = 32  # PWM0 green
        self.redLedPin = 33  # PWM0 blue
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.redLedPin, GPIO.OUT)
        self.pwmRedLed = GPIO.PWM(self.redLedPin, 500)
        self.pwmRedLed.start(100)
        self.pwmGreenLed = GPIO.PWM(self.redLedPin, 500)
        self.pwmGreenLed.start(100)
        self.pwmBlueLed = GPIO.PWM(self.redLedPin, 500)
        self.pwmBlueLed.start(100)

    def runLedDimming(self):
        while True:
            redDuty, greenDuty, blueDuty = map(int, input("Brightness red, green, blue :"))
            self.pwmRedLed.ChangeDutyCycle(redDuty)
            self.pwmGreenLed.ChangeDutyCycle(greenDuty)
            self.pwmBlueLed.ChangeDutyCycle(blueDuty)

def main():
    LEDController = LEDDimmingController()
    LEDController.runLedDimming()


if __name__ == "__main__":
    main()
