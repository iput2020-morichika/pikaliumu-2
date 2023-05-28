import time
import datetime
import requests
import math
import os
import RPi.GPIO as GPIO
from requests.models import to_key_val_list
import spidev

OFFSET = 0.00
ArrayLenth = 40
pH_array = [0] * ArrayLenth
pH_array_index = 0

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

Vref = 5  # need to check the actual voltage with a tester
spi = spidev.SpiDev()
spi.open(0, 0)  # bus0,cs0
spi.max_speed_hz = 100000  # 100kHz very important!!!
mcp3208_0 = 0
volt = 0


def readMCP3008(channel): #MCP3008用
    adc = spi.xfer2([1, (8 + channel) << 4, 200])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def readMCP3208(channel): #MCP3208用
    ch_b2 = ((channel & 4) >> 2) & 1
    ch_b1 = ((channel & 2) >> 1) & 1
    ch_b0 = channel & 1
    
    cmd1 = 0b000_00110 | ch_b2
    cmd2 = ((ch_b1 << 1) | ch_b0) << 6
    cmd3 = 0

    adc = spi.xfer2([cmd1, cmd2, cmd3])
    data = ((adc[1] & 0b0000_1111) << 8) + adc[2]
    return data

def convert_to_pH(voltage):
    # 電圧からpHに変換する式を適用
    # 実際のpH計測には正確な変換式が必要です
    ph_value = (voltage * (14 / 3.3)) - 0.4
    return ph_value
  
def pH_concent():
  while True:
    mcp3208_0 = readMCP3208(channel=0)
    volt = (mcp3208_0 * Vref) / float(4096)
    pH = convert_to_pH(volt)
    time.sleep(1)
    return pH

if __name__=="__main__":
  while True:
    pH = pH_concent()
    print("pH value: {:.2f}".format(pH))
