import sys
from service import ParkingLot
from service.service import Vehicle

def main():
    parking_lot = ParkingLot("PR1234")
    while True:
        command = input().split()
        if len(command) == 0:
            break
        if command[0] == "create_parking_lot":
            parking_lot.create_parking_lot(int(command[1]), int(command[2]))
        elif command[0] == "park_vehicle":
            vehicle = Vehicle(command[1], command[2], command[3])
            ticket_id = parking_lot.park_vehicle(vehicle)
            if ticket_id != "Parking Lot Full":
                print(ticket_id)
        elif command[0] == "unpark_vehicle":
            print(parking_lot.unpark_vehicle(command[1]))
        elif command[0] == "display":
            if command[1] == "free_count":
                parking_lot.display_free_count(command[2])
            elif command[1] == "free_slots":
                parking_lot.display_free_slots(command[2])
            elif command[1] == "occupied_slots":
                parking_lot.display_occupied_slots(command[2])
        elif command[0] == "exit":
            sys.exit(0)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()