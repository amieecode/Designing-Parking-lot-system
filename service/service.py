class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        """
        Initialize a vehicle object with its type, registration number, and color.

        :param vehicle_type: str, type of the vehicle (e.g., 'Car', 'Bike', 'Truck')
        :param registration_number: str, registration number of the vehicle
        :param color: str, color of the vehicle
        """
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

class ParkingSlot:
    def __init__(self, slot_type, floor, slot_number, is_available=True, vehicle=None):
        """
        Initialize a parking slot object with its type, floor number, slot number, availability, and vehicle (if parked).

        :param slot_type: str, type of the parking slot (e.g., 'Truck', 'Bike', 'Car')
        :param floor: int, floor number where the parking slot is located
        :param slot_number: int, slot number of the parking slot
        :param is_available: bool, availability of the parking slot (default: True)
        :param vehicle: Vehicle, vehicle parked in the slot (default: None)
        """
        self.slot_type = slot_type
        self.floor = floor
        self.slot_number = slot_number
        self.is_available = is_available
        self.vehicle = vehicle

class ParkingFloor:
    def __init__(self, floor_number, slots):
        """
        Initialize a parking floor object with its floor number and a list of parking slots.

        :param floor_number: int, floor number
        :param slots: list, list of ParkingSlot objects on the floor
        """
        self.floor_number = floor_number
        self.slots = slots

class ParkingLot:
    def __init__(self, parking_lot_id):
        """
        Initialize a parking lot object with its unique ID and an empty list of parking floors.

        :param parking_lot_id: str, unique ID of the parking lot
        """
        self.parking_lot_id = parking_lot_id
        self.floors = []

    def create_parking_lot(self, no_of_floors, no_of_slots_per_floor):
        """
        Create a parking lot with the specified number of floors and slots per floor.

        :param no_of_floors: int, number of floors in the parking lot
        :param no_of_slots_per_floor: int, number of slots per floor
        :return: str, message indicating the successful creation of the parking lot
        """
        for _ in range(no_of_floors):
            self.add_floor(no_of_slots_per_floor)
        return f"Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor"

    def add_floor(self, no_of_slots):
        """
        Add a floor with the specified number of slots to the parking lot.

        :param no_of_slots: int, number of slots on the floor
        :return: None
        """
        slots = [
            ParkingSlot('Truck', len(self.floors) + 1, i + 1)
            for i in range(no_of_slots)
            if i == 0
        ] + [
            ParkingSlot('Bike', len(self.floors) + 1, i + 1)
            for i in range(no_of_slots)
            if i in (1, 2)
        ] + [
            ParkingSlot('Car', len(self.floors) + 1, i + 1)
            for i in range(no_of_slots)
            if i > 2
        ]
        self.floors.append(ParkingFloor(len(self.floors) + 1, slots))

    def find_available_slot(self, vehicle):
        """
        Find an available parking slot for the given vehicle.

        :param vehicle: Vehicle, vehicle to park
        :return: ParkingSlot, available parking slot for the vehicle or None if no available slot is found
        """
        for floor in self.floors:
            available_slot = next((slot for slot in floor.slots if slot.is_available and slot.slot_type == vehicle.vehicle_type), None)
            if available_slot:
                return available_slot
        return None

    def park_vehicle(self, vehicle):
        """
        Park a vehicle in an available slot.

        :param vehicle: Vehicle, vehicle to park
        :return: str, ticket ID for the parked vehicle or a message indicating the parking lot is full
        """
        available_slot = self.find_available_slot(vehicle)
        if available_slot:
            available_slot.is_available = False
            available_slot.vehicle = vehicle
            ticket_id = f"Parked vehicle. Ticket ID: {self.parking_lot_id}_{available_slot.floor_number}_{available_slot.slot_number}"
            return ticket_id
        else:
            return "Parking Lot Full"

    def unpark_vehicle(self, ticket_id):
        """
        Unpark a vehicle using the given ticket ID.

        :param ticket_id: str, ticket ID for the parked vehicle
        :return: str, message indicating the successful unparking of the vehicle or an error message
        """
        floor_number = int(ticket_id.split('_')[1])
        slot_number = int(ticket_id.split('_')[2])

        for floor in self.floors:
            if floor.floor_number == floor_number:
                for slot in floor.slots:
                    if slot.slot_number == slot_number and not slot.is_available:
                        slot.is_available = True
                        slot.vehicle = None
                        return f"Unparked vehicle with Registration Number: {slot.vehicle.registration_number} and Color: {slot.vehicle.color}"
        return "Invalid Ticket"

    def display_free_count(self, vehicle_type):
        """
        Display the number of free slots for the given vehicle type.

        :param vehicle_type: str, type of the vehicle (e.g., 'Car', 'Bike', 'Truck')
        :return: int, number of free slots for the given vehicle type
        """
        free_slots = sum(1 for floor in self.floors for slot in floor.slots if slot.is_available and slot.slot_type == vehicle_type)
        print(f"No. of free slots for {vehicle_type}: {free_slots}")
        return free_slots

    def display_free_slots(self, vehicle_type):
        """
        Display the slot numbers of free slots for the given vehicle type.

        :param vehicle_type: str, type of the vehicle (e.g., 'Car', 'Bike', 'Truck')
        :return: None
        """
        free_slots = [slot for floor in self.floors for slot in floor.slots if slot.is_available and slot.slot_type == vehicle_type]
        print(f"Free slots for {vehicle_type}: {', '.join(str(slot.slot_number) for slot in free_slots)}")

    def display_occupied_slots(self, vehicle_type):
        """
        Display the slot numbers of occupied slots for the given vehicle type.

        :param vehicle_type: str, type of the vehicle (e.g., 'Car', 'Bike', 'Truck')
        :return: None
        """
        occupied_slots = [slot for floor in self.floors for slot in floor.slots if not slot.is_available and slot.slot_type == vehicle_type]
        for floor_number, floor in enumerate(self.floors, 1):
            print(f"Occupied slots for {vehicle_type} on Floor {floor_number}: {','.join(str(slot.slot_number) for slot in occupied_slots if slot.floor == floor_number)}")

    def __str__(self):
        """
        Return a string representation of the parking lot.

        :return: str, string representation of the parking lot
        """
        return f"Parking Lot ID: {self.parking_lot_id}"
