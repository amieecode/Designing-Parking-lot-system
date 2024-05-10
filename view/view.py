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
            lot,err=parking_lot.create_parking_lot(int(command[2]), int(command[3]))
            if not err:
            	print(lot)
            else:
            	print(err)
            
        # Park a vehicle
        elif command[0] == "park_vehicle":
            vehicle = Vehicle(command[1].title(), command[2], command[3])
            ticket_id,err = parking_lot.park_vehicle(vehicle)
            if not err:
            	if ticket_id != "Parking Lot Full":
                	print(ticket_id)
            else:
            	print(err)
        # Unpark a vehicle
        elif command[0] == "unpark_vehicle":
            unpark,err=parking_lot.unpark_vehicle(command[1])
            if not err:
            	print(unpark)
            else:
            	print(err)
        # Display information about free or occupied slots
        elif command[0] == "display":
            if command[1] == "free_count":
                d_free_count,err= parking_lot.display_free_count(command[2].title())
                if not err:
                	print(d_free_count)
                else:
                	print(err)
            elif command[1] == "free_slots":
                d_free_slots,err = parking_lot.display_free_slots(command[2].title())
                if not err:
                	print(d_free_slots)
                else:
                	print(err)
            elif command[1] == "occupied_slots":
                d_occupied_slots,err = parking_lot.display_occupied_slots(command[2].title())
                if not err:
                	print(d_occupied_slots)
                else:
                	print(err)
        # Exit the program
        elif command[0] == "exit":
            sys.exit(0)
        else:
            print("Invalid command")


