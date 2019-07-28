# main.py -- put your code here!

from base_utils import *
from utils import *
from network import WLAN
from network import LoRa
import socket
import time
import binascii
import ubinascii
import machine
import struct
import pycom

pycom.heartbeat(False)
##################


pycom.rgbled(0x006000)
time.sleep(3)

# wifi_connect(pwd='tupueslechien')
l = getLora()
pycom.rgbled(0x00B000)
time.sleep(3)
s = getSocket()
pycom.rgbled(0x00FF00)
time.sleep(3)

while True:

    if (not l.has_joined()):
        pycom.rgbled(0xFF0000) #
        time.sleep(6)
        pycom.rgbled(0x000000) #
        time.sleep(2)
        continue

    pycom.rgbled(0x0000FF) #
    time.sleep(1)
    s.send(bytes([0x01, 0x02, 0x03]))

    pycom.rgbled(0x007f00) # green
    time.sleep(1)

    pycom.rgbled(0x000000) # green
    time.sleep(28)
