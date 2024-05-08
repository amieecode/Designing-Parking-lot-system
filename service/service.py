# Define a class for vehicles with attributes like type, registration number, and color
class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.color = color


# Define a class for parking slots with attributes like type, floor number, slot number, availability, and associated vehicle
class ParkingSlot:
    def __init__(self, slot_type, floor, slot_number):
        self.slot_type = slot_type
        self.floor = floor
        self.slot_number = slot_number
        self.is_available = True
        self.vehicle = None


# Define a class for a parking lot with a unique ID and a list of floors
class ParkingLot:
    def __init__(self, parking_lot_id):
        self.parking_lot_id = parking_lot_id
        self.floors = []

    # Method to create a parking lot with specified number of floors and slots per floor
    def create_parking_lot(self, no_of_floors, no_of_slots_per_floor):
        try:
            for _ in range(no_of_floors):
                self.add_floor(no_of_slots_per_floor)
            return f"Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor"
        except:
            return "Their was an error creating parking lot"

    # Method to add a floor with specified number of slots to the parking lot
    def add_floor(self, no_of_slots):
        try:
            floor = []
            for i in range(no_of_slots):
                if i == 0:
                    slot_type = "Truck"
                elif i in [1, 2]:
                    slot_type = "Bike"
                else:
                    slot_type = "Car"
                slot = ParkingSlot(slot_type, len(self.floors) + 1, i + 1)
                floor.append(slot)
            self.floors.append(floor)
        except:
            return "An error occur while adding floor"

    # Method to find an available slot for a vehicle
    def find_available_slot(self, vehicle):
        try:
            for floor in self.floors:
                for slot in floor:
                    if slot.is_available and slot.slot_type == vehicle.vehicle_type:
                        return slot
            return None
        except:
            return "An error occured while finding slot"

    # Method to park a vehicle in an available slot
    def park_vehicle(self, vehicle):
        try:
            available_slot = self.find_available_slot(vehicle)
            if available_slot:
                available_slot.is_available = False
                available_slot.vehicle = vehicle
                ticket_id = f"Parked vehicle. Ticket ID: {self.parking_lot_id}_{available_slot.floor}_{available_slot.slot_number}"
                return ticket_id
            else:
                return "Parking Lot Full"
        except:
            return "Unable to park vehicle"

    # Method to unpark a vehicle using its ticket ID
    def unpark_vehicle(self, ticket_id):
        try:
            floor_number = int(ticket_id.split("_")[1])
            prev_vehicle_no = None
            prev_vehicle_color = None
            slot_number = int(ticket_id.split("_")[2])
            for floor in self.floors:
                if floor[0].floor == floor_number:
                    for slot in floor:
                        if slot.slot_number == slot_number:
                            if slot.vehicle:
                                prev_vehicle_no = slot.vehicle.registration_number
                                prev_vehicle_color = slot.vehicle.color
                                slot.is_available = True
                                slot.vehicle = None
                                return "Unparked vehicle with Registration Number: {} and Color: {}".format(
                                    prev_vehicle_no, prev_vehicle_color
                                )
            return "Invalid Ticket"
        except:
            return "An error occured while unparking vehicle"

    # Method to display the count of free slots for a specific vehicle type
    def display_free_count(self, vehicle_type):
        try:
            free_slots = []
            for floor in self.floors:
                free_slots += [
                    slot
                    for slot in floor
                    if slot.is_available and slot.slot_type == vehicle_type
                ]
            print(f"No. of free slots for {vehicle_type}: {len(free_slots)}")
            return f"No. of free slots for {vehicle_type}: {len(free_slots)}"
        except:
            return "An error occured while finding free count for {vehicle_type}"

    # Method to display the slot numbers of free slots for a specific vehicle type
    def display_free_slots(self, vehicle_type):
        try:
            free_slots = []
            for floor in self.floors:
                free_slots += [
                    slot
                    for slot in floor
                    if slot.is_available and slot.slot_type == vehicle_type
                ]
            print(
                f"Free slots for {vehicle_type}: {', '.join(str(slot.slot_number) for slot in free_slots)}"
            )
        except:
            return "An error occured while finding free slot for {vehicle_type}"

    # Method to display the slot numbers of occupied slots for a specific vehicle type on each floor
    def display_occupied_slots(self, vehicle_type):
        try:
            for floor in self.floors:
                occupied_slots = []
                for slot in floor:
                    if not slot.is_available and (slot.slot_type == vehicle_type):
                        occupied_slots.append(str(slot.slot_number))
                print(
                    f"Occupied slots for {vehicle_type} on Floor {floor[0].floor}: {','.join(occupied_slots)}"
                )
        except:
            return "An error occured while finding occupied slot for {vehicle_type} on all floors"
