from GPS.GPSSerialReader import GPSSerialReader
from GPS.NMEAParser import NMEAParser
from persistence.LocationSQLiteDAO import LocationSQLiteDAO
def main():
    serial_port = '/dev/serial0'
    baudrate = 9600
    timeout = 8

    gps_reader = GPSSerialReader(serial_port, baudrate, timeout)
    parser = NMEAParser()

    location_dao = LocationSQLiteDAO("locations.db")
    while True:
        nmea_line = gps_reader.read_line()
        location = parser.parse_location(nmea_line)
        if location is not None:
            location_id = location_dao.create(location)
            print(f"MAIN LOCATION :{location}")

if __name__ == "__main__":
    main()