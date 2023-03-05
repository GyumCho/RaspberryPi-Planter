import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import threading
import psycopg2
from datetime import datetime
import numpy as np

# Create a SPI Bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)  # Create the chip select
ADC = MCP.MCP3008(spi,cs)  # Create an object for the ADC

# Create an analog input channel on pin 0
LDRChan = AnalogIn(ADC,MCP.P0)
#multiple sensors can be connected to the pi on different pins. Currently, v r connected to pin 0. Hence, the moistureID will be  0. 

#TODO: add the moisture sensor ID to the moisture sensor table

global moisture_value
global cursor
global plantID
global moisture_data

try:
    dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    global moisture_ID
    cursor.execute("SELECT COUNT(DISTINCT moistureid) FROM raspberry.moisture")
    moistureID = cursor.fetchone()[0]
    moisture_data = []
    print("Thread working")
    count = 0
    programCounter = 0
    while programCounter <= 10:
        moisture_value = LDRChan.value
        moisture_data.append(moisture_value)
        print("Len: "+ str(len(moisture_data)))
        if(len(moisture_data)!=0):
            for i in moisture_data:
                print(str(i))
        count += 1
        if(count%5==0):
            while True:
                print(len(moisture_data))
                if(len(moisture_data)==5):
                    print("inside the if loop")
                    moisture_datacopy = moisture_data.copy()
                    moisture_data.clear()
                    if(np.std(moisture_datacopy)<=1000): #TODO:check if 1000 is a decent value
                        print("inside the std if loop")
                        t = datetime.now()
                        time1 = t.strftime("%H:%M:%S")
                        cursor.execute("INSERT INTO raspberry.moisture (moistureid, time, value) VALUES ("+ str(moistureID) + ", '" + str(time1) + "'," + str(moisture_datacopy[0]) + ")")
                        conn.commit()
                        print("inserted data")
                    moisture_datacopy.clear()
                    break
        time.sleep(1)
        programCounter += 1

finally:
    print("error")
