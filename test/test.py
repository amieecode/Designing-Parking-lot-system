import unittest
from service import ParkingLot
from service.service import Vehicle

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot("PR1234")

    def test_create_parking_lot(self):
        self.parking_lot.create_parking_lot(2, 3)
        self.assertEqual(len(self.parking_lot.floors), 2)
        self.assertEqual(len(self.parking_lot.floors[0]), 3)
        self.assertEqual(len(self.parking_lot.floors[1]), 3)

    def test_park_vehicle(self):
        self.parking_lot.create_parking_lot(2, 3)
        car = Vehicle("car", "KA-01-HB-1234", "Red")
        self.assertEqual(self.parking_lot.park_vehicle(car), "PR1234_1_2")
        bike = Vehicle("bike", "KA-01-HB-5678", "Blue")
        self.assertEqual(self.parking_lot.park_vehicle(bike), "PR1234_1_3")
        truck = Vehicle("truck", "KA-01-HB-9012", "Green")
        self.assertEqual(self.parking_lot.park_vehicle(truck), "PR1234_1_1")
        self.assertEqual(self.parking_lot.park_vehicle(car), "Parking Lot Full")

    def test_unpark_vehicle(self):
        self.parking_lot.create_parking_lot(2, 3)
        car = Vehicle("car", "KA-01-HB-1234", "Red")
        self.parking_lot.park_vehicle(car)
        self.assertEqual(self.parking_lot.unpark_vehicle("PR1234_1_2"), "Unparked vehicle with Registration Number: KA-01-HB-1234 and Color: Red")
        self.assertEqual(self.parking_lot.unpark_vehicle("PR1234_1_1"), "Invalid Ticket")

    def test_display_free_count(self):
        self.parking_lot.create_parking_lot(2, 3)
        self.assertEqual(self.parking_lot.display_free_count(), 6)