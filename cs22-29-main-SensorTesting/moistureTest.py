import unittest
import moistureDBConn

class moistureTest(unittest.TestCase):

    def test_moistureID(self):
        self.assertEquals((moistureDBConn.plantID, moistureDBConn.plantID-1, "Invalid moistureID"))

    def test_DBconn(self):
        moistureDBConn.database_connection()
        cursor = moistureDBConn.cursor
        plantid = cursor.execute("SELECT plantid FROM plants WHERE moistureid = 0")
        cursor.commit
        self.assertEquals(plantid, 1, "Database connection unsuccessful, wrong data" )

    def test_moistureDRY(self):
        if(moistureDBConn.moisture_value<800){
            a = "DRY"
        }
        self.assertEquals(a , "DRY", "Correct moisture value not detected")

    def test_moistureDRY(self):
        if(moistureDBConn.moisture_value>800){
            a = "WET"
        }
        self.assertEquals(a , "WET", "Correct moisture value not detected")

if __name__ == '__main__':
    unittest.main()