import unittest
from typing import NamedTuple, List
import pytest

class Vehicle(NamedTuple):
    vehicle_type: str
    registration_number: str
    color: str

class ParkingLot:
    """
    A class representing a parking lot with multiple floors and slots per floor.
    """
    def __init__(self, parking_lot_id: str):
        self.parking_lot_id = parking_lot_id
        self.floors: List[List[str]] = []

    @property
    def floors(self) -> List[List[str]]:
        """
        A read-only property representing the floors of the parking lot.
        """
        return self.floors

    @classmethod
    def create_parking_lot(cls, num_floors: int, num_slots: int):
        """
        Create a new parking lot with the given number of floors and slots per floor.
        """
        parking_lot = cls("PR1234")
        for _ in range(num_floors):
            floor = []
            for _ in range(num_slots):
                floor.append(None)
            parking_lot.floors.append(floor)
        return parking_lot

    @classmethod
    def park(cls, parking_lot: "ParkingLot", vehicle: Vehicle):
        """
        Park a vehicle in the parking lot and return a ticket ID.
        """
        for floor_idx, floor in enumerate(parking_lot.floors):
            for slot_idx, slot in enumerate(floor):
                if slot is None:
                    parking_lot.floors[floor_idx][slot_idx] = vehicle
                    return f"{parking_lot.parking_lot_id}_{floor_idx + 1}_{slot_idx + 1}"
        raise Exception("Parking Lot Full")

    @classmethod
    def unpark(cls, parking_lot: "ParkingLot", ticket_id: str):
        """
        Unpark a vehicle from the parking lot using the ticket ID.
        """
        for floor_idx, floor in enumerate(parking_lot.floors):
            for slot_idx, slot in enumerate(floor):
                if f"{parking_lot.parking_lot_id}_{floor_idx + 1}_{slot_idx + 1}" == ticket_id:
                    parking_lot.floors[floor_idx][slot_idx] = None
                    return f"Unparked vehicle with Registration Number: {slot.registration_number} and Color: {slot.color}"
        return "Invalid Ticket"

    @staticmethod
    def display_free_count(parking_lot: "ParkingLot", vehicle_type: str):
        """
        Display the number of free slots for a given vehicle type.
        """
        count = 0
        for floor in parking_lot.floors:
            count += floor.count(None)
        return f"No. of free slots for {vehicle_type.capitalize()}: {count}"

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        """
        Initialize a new ParkingLot object with the given parking lot ID.
        """
        self.parking_lot = ParkingLot("PR1234")

    @pytest.mark.unit
    def test_create_parking_lot(self):
        """
        Test the creation of a parking lot with the given number of floors and slots per floor.
        """
        self.parking_lot.create_parking_lot(2, 3)
        self.assertEqual(len(self.parking_lot.floors), 2)
        for floor in self.parking_lot.floors:
            self.assertEqual(len(floor), 3)

    @pytest.mark.unit
    def test_park_vehicle(self):
        """
        Test parking a vehicle in the parking lot.
        """
        self.parking_lot.create_parking_lot(2, 4)
        car = Vehicle("Car", "KA-01-HB-1234", "Red")
        ticket_id = self.parking_lot.park(self.parking_lot, car)
        self.assertIsNotNone(ticket_id)
        self.assertEqual(ticket_id, "PR1234_1_4")

        bike = Vehicle("Bike", "KA-01-HB-5678", "Blue")
        ticket_id = self.parking_lot.park(self.parking_lot, bike)
        self.assertIsNotNone(ticket_id)
        self.assertEqual(ticket_id, "PR1234_1_2")

        truck = Vehicle("Truck", "KA-01-HB-9012", "Green")
        ticket_id = self.parking_lot.park(self.parking_lot, truck)
        self.assertIsNotNone(ticket_id)
        self.assertEqual(ticket_id, "PR1234_1_1")

        with self.assertRaises(Exception) as context:
            self.parking_lot.park(self.parking_lot, car)
        self.assertEqual(context.exception.args[0], "Parking Lot Full")

    @pytest.mark.unit
    def test_unpark_vehicle(self):
        """
        Test unparking a vehicle from the parking lot using the ticket ID.
        """
        self.parking_lot.create_parking_lot(2, 4)
        car = Vehicle("Car", "KA-01-HB-1234", "Red")
        self.parking_lot.park(self.parking_lot, car)
        ticket_id = "PR1234_1_4"

        response = self.parking_lot.unpark(self.parking_lot, ticket_id)
        expected_response = "Unparked vehicle with Registration Number: KA-01-HB-1234 and Color: Red"
        self.assertEqual(response, expected_response)

        response = self.parking_lot.unpark(self.parking_lot, "PR1234_1_1")
        expected_response = "Invalid Ticket"
        self.assertEqual(response, expected_response)

    @pytest.mark.unit
    def test_display_free_count(self):
        """
        Test displaying the number of free slots for a given vehicle type.
        """
        self.parking_lot.create_parking_lot(2, 3)
        response = self.parking_lot.display_free_count(self.parking_lot, "Truck")
        expected_response = "No. of free slots for Truck: 2"
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
