
from network import WLAN
from network import LoRa
import socket
import time
import binascii
import machine
import struct
import ubinascii
import pycom
from cayenneLPP.CayenneLPP import CayenneLPP


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

def abp(address = '00124f11',
        networkSessionKey = '844a432a89b1b23598e4d24d631a9248',
        applicationSessionKey = '3f1807cd4c7817144147a48b4ec93648',
        value=True):

    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # This is to make sure it work with nano gw
    LORA_FREQUENCY = 868100000 # sigle channel used on nano gw
    lora.add_channel(0, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)
    lora.add_channel(1, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)
    lora.add_channel(2, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)


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
    lpp = CayenneLPP(size = 100, sock = s)
    lpp.add_digital_input(value, channel = 66)

    # sending the packet via the socket
    lpp.send()



    # s.send(bytes([0x01, 0x02, 0x03]))

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
