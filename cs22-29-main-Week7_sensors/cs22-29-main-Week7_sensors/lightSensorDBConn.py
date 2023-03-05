import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import psycopg2
from datetime import datetime

# Create a SPI Bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)  # Create the chip select
ADC = MCP.MCP3008(spi,cs)  # Create an object for the ADC

# Create an analog input channel on pin 0
LDRChan = AnalogIn(ADC,MCP.P1)
#LDRPin = 0
global LDRPin
global cursor

try:
    dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT sunlightid) FROM raspberry.sunlight")
    lightsensorID = cursor.fetchone()[0]
    programCounter = 1
    while programCounter <= 10:
        # Read LRD data
        LDR_value = LDRChan.value
        print(LDR_value)
        t = datetime.now()
        time1 = t.strftime("%H:%M:%S")
        cursor.execute("INSERT INTO raspberry.sunlight (sunlightid, time, value) VALUES (" + str(lightsensorID) + ", '" + str(time1) + "' , " + str(LDR_value) + ")")
        conn.commit()
        print("inserted data")
        time.sleep(1)
        programCounter += 1
finally:
    print("error")
