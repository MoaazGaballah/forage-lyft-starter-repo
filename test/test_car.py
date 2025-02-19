import unittest
from datetime import datetime
import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from car_factory import CarFactory





class TestCalliope(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertTrue(car.battery.needs_service())



    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        today = datetime.today().date()
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        today = datetime.today().date()
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_calliope(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertFalse(car.engine.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car =CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        today = datetime.today().date()
        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_glissade(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertFalse(car.engine.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on,tires_list)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on,tires_list)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        today = datetime.today().date()
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on,tires_list)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        today = datetime.today().date()
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on,tires_list)
        self.assertFalse(car.engine.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tires_list)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tires_list)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        today = datetime.today().date()
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tires_list)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        today = datetime.today().date()
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage, tires_list)
        self.assertFalse(car.engine.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertFalse(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        today = datetime.today().date()
        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tires_list=[0.5,0.3,0.1,0.2]
        today = datetime.today().date()
        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage,tires_list)
        self.assertFalse(car.engine.needs_service())


if __name__ == '__main__':
    unittest.main()
