#!/usr/bin/env python
# import os

import bluepy.btle as ble

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

devs = scanner.scan(2)

for dev in devs:
    if dev.addr == "ac:23:3f:25:a1:06":
        print(dev.addr, "acquired data:")
        print(dev.getScanData())
