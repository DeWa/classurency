# Classurency

Create your own currency and banking system to credit your students

## Installation

Install dependencies of Python packages
```sh
sudo apt install clang build-essential python3-dev
```
Install Kivy dependencies
```sh
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev mesa-common-dev
```

# Misc

Poetry can sometimes freeze when fetching packages on Raspberry Pi. This config should fix that:
```sh
poetry config keyring.enabled false
```