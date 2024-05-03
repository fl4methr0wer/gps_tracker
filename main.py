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
        print(f"MAIN LOCATION :{location}")



# def main2():
#     serial_port = "/dev/serial0"
#     baudrate = 9600
#     timeout = 1
#
#     ser = serial.Serial(serial_port, baudrate, timeout=timeout)
#     print(f"SERIAL : {ser}")
#
#     while True:
#         try:
#             line = ser.readline().decode('utf-8', errors='replace').strip()
#             if line.startswith('$GPGGA'):
#                 try:
#                     msg = pynmea2.parse(line)
#                     timestamp = datetime.combine(datetime.utcnow().date(), msg.latitude = round(msg.latitude, 4)
#                     longitude = round(msg.longitude, 4)
#                     print(f"{timestamp}|{latitude}|{longitude}")
#                 except pynmea2.ParseError as e:
#                     print("Parse error:", e)
#         except UnicodeDecodeError:
#             print("UnicodeDecodeError: Unable to decode the received data.")

if __name__ == "__main__":
    main()