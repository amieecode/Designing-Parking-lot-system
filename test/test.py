import unittest
from service import ParkingLot, Vehicle


class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot("PR1234")

    def test_create_parking_lot(self):
        self.parking_lot.create_parking_lot(2, 3)
        self.assertEqual(len(self.parking_lot.floors), 2)
        for floor in self.parking_lot.floors:
            self.assertEqual(len(floor), 3)

    def test_park_vehicle(self):
        self.parking_lot.create_parking_lot(2, 4)
        car = Vehicle("Car", "KA-01-HB-1234", "Red")
        self.assertEqual(self.parking_lot.park_vehicle(car), "Parked vehicle. Ticket ID: PR1234_1_4")

        bike = Vehicle("Bike", "KA-01-HB-5678", "Blue")
        self.assertEqual(self.parking_lot.park_vehicle(bike), "Parked vehicle. Ticket ID: PR1234_1_2")

        truck = Vehicle("Truck", "KA-01-HB-9012", "Green")
        self.assertEqual(self.parking_lot.park_vehicle(truck), "Parked vehicle. Ticket ID: PR1234_1_1")

        self.assertEqual(self.parking_lot.park_vehicle(car), "Parking Lot Full")

    def test_unpark_vehicle(self):
        self.parking_lot.create_parking_lot(2, 4)
        car = Vehicle("Car", "KA-01-HB-1234", "Red")
        self.parking_lot.park_vehicle(car)

        response = self.parking_lot.unpark_vehicle("PR1234_1_4")
        expected_response = "Unparked vehicle with Registration Number: KA-01-HB-1234 and Color: Red"
        self.assertEqual(response, expected_response)

        response = self.parking_lot.unpark_vehicle("PR1234_1_1")
        expected_response = "Invalid Ticket"
        self.assertEqual(response, expected_response)

    def test_display_free_count(self):
        self.parking_lot.create_parking_lot(2, 3)
        response = self.parking_lot.display_free_count("Truck")
        expected_response = "No. of free slots for Truck: 2"
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
