import serial
import time
# a = ('{0:08b}'.format(1))
# print(bin,bytearray(a))

serialPort = serial.Serial(port="/dev/cu.usbmodem8D70129A53531", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""  # Used to hold data coming over UART

# a = ('{0:08b}'.format(1))


# serialPort.write(b'')

while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            print(serialString.decode("Ascii"))
        except:
            pass
