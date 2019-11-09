import datetime
import time
import pytz
from Error import TimeZoneError

class CustomTime:

    def __init__(self, _time_zone="UTC", _print=False):
        self.time_zone = _time_zone
        self._print = _print

        # check timeZone
        self._check_time_zone()
        # Set now time   
        self._set_now()

    def _now(self):
        nowTime = datetime.datetime.utcnow().replace(tzinfo = pytz.utc)
        return nowTime
    
    def _set_now(self):
        self.custom_time_zone = pytz.timezone(self.time_zone) 
        self.now = self._now().astimezone(self.custom_time_zone)

    def _check_time_zone(self):
        if not (self.time_zone in pytz.all_timezones):
            raise TimeZoneError()

        if self._print:
            print(f"[TimeZone]{self.time_zone}")
            ## TODO search when user put wrong timezone.
