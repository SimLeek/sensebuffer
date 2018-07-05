import sys
import glob
import serial
import struct

#https://stackoverflow.com/a/14224477/782170
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class SerialError(Exception):
    pass

def check_byte_packing(ser):
    test_float_bytes = ser.read(4)
    if len(test_float_bytes)!=4: raise SerialError("Initial test bytes not read. Short serial timeout likely cause.")
    test_float = struct.unpack('f', test_float_bytes)[0]
    if not (3.14160 > test_float > 3.14158): raise SerialError("Test float not converted correctly.")


class SertialStateMachine( object ):
    def __init__(self, ser):
        self.ser = ser

        self.start_state = {}
        self.current_state = {}
        self.inertial_state = {}

        self.current_state = self.start_state

        self.start_state[b'I'] = self.run_inertial_state

        self.inertial_state[b'a'] = self.run_read_acceleration
        self.inertial_state[b'm'] = self.run_read_magnetometer
        self.inertial_state[b'g'] = self.run_read_gyroscope
        self.inertial_state[b'I'] = self.run_inertial_state

        self.exit = False

    def __call__(self, character):
        while character==b'\n':
            return

        self.current_state[character]()

    def run_inertial_state(self):
        self.current_state = self.inertial_state

    def run_read_acceleration(self):
        ax_b = ser.read(4)
        ay_b = ser.read(4)
        az_b = ser.read(4)

        ax = struct.unpack('f', ax_b)[0]
        ay = struct.unpack('f', ay_b)[0]
        az = struct.unpack('f', az_b)[0]

        print("accel",ax,ay,az)

        self.run_inertial_state()

    def run_read_magnetometer(self):
        mx_b = ser.read(4)
        my_b = ser.read(4)
        mz_b = ser.read(4)

        mx = struct.unpack('f', mx_b)[0]
        my = struct.unpack('f', my_b)[0]
        mz = struct.unpack('f', mz_b)[0]

        print("compass", mx, my, mz)

        self.run_inertial_state()

    def run_read_gyroscope(self):
        gx_b = ser.read(4)
        gy_b = ser.read(4)
        gz_b = ser.read(4)

        gx = struct.unpack('f', gx_b)[0]
        gy = struct.unpack('f', gy_b)[0]
        gz = struct.unpack('f', gz_b)[0]

        print("gyro", gx, gy, gz)

        self.run_inertial_state()


if __name__ == '__main__':
    all_ports = serial_ports()


    for p in all_ports:
        with serial.Serial(p, 9600, timeout=10) as ser:
            check_byte_packing(ser)

            ssm = SertialStateMachine(ser)
            while not ssm.exit:
                ssm(ser.read(1))








