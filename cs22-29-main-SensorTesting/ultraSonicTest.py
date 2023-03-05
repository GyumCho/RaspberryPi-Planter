import unittest
import UltraSonicDBConn

class ultraSonicTest(unittest.TestCase):
    def test_DBconn(self):
        UltraSonicDBConn.database_connection()
        cursor = UltraSonicDBConn.cursor
        ultrasonicid = cursor.execute("SELECT ultrasonicid FROM ultrasonic")
        self.assertEquals(ultrasonicid, 1, "Database connection unsuccessful, wrong data" )

    def test_ultrasonic(self): #TODO:make this test better
        self.assertGreaterEquals(UltraSonicDBConn.distance, 0, "Wrong data shown")  #TODO: distance is not global
