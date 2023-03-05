import unittest
import lightSensorDBConn

class lightTest(unittest.TestCase):

    def test_lightID(self):
       self.assertEquals((lightSensorDBConn.plantID, lightSensorDBConn.plantID-1, "Invalid lightID"))

    def test_DBconn(self):
        lightSensorDBConn.database_connection()
        cursor = lightSensorDBConn.cursor
        plantid = cursor.execute("SELECT plantid FROM plants WHERE lightid = 0")
        self.assertEquals(plantid, 1, "Database connection unsuccessful, wrong data" )

    def test_lightValue(self):
        self.assertGreaterEquals(lightID.LDRChan.value, 0, "Wrong data shown")

if __name__ == '__main__':
    unittest.main()
