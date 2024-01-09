import time
import board    # 데이터 송신용 board 모듈 (GPIO.setmode의 board 모드 아님)
import adafruit_dht

mydht11 = adafruit_dht.DHT11(board.D6)  # GPIO06 번 핀

# try:
#     while True:
#         humidity_data = mydht11.humidity
#         temperature_data = mydht11.temperature
#         print(humidity_data, temperature_data)
#         time.sleep(2)   # 대기시간이 2초 필요 - 센서 내부에서 초기화작업시 필요한 시간
# except RuntimeError as error:
#     print(error.args[0])
# finally:
#     pass

while True:
    try:
        humidity_data = mydht11.humidity
        temperature_data = mydht11.temperature
        print(humidity_data, temperature_data)
        time.sleep(2)   # 대기시간이 2초 필요 - 센서 내부에서 초기화작업시 필요한 시간
    except RuntimeError as error:
        print(error.args[0])
    finally:
        pass