
from network import WLAN
import socket
import time
import binascii
import machine
import pycom

def wifi_connect(ssid='Batcave', pwd='tupueslechien'):
    wlan = WLAN(mode=WLAN.STA)
    nets = wlan.scan()
    for net in nets:
        if net.ssid == ssid:
            print('Network found!')
            wlan.connect(net.ssid, auth=(net.sec, pwd), timeout=5000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print('WLAN connection succeeded!')
            break

def xblink(heartbeat=False):
    pycom.heartbeat(heartbeat)
    if heartbeat:
        return
    for cycles in range(15): # stop after n cycles
        pycom.rgbled(0x007f00) # green
        time.sleep(5)
        pycom.rgbled(0x7f7f00) # yellow
        time.sleep(1.5)
        pycom.rgbled(0x7f0000) # red
        time.sleep(4)
