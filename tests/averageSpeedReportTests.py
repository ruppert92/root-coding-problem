import unittest
from averageSpeedReport import DriverData, GetDriverData

class TestDriverData(unittest.TestCase):
    def test_avgSpeed_zero(self):
        "Test avgSpeed is zero if duration is 0"
        driver = DriverData("Test", 100, 0)
        self.assertEqual(driver.avgSpeed, 0)

    def test_slow_trip_not_added(self):
        "Test that trips under 5mph not added"
        driver = DriverData("Test", 0, 0)
        driver.AddTripToDriver("7:00", "8:00", 4.99)
        self.assertEqual(driver.totalDuration, 0)
        self.assertEqual(driver.totalDistance, 0)

    def test_fast_trip_not_added(self):
        "Test that trips over 100mph not added"
        driver = DriverData("Test", 0, 0)
        driver.AddTripToDriver("7:00", "8:00", 100.01)
        self.assertEqual(driver.totalDuration, 0)
        self.assertEqual(driver.totalDistance, 0)

    def test_trips_are_added(self):
        "Test that trips are added"
        driver = DriverData("Test", 0, 0)
        driver.AddTripToDriver("7:00", "8:00", 100)
        self.assertEqual(driver.totalDuration, 1)
        self.assertEqual(driver.totalDistance, 100)
        driver.AddTripToDriver("7:00", "8:00", 5)
        self.assertEqual(driver.totalDuration, 2)
        self.assertEqual(driver.totalDistance, 105)

    def test_avgSpeed_calculated(self):
        "Test that avgSpeed is calculated"
        driver = DriverData("Test", 100, 1)
        self.assertEqual(driver.avgSpeed, 100)
        driver.AddTripToDriver("10:00", "11:00", 50)
        self.assertEqual(driver.avgSpeed, 75)


class TestImportingDriverData(unittest.TestCase):
    def test_simple_input(self):
        "Test that simple input generates expected output"
        driverDataList = GetDriverData("tests/simpleInput.txt")
        self.assertEqual(len(driverDataList), 3)
        self.assertEqual(driverDataList[0].name, "Lauren")
        self.assertEqual(driverDataList[2].name, "Kumi")

    def test_long_input(self):
        "Test that more complicated input generates expected output"
        driverDataList = GetDriverData("tests/longInput.txt")
        self.assertEqual(len(driverDataList), 5)
        self.assertEqual(driverDataList[0].name, "Kumi")
        self.assertEqual(driverDataList[1].name, "Dan")
        self.assertEqual(driverDataList[2].name, "Lauren")
        self.assertEqual(driverDataList[3].name, "Bob")
        self.assertEqual(driverDataList[4].name, "Billy")
        self.assertEqual(driverDataList[4].totalDistance, 0)


if __name__ == '__main__':
    unittest.main()
