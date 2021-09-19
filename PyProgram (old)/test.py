import serial


if __name__ == '__main__':

    # s = serial.Serial('/dev/cu.usbmodem8D70129A53531')
    # res = s.read()
    # print(res)



    serialPort = serial.Serial(port="/dev/cu.usbmodem8D70129A53531", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    serialString = ""  # Used to hold data coming over UART
    while 1:
        # Wait until there xqis data waiting in the serial buffer
        serialPort.write(b"Hello World ")


        if serialPort.in_waiting > 0:

            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()

            # Print the contents of the serial data
            try:
                print(serialString.decode("Ascii"))
            except:
                pass
        