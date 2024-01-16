# Raspberry Pi 4B PhotoResistor(light sensor)
## Environment
Device : Raspberry Pi 8GB</br>
SD Card : 32GB</br>
OS : Raspberry Pi OS(64-bit), Released Date :2023.12.05</br>
## Installation
### Install dependencies
    $ sudo raspi-config
    # 3. Interface Options
    # I4 SPI - Enable
    $ sudo vim /etc/modules
    # add spidev
    $ sudo git clone https://github.com/Gadgetoid/py-spidev.git
    $ cd py-spidev
    $ sudo python setup.py install
