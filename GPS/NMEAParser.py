import pynmea2
from GPS.Location import Location
class NMEAParser:
    def __init__(self) -> None:
        pass

    def parse_location(self, nmea_line : str) -> Location:
        if not nmea_line.startswith("$GPGGA"):
            return None
        try:
            msg = pynmea2.parse(nmea_line)
            timestamp = msg.timestamp
            latitude = msg.lat
            longitude = msg.lon
            return Location(timestamp, latitude, longitude)
        except Exception:
            print("Could not parse NMEA")
            print(Exception)
