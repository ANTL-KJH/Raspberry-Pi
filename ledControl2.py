import RPi.GPIO as GPIO


class LEDDimmingController:
    def __init__(self):
        self.ledPin = 12  # PWM0
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ledPin, GPIO.OUT)
        self.pwmLED = GPIO.PWM(self.ledPin, 500)
        self.pwmLED.start(100)

    def runLedDimming(self):
        while True:
            duty = int(input("Brightness (0 to 100) :"))
            if duty == -1:
                GPIO.cleanup()
                break
            self.pwmLED.ChangeDutyCycle(duty)


def main():
    LEDController = LEDDimmingController()
    LEDController.runLedDimming()


if __name__ == "__main__":
    main()
