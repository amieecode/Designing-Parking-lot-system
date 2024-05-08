import sys
from service.service import ParkingLot,Vehicle



# Define the main function to interact with the parking lot system
def main():
    parking_lot = None
    while True:
        # Take user input for command
        command = input("What would you like to do?  ").split()
        if len(command) == 0:
            break
        # Create a new parking lot
        if command[0] == "create_parking_lot":
            parking_lot = ParkingLot(command[1])
            print(parking_lot.create_parking_lot(int(command[2]), int(command[3])))
        # Park a vehicle
        elif command[0] == "park_vehicle":
            vehicle = Vehicle(command[1].title(), command[2], command[3])
            ticket_id = parking_lot.park_vehicle(vehicle)
            if ticket_id != "Parking Lot Full":
                print(ticket_id)
        # Unpark a vehicle
        elif command[0] == "unpark_vehicle":
            print(parking_lot.unpark_vehicle(command[1]))
        # Display information about free or occupied slots
        elif command[0] == "display":
            if command[1] == "free_count":
                parking_lot.display_free_count(command[2].title())
            elif command[1] == "free_slots":
                parking_lot.display_free_slots(command[2].title())
            elif command[1] == "occupied_slots":
                parking_lot.display_occupied_slots(command[2].title())
        # Exit the program
        elif command[0] == "exit":
            sys.exit(0)
        else:
            print("Invalid command")
