class Vehicle:
    def __init__(self, vehicle_type, registration_number, color, speed=0):
        """
        Initialize a new instance of the Vehicle class.

        :param str vehicle_type: The type of vehicle (e.g. "car", "truck", "motorcycle")
        :param str registration_number: The registration number of the vehicle
        :param str color: The color of the vehicle
        :param float speed: The initial speed of the vehicle (in mph)
        """
        self.vehicle_type = vehicle_type  #: The type of vehicle
        self.registration_number = registration_number  #: The registration number of the vehicle
        self.color = color  #: The color of the vehicle
        self._speed = speed  #: The current speed of the vehicle (in mph)

        # Perform basic validation on the input
        self._validate_input()

    def _validate_input(self):
        """Validate the input parameters."""
        if not isinstance(self.vehicle_type, str) or not isinstance(self.registration_number, str) or not isinstance(self.color, str):
            raise TypeError("All arguments must be strings.")
        if not self.registration_number or not self.registration_number.isalnum():
            raise ValueError("Invalid registration number.")
        if not isinstance(self._speed, (int, float)):
            raise TypeError("Speed must be a number.")
        if self._speed < 0:
            raise ValueError("Speed cannot be negative.")

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
        self._validate_input()
        if value < 0:
            raise ValueError("Speed cannot be negative.")
        self._speed = value

    def accelerate(self, amount):
        """
        Accelerate the vehicle by a given amount (in mph).

        :param float amount: The amount to accelerate by.
        """
        self.speed += amount

    def brake(self, amount):
        """
        Brake the vehicle by a given amount (in mph).

        :param float amount: The amount to brake by.
        """
        self.speed = max(0, self.speed - amount)

