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
from cayenneLPP.CayenneLPP import CayenneLPP

pycom.heartbeat(False)
##################


pycom.rgbled(0x006000)
time.sleep(3)

# wifi_connect(pwd='tupueslechien')



# l = getLora()
pycom.rgbled(0x00B000)
time.sleep(3)
# s = getSocket()


while True:

    time.sleep(30)

    pycom.rgbled(0x00FF00)
    time.sleep(1)
    pycom.rgbled(0x000000)

    # Send (with abp) packet to the (first) homeserver
    abp(address = '00124f11',
        networkSessionKey = '844a432a89b1b23598e4d24d631a9248',
        applicationSessionKey = '3f1807cd4c7817144147a48b4ec93648',
        value=True)

    time.sleep(14)


    # Send (with abp) packet to the *second* homeserver
    abp(address = '00521fb0',
        networkSessionKey = '441b7b16eb5585fe7214d2631681db09',
        applicationSessionKey = '7b8a3f397458d23214025b38f389dfe7',
        value=False)


    time.sleep(14)




#
# while True:
#
#     if (not l.has_joined()):
#         pycom.rgbled(0xFF0000) #
#         time.sleep(6)
#         pycom.rgbled(0x000000) #
#         time.sleep(2)
#         continue
#
#     pycom.rgbled(0x0000FF) #
#     time.sleep(1)
#
#     # creating Cayenne LPP packet
#     lpp = CayenneLPP(size = 100, sock = s)
#
#     # adding 2 digital outputs, the first one uses the default channel
#     #lpp.add_digital_input(True)
#     lpp.add_digital_input(False, channel = 68)
#
#     # sending the packet via the socket
#     lpp.send()
#
#     pycom.rgbled(0x007f00) # green
#     time.sleep(1)
#
#     pycom.rgbled(0x000000) # green
#     time.sleep(28)
