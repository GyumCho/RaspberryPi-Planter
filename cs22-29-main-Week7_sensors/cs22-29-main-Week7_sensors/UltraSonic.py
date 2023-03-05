from distutils import dist
import busio
import digitalio
import board
import time
import RPi.GPIO as GPIO
import psycopg2
from datetime import datetime

# NOTE WHEN BUILDING THE Circuit keep in mind that you should have a voltage divider at the trigger pin
#  to step down the voltage to around 3.3V. 
#  3.3V = 5V*R1/(R1+R2)   where R1 is between echo and the node, and R2 goes from the node to ground
#  I used R1 = 470Ohm,  R2 = 330Ohm, Max volt is ca. 3V


# Set the GPIO Mode
GPIO.setmode(GPIO.BCM)
trigPin = 18   # Note this is a GPIO pin numbering not normal pin numbering
echoPin = 24   # GPIO24 = pin 18
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
    conn = psycopg2.connect(dsn)
    cursor = conn.cursor()
    programCounter = 0
    while programCounter <= 10: 
        # Send trigger
        GPIO.output(trigPin, True) #TODO: what is this for?
        time.sleep(0.00001)
        GPIO.output(trigPin, False)

        # See how long it takes before it recieves output
        startTime = time.time()
        endTime = time.time()
        print(GPIO.input(echoPin))
        while GPIO.input(echoPin) == 0:
            startTime = time.time()
        print("Start Time")

        # save time of arrival
        while GPIO.input(echoPin) == 1:
            endTime = time.time()
        print("End time")
        # time difference between start and arrival
        elapsedTime = endTime - startTime
         t = datetime.now()
        time1 = t.strftime("%H:%M:%S")
        # Change to distance (Speed of sound = 34300 cm/s)
        distance = ((elapsedTime * 34300) / 2); #TODO: figure out how big the storage is and when to alert the user that there is not enough water.
        cursor.execute("INSERT INTO raspberry.ultrasonic (ultrasonicid, time, value) VALUES (" + str(echoPin) + ", '" + str(time) + "' , " + str(distance) + ")")
        conn.commit()
        time.sleep(1) #TODO: increase the time
        programCounter += 1
finally:
    print("Error")

    
