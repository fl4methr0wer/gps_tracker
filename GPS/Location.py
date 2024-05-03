class Location(object):
    def __init__(self, timestamp, latitude, longitude):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"""Location(timestamp={self.timestamp},latitude={self.latitude},longitude={self.longitude})"""

