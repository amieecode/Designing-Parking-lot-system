class Vehicle:
    def __init__(self, vehicle_type, registration_number, color):
        """
        Initialize a new instance of the Vehicle class.

        :param str vehicle_type: The type of vehicle (e.g. "car", "truck", "motorcycle")
        :param str registration_number: The registration number of the vehicle
        :param str color: The color of the vehicle
        """
        self.vehicle_type = vehicle_type  #: The type of vehicle
        self.registration_number = registration_number  #: The registration number of the vehicle
        self.color = color  #: The color of the vehicle

        # Perform some basic validation on the input
        if not isinstance(vehicle_type, str) or not isinstance(registration_number, str) or not isinstance(color, str):
            raise TypeError("All arguments must be strings.")
        if not registration_number or not registration_number.isalnum():
            raise ValueError("Invalid registration number.")

        # Initialize other attributes
        self._speed = 0  #: The current speed of the vehicle (in mph)

    @property
    def speed(self):
        """
        The current speed of the vehicle (in mph).

        :getter: Returns the current speed.
        :setter: Sets the new speed.
        :type: float
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Speed must be a number.")
        if value < 0:
            raise ValueError("Speed cannot be negative.")
        self._speed = value

