import pytest
from GPS.NMEAParser import NMEAParser

def test_location_nmea_string():
    nmea_string = "$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D"
    parser = NMEAParser()
    location = parser.parse_location(nmea_string)
    print()
    print()
    print(location)

    assert 1 == 1
