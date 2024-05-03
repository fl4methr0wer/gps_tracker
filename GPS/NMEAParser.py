import pynmea2
from GPS.Location import Location


class NMEAParser:
    def __init__(self) -> None:
        pass

    def is_location(self, nmea_line: str) -> bool:
        return nmea_line.startswith("$GPGGA")

    def parse_location(self, nmea_line: str) -> Location:
        if not self.is_location(nmea_line):
            return None
        try:
            msg = pynmea2.parse(nmea_line)
            print(type(msg))
            return self.__message_to_location(msg)
        except pynmea2.ParseError as e:
            print(f"Could not parse NMEA: {e}")

    def __message_to_location(self, gga_message : pynmea2.types.talker.GGA) -> Location:
        timestmp = gga_message.timestamp
        latitude = gga_message.lat
        longitude = gga_message.lon
        return Location(timestmp, latitude, longitude)
