from GPS.GPSSerialReader import GPSSerialReader
from GPS.NMEAParser import NMEAParser

def main():
    serial_port = '/dev/serial0'
    baudrate = 9600
    timeout = 8

    gps_reader = GPSSerialReader(serial_port, baudrate, timeout)
    parser = NMEAParser()
    while True:
        nmea_line = gps_reader.read_line()
        location = parser.parse_location(nmea_line)
        if location is not None:
            print(f"MAIN LOCATION :{location}")

if __name__ == "__main__":
    main()