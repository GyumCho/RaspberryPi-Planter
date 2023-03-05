import unittest
import temperatureDBConn

class temperatureTest(unittest.TestCase):

    def test_temperatureID(self):
        #temperatureID = plantID + 3
        self.assertEquals((temperatureDBConn.plantID, temperatureDBConn.plantID+3, "Invalid temperatureID"))

    def test_DBconn(self):
        temperatureDBConn.database_connection()
        cursor = temperatureDBConn.cursor
        plantid = cursor.execute("SELECT plantid FROM plants WHERE temperatureid = 4")
        self.assertEquals(plantid, 1, "Database connection unsuccessful, wrong data" )

    def test_temperature(self):
        self.assertGreaterEquals(temperatureDBConn.temperature, 0, "Wrong data shown")
