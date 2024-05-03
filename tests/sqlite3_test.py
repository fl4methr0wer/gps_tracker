from GPS.Location import Location
from persistence.LocationSQLiteDAO import LocationSQLiteDAO
from datetime import time
import datetime

def test_sqlite3():
    sqlite_dao = LocationSQLiteDAO("test.db")
    timestamp = time(20, 43, 54, 70000, tzinfo=datetime.timezone.utc)
    latitude = "51.4673633"
    longitude = "20.3957388"
    location_to_save = Location(timestamp,latitude, longitude)
    print(f"ABOUT TO SAVE: {location_to_save}")
    location_id = sqlite_dao.create(location_to_save)
    db_location = sqlite_dao.read(location_id)
    assert location_to_save == db_location
