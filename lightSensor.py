import spidev, time


class photoResister:
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1350000

    def analog_read(self, channel):
        r = self.spi.xfer2([1, (8 + channel) << 4, 0])
        adc_out = ((r[1] & 3) << 8) + r[2]
        return adc_out

    def runPhotoResister(self):
        while True:
            reading = self.analog_read(0)
            voltage = reading * 3.3 / 1024
            reading = (reading * 100) // 1024 # for get 0 ~ 100
            print("Reading=%d\tVoltage=%f" % (reading, voltage))
            time.sleep(1)


def main():
    lightSensor = photoResister()
    lightSensor.runPhotoResister()


if __name__ == "__main__":
    main()
