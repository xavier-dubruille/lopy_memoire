#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

""" LoPy LoRaWAN Nano Gateway example usage """
import pycom
import config
import time
from nanogateway import NanoGateway

if __name__ == '__main__':

    pycom.heartbeat(False)
    pycom.rgbled(0xB00000)
    time.sleep(1)
    pycom.rgbled(0x000000)

    nanogw = NanoGateway(
        id=config.GATEWAY_ID,
        frequency=config.LORA_FREQUENCY,
        datarate=config.LORA_GW_DR,
        ssid=config.WIFI_SSID,
        password=config.WIFI_PASS,
        server=config.SERVER,
        port=config.PORT,
        ntp_server=config.NTP,
        ntp_period=config.NTP_PERIOD_S
        )

    pycom.rgbled(0x0000B0)
    time.sleep(1)
    pycom.rgbled(0x000000)


    nanogw.start()
    pycom.rgbled(0x00B000)
    time.sleep(1)
    pycom.rgbled(0x000000)
    
    nanogw._log('You may now press ENTER to enter the REPL')
    input()
