import unittest
from test.test import TestParkingLot

if __name__ == "__main__":
    # Load tests from TestParkingLot class
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParkingLot)

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the tests
    runner.run(suite)
