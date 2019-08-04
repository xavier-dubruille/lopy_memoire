
from network import WLAN
from network import LoRa
import socket
import time
import binascii
import machine
import struct

def getLora(app_eui_ascii='0000000000000000', app_key_ascii='1b1676a831130b79ed627cd68476593e'):
    """
    tmp. don't pay attention to this.
    """

    lora = LoRa(mode=LoRa.LORAWAN)

    # create an OTAA authentication parameters
    app_eui = binascii.unhexlify(app_eui_ascii)
    app_key = binascii.unhexlify(app_key_ascii)

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    return lora

def getSocket():
    """ idem: don't pay attention to this. """
    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(False)
    return s

def otaa(app_eui_ascii='0000000000000000', app_key_ascii='1b1676a831130b79ed627cd68476593e'):
    """
    Those have already worked ? ==>
    app_eui_ascii='70B3D57ED0013FC6'
    app_key_ascii='10E76C759EACEC124FEEF90B710556EE'
    """
    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN)

    # create an OTAA authentication parameters
    app_eui = binascii.unhexlify(app_eui_ascii)
    app_key = binascii.unhexlify(app_key_ascii)

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    # wait until the module has joined the network
    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket non-blocking
    s.setblocking(False)

    # send some data
    while True:
        try:
            s.send(bytes([0x01, 0x02, 0x03]))

            # get any data received...
            data = s.recv(64)
            if len(data) > 0:
                print(data)
        except:
            pass
    time.sleep(2.5)

def abp():
    address = '061010C7'
    applicationSessionKey = '80974D854F4D0328646E02F9823703C4'
    networkSessionKey = 'E397B3E73863FFC70B34A5E76E7B233F'
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    # create an ABP authentication params
    dev_addr = struct.unpack(">l", ubinascii.unhexlify(address))[0]
    nwk_swkey = ubinascii.unhexlify(networkSessionKey)
    app_swkey = ubinascii.unhexlify(applicationSessionKey)
    # join a network using ABP (Activation By Personalization)
    lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)
    # send some data
    s.send(bytes([0x01, 0x02, 0x03]))
    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)
    # get any data received (if any...)
    data = s.recv(64)
    print(data)

def abp_2():
    """
    Je suis assez sur que ce code a marché. Je crois que c'est pour ttn (en abp obviously)
    """
    pycom.rgbled(0x7f7f00)

    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # create an ABP authentication params
    address = '26011906'
    networkSessionKey = 'A047954C93A7C1D637F6EA7FD0DA1EE0'
    applicationSessionKey = '97E552A4C2F14A35E5E97714B17782DA'

    dev_addr = struct.unpack(">l", ubinascii.unhexlify('26011906'))[0]
    nwk_swkey = ubinascii.unhexlify('A047954C93A7C1D637F6EA7FD0DA1EE0')
    app_swkey = ubinascii.unhexlify('97E552A4C2F14A35E5E97714B17782DA')

    # join a network using ABP (Activation By Personalization)
    lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    # send some data
    s.send(bytes([0x01, 0x02, 0x03]))

    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)

    # get any data received (if any...)
    data = s.recv(64)
    print(data)
    print("done")
    pycom.rgbled(0x007f00) # green
    time.sleep(5)
    pycom.heartbeat(False)


# autre code que je sais plus d'ou il vient
# TTN
# address = '26011F69'
# applicationSessionKey = '3A079E29F7E417AD1B68ED6FD450D748'
# networkSessionKey = 'F81E821FD72A916921B02EE633E3E170'
# address = '26011E54'
# networkSessionKey = 'AA32A75EA66E321EF958F0F22C50B97A'
# applicationSessionKey = '9B428CB611BCA3D84076EEADB4667BDB'

# from platform import Platform
# from connection import Lora
# from m2m_integersensor import IntegerSensor
# from ujson import dumps
# import utime
# import gc
#
# gc.enable()
# gc.collect()
# gc.mem_free()
#
# address = '061010C7'
# applicationSessionKey = '80974D854F4D0328646E02F9823703C4'
# networkSessionKey = 'E397B3E73863FFC70B34A5E76E7B233F'
#

# connection = Lora(address, applicationSessionKey, networkSessionKey)
# lopyDevice = Platform(connection, address)

#
# sensor = IntegerSensor()
# sensor.setValue(55)
# gc.collect()
#
# print("Pushing .......")
# print (dumps(sensor.getAsJson()))
# lopyDevice.pushSensorData(sensor, debug=False)
