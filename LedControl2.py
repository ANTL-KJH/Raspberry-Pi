import RPi.GPIO as GPIO

ledPin = 12 # PWM0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

pwmLED=GPIO.PWM(ledPin,500)
pwmLED.start(100)

while True:
    duty = int(input("Brightness (0 to 100) :"))
    if duty == -1:
        GPIO.cleanup()
        break
    pwmLED.ChangeDutyCycle(duty)