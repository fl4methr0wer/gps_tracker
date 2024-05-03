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
            return self.__message_to_location(msg)
        except pynmea2.ParseError as e:
            print(f"Could not parse NMEA: {e}")

    def __message_to_location(
            self, nmea_sentence : pynmea2.ProprietarySentence | pynmea2.QuerySentence) -> Location:
        timestmp = nmea_sentence.timestamp
        latitude = nmea_sentence.lat
        longitude = nmea_sentence.lon
        return Location(timestmp, latitude, longitude)
