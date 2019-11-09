from CustomTime import CustomTime
from Error import TimeZoneError
import unittest

class TestCustomTime(unittest.TestCase):

    def test_right_time_zone_error(self):
        try:
            time = CustomTime(_time_zone="Aseoul", _print=True)
        except TimeZoneError as tz_error:
            print(self.test_wrong_time_zone_error.__name__, "pass")

    def test_wrong_time_zone_error(self):
        try:
            time = CustomTime(_time_zone="Aseoul", _print=True)
        except TimeZoneError as tz_error:
            print(self.test_wrong_time_zone_error.__name__, "pass")

if __name__ == '__main__':
    unittest.main()