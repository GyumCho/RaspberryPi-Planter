import glob
import time
from time import sleep
import RPi.GPIO as GPIO
import psycopg2
from datetime import datetime
import threading

#https://stackoverflow.com/questions/12906351/importerror-no-module-named-psycopg2

sleeptime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#The pull-up/downs supply that voltage so that the gpio will have a defined value UNTIL overridden by a stronger force.

base_directory = '/sys/bus/w1/devices/'
global device_file
global conn
global cursor
global plantID 
global device_folder
global temperatureID

    

def base_dir():
    global device_file
    while True:
        try:
            device_folder = glob.glob(base_directory + '28*')[0]
            break
        except IndexError:
            sleep(0.5)
            continue
        finally:
            device_file = device_folder + '/w1_slave'
    return device_file

try:
    dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    device_file = base_dir()
    cursor.execute("SELECT COUNT(DISTINCT temperatureid) FROM raspberry.temperature")
    temperatureID = cursor.fetchone()[0]
    programCounter = 0
    while programCounter <= 10:
        tempfile = open(device_file, "r")
        thetext = tempfile.read()
        tempfile.close()
        tempdata = thetext.split("\n")[1].split(" ")[9]
        temperature = float(tempdata[2:])
        temperature = temperature / 1000
        t = datetime.now()
        time1 = t.strftime("%H:%M:%S")
        cursor.execute("INSERT INTO raspberry.temperature (temperatureid, time, value) VALUES ("+ str(temperatureID)+ " , '" + str(time1) + "' , " + str(temperature) + ")")
        conn.commit()
        print("Inserted data")
        print(temperature)
        sleep(1)
        programCounter += 1

finally:
    print("error")
