class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

class ParkingSlot:
    def __init__(self, slot_type, floor, slot_number, is_available=True, vehicle=None):
        self.slot_type = slot_type
        self.floor = floor
        self.slot_number = slot_number
        self.is_available = is_available
        self.vehicle = vehicle

class ParkingFloor:
    def __init__(self, floor_number, slots):
        self.floor_number = floor_number
        self.slots = slots

class ParkingLot:
    def __init__(self, parking_lot_id):
        self.parking_lot_id = parking_lot_id
        self.floors = []

    def create_parking_lot(self, no_of_floors, no_of_slots_per_floor):
        for _ in range(no_of_floors):
            self.add_floor(no_of_slots_per_floor)
        return f"Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor"

    def add_floor(self, no_of_slots):
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
        for floor in self.floors:
            for slot in floor.slots:
                if slot.is_available and slot.slot_type == vehicle.vehicle_type:
                    return slot
        return None

    def park_vehicle(self, vehicle):
        available_slot = self.find_available_slot(vehicle)
        if available_slot:
            available_slot.is_available = False
            available_slot.vehicle = vehicle
            ticket_id = f"Parked vehicle. Ticket ID: {self.parking_lot_id}_{available_slot.floor_number}_{available_slot.slot_number}"
            return ticket_id
        else:
            return "Parking Lot Full"

    def unpark_vehicle(self, ticket_id):
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
        free_slots = sum(1 for floor in self.floors for slot in floor.slots if slot.is_available and slot.slot_type == vehicle_type)
        print(f"No. of free slots for {vehicle_type}: {free_slots}")
        return free_slots

    def display_free_slots(self, vehicle_type):
        free_slots = [slot for floor in self.floors for slot in floor.slots if slot.is_available and slot.slot_type == vehicle_type]
        print(f"Free slots for {vehicle_type}: {', '.join(str(slot.slot_number) for slot in free_slots)}")

    def display_occupied_slots(self, vehicle_type):
        occupied_slots = [slot for floor in self.floors for slot in floor.slots if not slot.is_available and slot.slot_type == vehicle_type]
        for floor_number, floor in enumerate(self.floors, 1):
            print(f"Occupied slots for {vehicle_type} on Floor {floor_number}: {','.join(str(slot.slot_number) for slot in occupied_slots if slot.floor == floor_number)}")
