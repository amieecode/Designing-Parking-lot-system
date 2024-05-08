class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color

class ParkingSlot:
    def __init__(self, slot_type, floor, slot_number):
        self.slot_type = slot_type
        self.floor = floor
        self.slot_number = slot_number
        self.is_available = True
        self.vehicle = None

class ParkingLot:
    def __init__(self, parking_lot_id):
        self.parking_lot_id = parking_lot_id
        self.floors = []

    def create_parking_lot(self, no_of_floors, no_of_slots_per_floor):
        for _ in range(no_of_floors):
            self.add_floor(no_of_slots_per_floor)

    def add_floor(self, no_of_slots):
        floor = []
        for i in range(no_of_slots):
            if i == 0:
                slot_type = 'truck'
            elif i == 1:
                slot_type = 'bike'
            else:
                slot_type = 'car'
            slot = ParkingSlot(slot_type, len(self.floors) + 1, i + 1)
            floor.append(slot)
        self.floors.append(floor)

    def find_available_slot(self, vehicle):
        for floor in self.floors:
            for slot in floor:
                if slot.is_available and slot.slot_type == vehicle.vehicle_type:
                    return slot
        return None

    def park_vehicle(self, vehicle):
        available_slot = self.find_available_slot(vehicle)
        if available_slot:
            available_slot.is_available = False
            available_slot.vehicle = vehicle
            ticket_id = f"{self.parking_lot_id}_{available_slot.floor}_{available_slot.slot_number}"
            return ticket_id
        else:
            return "Parking Lot Full"

    def unpark_vehicle(self, ticket_id):
        floor_number = int(ticket_id.split('_')[1])
        slot_number = int(ticket_id.split('_')[2])
        for floor in self.floors:
            if floor[0].floor == floor_number:
                for slot in floor:
                    if slot.slot_number == slot_number:
                        slot.is_available = True
                        slot.vehicle = None
                        return "Unparked vehicle with Registration Number: {} and Color: {}".format(slot.vehicle.registration_number, slot.vehicle.color)
        return "Invalid Ticket"

    def display_free_count(self, vehicle_type):
        free_slots = []
        for floor in self.floors:
            free_slots += [slot for slot in floor if slot.is_available and slot.slot_type == vehicle_type]
        print(f"No. of free slots for {vehicle_type}: {len(free_slots)}")

    def display_free_slots(self, vehicle_type):
        free_slots = []
        for floor in self.floors:
            free_slots += [slot for slot in floor if slot.is_available and slot.slot_type == vehicle_type]
        print(f"Free slots for {vehicle_type}: {', '.join(str(slot.slot_number) for slot in free_slots)}")

    def display_occupied_slots(self, vehicle_type):
        occupied_slots = []
        for floor in self.floors:
            occupied_slots += [slot for slot in floor if not slot.is_available and slot.slot_type == vehicle_type]
        print(f"Occupied slots for {vehicle_type}: {', '.join(str(slot.slot_number) for slot in occupied_slots)}")