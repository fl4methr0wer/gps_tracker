import datetime
import this


class Location(object):
    def __init__(self, timestamp: datetime.time, latitude: str, longitude: str):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"""Location(timestamp={self.timestamp},latitude={self.latitude},longitude={self.longitude})"""
    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        timestamps_equal = str(self.timestamp) == str(other.timestamp)
        latitude_equal = self.latitude == other.latitude
        longitude_equal = self.longitude == other.longitude
        return timestamps_equal and latitude_equal and longitude_equal
