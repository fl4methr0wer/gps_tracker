import serial
class GPSSerialReader:
    def __init__(self, port='/dev/ttyAMA0', baudrate=9600, timeout=1) -> None:
        self.ser = serial.Serial(port, baudrate, timeout)

    def read_line(self) -> str:
        try:
            return self.ser.readline().decode('utf-8', errors='replace').strip()
        except UnicodeDecodeError:
            print("UnicodeDecodeError: Unable to decode the received data.")
            return ""
