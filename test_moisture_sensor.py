import busio 
import time 
import digitalio 
import board
import adafruit_mcp3xxx.mcp3008 as MCP 
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO


spi = busio.SPI( clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI ) #

cs = digitalio.DigitalInOut(board.D8)

mpc = MCP.MCP3008(spi, cs)

chan = AnalogIn(mpc, MCP.P0)

print('Reading of MCP 3008 values , Ctrl +C to End ')
while True :
    print('ADC Value :',chan.value)
    time.sleep(5)   
    
