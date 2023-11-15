# Raspberry Pi 4B fcitx-Korean Installation
## Environment
Device : Raspberry Pi 8GB</br>
SD Card : 32GB</br>
OS : Raspberry Pi OS(64-bit), Released Date :2023.05.03</br>
## Installation
### Install dependencies
    $ sudo apt update
    $ sudo apt upgrade
    $ sudo apt -y install vim fcitx-hangul fonts-unfonts-core
### Set Environment
    $ sudo vim /etc/default/im-config
    IM_CONFIG_DEFAULT_MODE=fcitx
    $ im-config -a
    Click OK - Yes
    Choose default
    Click OK - OK
## After Reboot
    $ sudo reboot now
    PI menu - Perferences - Fcitx Configuration - Input Method - + - Search Hangul and Add
    Global config - Trigger Input Method - Input(Kor/eng)
