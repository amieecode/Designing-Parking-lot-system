import sys
from service import ParkingLot
from service.service import Vehicle

def print_help():
    """Print the list of available commands"""
    print("Available commands:")
    print("  create_parking_lot <rows> <columns>")  # Create a new parking lot with the given dimensions
    print("  park_vehicle <registration_number> <color> <vehicle_type>")  # Park a vehicle in the parking lot
    print("  unpark_vehicle <ticket_id>")  # Unpark a vehicle from the parking lot
    print("  display free_count <parking_lot_id> | free_slots <parking_lot_id> | occupied_slots <parking_lot_id>")  # Display information about parking lots
    print("  status")  # Print the current status of parking lots
    print("  help")  # Print the list of available commands
    print("  exit")  # Exit the program

def print_status():
    """Print the current status of parking lots"""
    print(f"Current status of parking lots:")
    for command in command_history:
        if command[0] == "create_parking_lot":
            print(f"Parking Lot {command[1]} ({command[2]} x {command[3]}):")
            print(f"  Free slots: {parking_lot.get_free_slots(command[1])}")  # Number of free slots in the parking lot
            print(f"  Occupied slots: {parking_lot.get_occupied_slots(command[1])}")  # Number of occupied slots in the parking lot

