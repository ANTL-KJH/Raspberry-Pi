# Raspberry Pi 4B AP Mode
## Environment
Device : Raspberry Pi 8GB</br>
SD Card : 32GB</br>
OS : Raspberry Pi OS(64-bit), Released Date :2023.05.03</br>
## Installation
### Install dependencies
    $ sudo apt update
    $ sudo apt upgrade
    $ sudo apt install -y hostapd dnsmasq vim
### Set Environment
    $ sudo vim /etc/dhcpcd.conf
### 파일의 마지막에 아래 내용 추가
    interface wlan0
    static ip_address=192.168.32.1/24
    nohook wpa_supplicant
### Set Environment
    $ sudo vim /etc/dnsmasq.conf
### 파일의 마지막에 아래 내용 추가
    interface=wlan0
    dhcp-range=192.168.32.2,192.168.32.10,255.255.255.0,24h
    domain=wlan
    address=/gw.wlan/192.168.32.1
### Set WiFi Environment
    $ sudo vim /etc/hostapd/hostapd.conf
### 파일에 아래 내용 추가
    country_code=AD
    interface=wlan0
    ssid=antl-kjh        # WiFi Name
    hw_mode=a            # a(5GHz),b/g(2.4GHz)
    channel=36           # 2.4GHz 대역 사용시 14 미만으로 설정 ex) 7
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    wpa=2
    wpa_passphrase=12345678  # password
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP
    rsn_pairwise=CCMP
### Reboot
    $ sudo reboot
### daemon Setting
    $ sudo systemctl unmask hostapd.service
    $ sudo systemctl unmask dnsmasq
    $ sudo systemctl start hostapd
    $ sudo systemctl start dnsmasq
### Reboot
    Finish
