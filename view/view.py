import sys
from service import ParkingLot
from service.service import Vehicle

def main():
    parking_lot = None
    command_history = []

    def print_help():
        print("Available commands:")
        print("  create_parking_lot <rows> <columns>")
        print("  park_vehicle <registration_number> <color> <vehicle_type>")
        print("  unpark_vehicle <ticket_id>")
        print("  display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")
        print("  exit")

    def print_status():
        print(f"Current status of parking lots:")
        for command in command_history:
            if command[0] == "create_parking_lot":
                print(f"Parking Lot {command[1]} ({command[2]} x {command[3]}):")
                print(f"  Free slots: {parking_lot.get_free_slots(command[1])}")
                print(f"  Occupied slots: {parking_lot.get_occupied_slots(command[1])}")

    while True:
        command = input("What would you like to do? ").split()
        if len(command) == 0:
            continue
        command_history.append(command)
        if command[0] == "help":
            print_help()
        elif command[0] == "status":
            print_status()
        elif command[0] == "create_parking_lot":
            if len(command) != 4:
                print("Invalid command. Use: create_parking_lot <rows> <columns>")
                continue
            try:
                rows = int(command[1])
                columns = int(command[2])
                parking_lot = ParkingLot(command[1], command[2])
                print(parking_lot.create_parking_lot(rows, columns))
            except ValueError:
                print("Invalid input. Use: create_parking_lot <rows> <columns>")
        elif command[0] == "park_vehicle":
            if len(command) != 4:
                print("Invalid command. Use: park_vehicle <registration_number> <color> <vehicle_type>")
                continue
            try:
                vehicle = Vehicle(command[1], command[2], command[3])
                ticket_id = parking_lot.park_vehicle(vehicle)
                if ticket_id != "Parking Lot Full":
                    print(ticket_id)
                else:
                    print("Parking Lot Full")
            except ValueError:
                print("Invalid input. Use: park_vehicle <registration_number> <color> <vehicle_type>")
        elif command[0] == "unpark_vehicle":
            if len(command) != 2:
                print("Invalid command. Use: unpark_vehicle <ticket_id>")
                continue
            print(parking_lot.unpark_vehicle(command[1]))
        elif command[0] == "display":
            if len(command) != 3:
                print("Invalid command. Use: display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")
                continue
            if command[1] == "free_count":
                print(parking_lot.display_free_count(command[2]))
            elif command[1] == "free_slots":
                print(parking_lot.display_free_slots(command[2]))
            elif command[1] == "occupied_slots":
                print(parking_lot.display_occupied_slots(command[2]))
            else:
                print("Invalid command. Use: display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")
        elif command[0] == "exit":
            sys.exit(0)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
