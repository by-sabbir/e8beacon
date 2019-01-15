#!/usr/bin/env python
import os
from bluepy.btle import Scanner, DefaultDelegate


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device"), dev.addr
        elif isNewData:
            print("Received new data from", dev.addr)


scanner = Scanner().withDelegate(ScanDelegate())


def cmd(command):
    os.system(command)


def lock():
    cmd("xdotool key Ctrl+alt+l")


def unlock():
    cmd("xdotool type ./")
    # time.sleep(.3)
    cmd("xdotool key Return")


def main():
    locked = 0
    while True:
        devices = scanner.scan(3.0)
        for dev in devices:
            if dev.addr == "ac:23:3f:25:a1:06":
                print(dev.rssi, type(dev.rssi))
                if dev.rssi < -65:
                    lock()
                    locked = True
                else:
                    if locked is True:
                        unlock()
                        locked = False


if __name__ == '__main__':
    main()
