import sqlite3
from persistence.LocationDAO import LocationDAO
from GPS.Location import Location
from typing import List

class LocationSQLiteDAO(LocationDAO):
    def __init__(self, db_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            latitude TEXT,
            longitude TEXT
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def create(self, location: Location) -> int:
        insert_query = 'INSERT INTO locations (timestamp, latitude, longitude) VALUES (?, ?, ?)'
        data = (str(location.timestamp), location.latitude, location.longitude)
        self.cursor.execute(insert_query, data)
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, location_id: int) -> Location:
        select_query = 'SELECT * FROM locations WHERE id = ?'
        self.cursor.execute(select_query, (location_id,))
        row = self.cursor.fetchone()
        if row:
            return Location(row[1], row[2], row[3])  # Assuming the order of columns is timestamp, latitude, longitude
        else:
            return None

    def update(self, location_id: int, new_location: Location) -> None:
        update_query = 'UPDATE locations SET timestamp=?, latitude=?, longitude=? WHERE id=?'
        data = (str(new_location.timestamp), new_location.latitude, new_location.longitude, location_id)
        self.cursor.execute(update_query, data)
        self.conn.commit()

    def delete(self, location_id: int) -> None:
        delete_query = 'DELETE FROM locations WHERE id=?'
        self.cursor.execute(delete_query, (location_id,))
        self.conn.commit()

    def read_all(self) -> List[Location]:
        select_query = 'SELECT * FROM locations'
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        locations = []
        for row in rows:
            locations.append(Location(row[1], row[2], row[3]))  # Assuming the order of columns is timestamp, latitude, longitude
        return locations

    def __del__(self) -> None:
        self.cursor.close()
        self.conn.close()
