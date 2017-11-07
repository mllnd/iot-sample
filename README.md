# iot-sample

Resource for launching a basic IoT scenario with WeMos D1 microcontroller

## Dependencies

* esptool - `pip install esptool`
* ampy - `pip install adafruit-amp`
* picocom
* python 3.x

## Installation & usage

### Installation

Clone the repository to a desired place with `git clone` command.

### Usage

You can quickstart by running the Makefile with `make` command. This will perform basic setup for WeMos board and will connect you to it.

**Note:** this will assume that you have WeMos board already connected to your machine and an IoT socket server up and running.

If you want to try the scenario on your machine without the WeMos board, run
```sh
python main.py
```
and then browse http://localhost:8080/.
