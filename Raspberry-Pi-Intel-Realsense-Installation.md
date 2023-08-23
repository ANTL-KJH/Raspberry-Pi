# Raspberry Pi 4B Intel Realsense Installation
## Environment
Device : Raspberry Pi 8GB</br>
SD Card : 32GB</br>
OS : Raspberry Pi OS(64-bit), Released Date :2023.05.03
## Installation
### Install dependencies
    $ sudo apt -y install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at python3-pybind11 pybind11-dev cmake vim
### Download file
    $ wget https://github.com/IntelRealSense/librealsense/archive/v2.54.1.tar.gz
    $ tar xf v2.54.1.tar.gz
    $ cd librealsense-2.54.1
### Update udev rule
    $ sudo ./scripts/setup_udev_rules.sh
### Build
    $ mkdir build && cd build
    $ cmake .. \-DBUILD_PYTHON_BINDINGS=ON -DBUILD_WITH_OPENMP=ON-DCMAKE_BUILD_TYPE=Release -DFORCE_RSUSB_BACKEND=true
    $ make -j4
    $ sudo make install
### Reboot
    $ sudo reboot now
