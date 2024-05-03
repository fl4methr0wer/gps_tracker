import datetime

import pytest
from GPS.NMEAParser import NMEAParser
from GPS.Location import Location
from datetime import time

def test_location_nmea_string():
    nmea_string = "$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D"
    parser = NMEAParser()
    location = parser.parse_location(nmea_string)
    print(location)
    print(f"TIMESTAMP : {type(location.timestamp)} : {location.timestamp}")
    expected_timestamp = time(18, 43, 53, 70000, tzinfo=datetime.timezone.utc)
    assert expected_timestamp == location.timestamp

    assert 1 == 1
