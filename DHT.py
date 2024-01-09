import time
import board    # 데이터 송신용 board 모듈 (GPIO.setmode의 board 모드 아님)
import adafruit_dht


class DHTController:
    def __init__(self):
        self.dht11 = adafruit_dht.DHT11(board.D26)  # GPIO26 번 핀
    def runDHT11(self):
        while True:
            try:
                humidity_data = self.dht11.humidity
                temperature_data = self.dht11.temperature
                print("humidity : {}, temperature : {}".format(humidity_data, temperature_data))
                time.sleep(2)  # 대기시간이 2초 필요 - 센서 내부에서 초기화작업시 필요한 시간
            except RuntimeError as error:
                print(error.args[0])
            finally:
                pass
def main():
    dhtController = DHTController()
    dhtController.runDHT11()

