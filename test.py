import RPi.GPIO as GPIO
from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import time
import uvicorn

class LEDDimmingController:
    def __init__(self):
        self.redLedPin = 12  # PWM0 red
        self.greenLedPin = 32  # PWM0 green
        self.blueLedPin = 33  # PWM0 blue
        self.redduty = 100
        self.greenduty = 100
        self.blueduty = 100
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.redLedPin, GPIO.OUT)
        GPIO.setup(self.greenLedPin, GPIO.OUT)
        GPIO.setup(self.blueLedPin, GPIO.OUT)
        self.pwmRedLed = GPIO.PWM(self.redLedPin, 1000)
        self.pwmRedLed.start(100)
        self.pwmGreenLed = GPIO.PWM(self.greenLedPin, 1000)
        self.pwmGreenLed.start(100)
        self.pwmBlueLed = GPIO.PWM(self.blueLedPin, 1000)
        self.pwmBlueLed.start(100)

    def setLedDuty(self, color, duty):
        if duty == -1:
            GPIO.cleanup()
            return
        if color == 'R':
            self.redduty = duty
            self.pwmRedLed.ChangeDutyCycle(duty)
        elif color == 'G':
            self.greenduty = duty
            self.pwmGreenLed.ChangeDutyCycle(duty)
        elif color == 'B':
            self.blueduty = duty
            self.pwmBlueLed.ChangeDutyCycle(duty)


app = FastAPI()
LEDController = LEDDimmingController()


@app.get("/api/LED", response_class=PlainTextResponse)
async def handle(color: str = Query(..., title="Color"), value: int = Query(..., title="value")):
    LEDController.setLedDuty(color, value)
    return "hello"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
