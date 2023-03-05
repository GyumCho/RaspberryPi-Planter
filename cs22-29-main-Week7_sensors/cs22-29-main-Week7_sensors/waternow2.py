import time
import RPi.GPIO as GPIO
import psycopg2

global cursor
global plant_id

waterPinBase1 = 13
waterPinBase2 = 15
waterPinBase3 = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(waterPinBase1, GPIO.OUT)
GPIO.setup(waterPinBase2, GPIO.OUT)
GPIO.setup(waterPinBase3, GPIO.OUT)

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
                cursor.execute("SELECT waternow FROM raspberry.plants WHERE plantid=0;")
                plants_waternow = cursor.fetchone()[0]
                print(plants_waternow)
                if(plants_waternow == 1):
                    print("watering plant_id 0")
                    GPIO.output(waterPinBase1, 1)
                    time.sleep(5)
                    GPIO.output(waterPinBase1, 0)

                    time.sleep(3)
                    GPIO.output(waterPinBase2, 1)
                    time.sleep(5)
                    GPIO.output(waterPinBase2, 0)

                    cursor.execute("UPDATE raspberry.plants SET waternow=0 WHERE plantid=0;")
                    conn.commit()

            if(plant_id%2 == 1):
                print("second if")
                cursor.execute("SELECT waternow FROM raspberry.plants WHERE plantid=1;")
                plants_waternow = cursor.fetchone()[0]
                print(plants_waternow)
                if(plants_waternow == 1):
                    print("watering plant_id 1")
                    GPIO.output(waterPinBase1, 1)
                    time.sleep(5)
                    GPIO.output(waterPinBase1, 0)

                    time.sleep(3)
                    GPIO.output(waterPinBase3, 1)
                    time.sleep(5)
                    GPIO.output(waterPinBase3, 0)

                    cursor.execute("UPDATE raspberry.plants SET waternow=0 WHERE plantid=1;")
                    conn.commit()

finally:
    GPIO.cleanup()
    print("error")
    
