import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import psycopg2
from datetime import datetime
import numpy as np
import glob
from time import sleep
from distutils import dist
import RPi.GPIO as GPIO



global moisture_value
global cursor
global plantID
global moisture_data
global LDRChan
global MoistureChan
global waterPinBase1
global waterPinBase2
global waterPinBase3
global trigPin
global echoPin


def moisture():
	
	#multiple sensors can be connected to the pi on different pins. Currently, v r connected to pin 0. Hence, the moistureID will be  0. 

	#TODO: add the moisture sensor ID to the moisture sensor table
	try:
		dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
		conn = psycopg2.connect(dsn)
		cursor = conn.cursor()
		global moisture_ID
		cursor.execute("SELECT plantid FROM raspberry.plants")
		row = cursor.fetchall()
		moisture_list = list(sum(row, ()))
		for i in range(0,len(moisture_list)):
			moistureID = moisture_list[i]
			print("moisture id :" + str(moistureID))
			moisture_data = []
			#print("Thread working")
			count = 0
			programCounter = 0
			while programCounter <= 10:
				if(moistureID%2==0):
				    print("read from sensor 0")
				    moisture_value = MoistureChan.value
				elif (moistureID%2!=0):
				    print("read from sensor 2")
				    moisture_value = MoistureChan2.value
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
            
		
		#combined1.combined.temp()
	finally:
		print("finished moisture")#temp()


def temp():
	print("inside temperature")
	sleeptime = 1

	
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
		#cursor.execute("SELECT COUNT(DISTINCT temperatureid) FROM raspberry.temperature")
		temperatureID = 0
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
		#GPIO.cleanup()
		print("finished temperature")
		#light()

def light():		
	global cursor
	try:
		dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
		conn = psycopg2.connect(dsn)
		cursor = conn.cursor()
		#cursor.execute("SELECT COUNT(DISTINCT sunlightid) FROM raspberry.sunlight")
		lightsensorID = 0
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
		print("finished light")
		#ultrasonic()

# NOTE WHEN BUILDING THE Circuit keep in mind that you should have a voltage divider at the trigger pin
#  to step down the voltage to around 3.3V. 
#  3.3V = 5V*R1/(R1+R2)   where R1 is between echo and the node, and R2 goes from the node to ground
#  I used R1 = 470Ohm,  R2 = 330Ohm, Max volt is ca. 3V
def ultrasonic():
	
	try:
		dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
		conn = psycopg2.connect(dsn)
		cursor = conn.cursor()
		programCounter = 0
		while programCounter <= 10:
			cursor.execute("SELECT COUNT(*) FROM raspberry.ultrasonic")
			noOfElement = cursor.fetchone()[0]
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
			if(noOfElement==0):
				cursor.execute("INSERT INTO raspberry.ultrasonic (ultrasonicid,time,value) VALUES ("+ str(echoPin) + ", '" + str(time1) + "' , " + str(distance) + ")")
			elif(noOfElement > 0):
				cursor.execute("UPDATE raspberry.ultrasonic SET value=" + str(distance) + "WHERE ultrasonicid= "+ str(echoPin)+ ";")
				cursor.execute("UPDATE raspberry.ultrasonic SET time=" + str(time1) + "WHERE ultrasonicid= " + str(echoPin)+ ";")
			print("distance: " + str(distance))
			conn.commit()
			time.sleep(1) #TODO: increase the time
			programCounter += 1
	finally:
		#GPIO.cleanup()
		print("finished ultrasonic")
		#waternow()

def waternow():


	try:
		dsn = "host={} dbname={} user={} password={}".format("bronto.ewi.utwente.nl", "dab_di21222b_353", "dab_di21222b_353", "bIYdPvU3mYQ6X86Q")
		conn = psycopg2.connect(dsn)
		cursor = conn.cursor()
		global plants_waternow
		global plants_id
		programCounter = 1

		while programCounter <= 10:    
			time.sleep(1)    
			programCounter += 1
			cursor.execute("SELECT plantid FROM raspberry.plants")
			row = cursor.fetchall()
			plant_list = list(sum(row, ()))

			for i in range(0,len(plant_list)):
				plant_id = plant_list[i]
				print("TEST" + str(plant_id))
				print("this is plant id" + str(plant_id))
				cursor.execute("SELECT plantname FROM raspberry.plants WHERE plantid=" + str(plant_id) + ";")
				plant_name = cursor.fetchone()[0]
				print("this is " + str(plant_name) + " ")

				if(plant_id%2 == 0):
					print("first if")
					cursor.execute("SELECT waternow FROM raspberry.plants WHERE plantid=" + str(plant_id) + ";")
					plants_waternow = cursor.fetchone()[0]
					print(plants_waternow)
					if(plants_waternow == 1):
						print("watering plant_id 0")
						GPIO.output(waterPinBase1, 1)
						time.sleep(100)
						GPIO.output(waterPinBase1, 0)

						time.sleep(3)
						GPIO.output(waterPinBase2, 1)
						time.sleep(300)
						GPIO.output(waterPinBase2, 0)

						cursor.execute("UPDATE raspberry.plants SET waternow=0 WHERE plantid=" + str(plant_id) + ";")
						conn.commit()

				if(plant_id%2 == 1):
					print("second if")
					cursor.execute("SELECT waternow FROM raspberry.plants WHERE plantid=" + str(plant_id) + ";")
					plants_waternow = cursor.fetchone()[0]
					print(plants_waternow)
					if(plants_waternow == 1):
						print("watering plant_id 1")
						GPIO.output(waterPinBase1, 1)
						time.sleep(100)
						GPIO.output(waterPinBase1, 0)

						time.sleep(3)
						GPIO.output(waterPinBase3, 1)
						time.sleep(300)
						GPIO.output(waterPinBase3, 0)

						cursor.execute("UPDATE raspberry.plants SET waternow=0 WHERE plantid=" + str(plant_id) + ";")
						conn.commit()

	finally:
		#GPIO.cleanup()
		print("finished watering")
		#main()

try:
    global MoistureChan
    global LDRChan
    global waterPinBase1
    global waterPinBase2
    global waterPinBase3
    global trigPin
    global echoPin


    # Create a SPI Bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    cs = digitalio.DigitalInOut(board.CE0)  # Create the chip select
    ADC = MCP.MCP3008(spi,cs)  # Create an object for the ADC

    # Create an analog input channel on pin 0
    MoistureChan = AnalogIn(ADC,MCP.P1)
    MoistureChan2 = AnalogIn(ADC,MCP.P2) #TODO:GET the right pint
    # Create an analog input channel on pin 1
    LDRChan = AnalogIn(ADC,MCP.P0)

    waterPinBase1 =16
    waterPinBase2 = 20
    waterPinBase3 = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(waterPinBase1, GPIO.OUT)
    GPIO.setup(waterPinBase2, GPIO.OUT)
    GPIO.setup(waterPinBase3, GPIO.OUT)

    # Set the GPIO Mode
    trigPin = 18   # Note this is a GPIO pin numbering not normal pin numbering
    echoPin = 23   # GPIO24 = pin 16
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        moisture()
        temp()
        light()
        ultrasonic()
        waternow()
finally:
    GPIO.cleanup()
    print("end of program")


