import sys
from service import ParkingLot
from service.service import Vehicle

def print_help():
    """Print the list of available commands"""
    print("Available commands:")
    print("  create_parking_lot <rows> <columns>")
    print("  park_vehicle <registration_number> <color> <vehicle_type>")
    print("  unpark_vehicle <ticket_id>")
    print("  display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")
    print("  status")
    print("  help")
    print("  exit")

def print_status():
    """Print the current status of parking lots"""
    print(f"Current status of parking lots:")
    for command in command_history:
        if command[0] == "create_parking_lot":
            print(f"Parking Lot {command[1]} ({command[2]} x {command[3]}):")
            print(f"  Free slots: {parking_lot.get_free_slots(command[1])}")
            print(f"  Occupied slots: {parking_lot.get_occupied_slots(command[1])}")

def main():
    # Initialize parking_lot and command_history variables
    parking_lots = {}
    command_history = []

    while True:
        # Get user input and split it into a command list
        command = input("What would you like to do? ").split()
        if len(command) == 0:
            # Skip empty commands
            continue
        command_history.append(command)

        if command[0] == "help":
            # Print the list of available commands
            print_help()
        elif command[0] == "status":
            # Print the current status of parking lots
            print_status()
        elif command[0] == "create_parking_lot":
            # Create a new parking lot
            if len(command) != 4:
                print("Invalid command. Use: create_parking_lot <rows> <columns>")
                continue
            try:
                rows = int(command[1])
                columns = int(command[2])
                parking_lot = ParkingLot(command[1], command[2])
                parking_lots[command[1]] = parking_lot
                # Print the result of creating a parking lot
                print(parking_lot.create_parking_lot(rows, columns))
            except ValueError:
                print("Invalid input. Use: create_parking_lot <rows> <columns>")
        elif command[0] == "park_vehicle":
            # Park a vehicle in the parking lot
            if len(command) != 4:
                print("Invalid command. Use: park_vehicle <registration_number> <color> <vehicle_type>")
                continue
            try:
                parking_lot_id = command[1]
                if parking_lot_id not in parking_lots:
                    print(f"No parking lot found with ID {parking_lot_id}")
                    continue
                parking_lot = parking_lots[parking_lot_id]
                vehicle = Vehicle(command[2], command[3], command[4])
                ticket_id = parking_lot.park_vehicle(vehicle)
                if ticket_id != "Parking Lot Full":
                    # Print the ticket ID if the vehicle is parked successfully
                    print(ticket_id)
                else:
                    print("Parking Lot Full")
            except ValueError:
                print("Invalid input. Use: park_vehicle <registration_number> <color> <vehicle_type>")
        elif command[0] == "unpark_vehicle":
            # Unpark a vehicle from the parking lot
            if len(command) != 2:
                print("Invalid command. Use: unpark_vehicle <ticket_id>")
                continue
            # Print the result of unparking a vehicle
            for parking_lot_id, parking_lot in parking_lots.items():
                print(parking_lot.unpark_vehicle(command[1]))
        elif command[0] == "display":
            # Display information about parking lots
            if len(command) != 3:
                print("Invalid command. Use: display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")
                continue
            parking_lot = parking_lots.get(command[2])
            if parking_lot is None:
                print(f"No parking lot found with ID {command[2]}")
                continue
            if command[1] == "free_count":
                # Display the number of free slots in a parking lot
                print(parking_lot.display_free_count(command[2]))
            elif command[1] == "free_slots":
                # Display the free slots in a parking lot
                print(parking_lot.display_free_slots(command[2]))
            elif command[1] == "occupied_slots":
                # Display the occupied slots in a parking lot
                print(parking_lot.display_occupied_slots(command[2]))
            else:
                print("Invalid command. Use: display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")
        elif command[0] == "exit":
            # Exit the program
            sys.exit(0)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

