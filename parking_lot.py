class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        """
        Initialize a new instance of the Vehicle class.

        :param vehicle_type: A string representing the type of vehicle (e.g. "car", "truck", "motorcycle")
        :param registration_number: A string representing the registration number of the vehicle
        :param color: A string representing the color of the vehicle
        """
        self.vehicle_type = vehicle_type  #: The type of vehicle
        self.registration_number = registration_number  #: The registration number of the vehicle
        self.color = color  #: The color of the vehicle
