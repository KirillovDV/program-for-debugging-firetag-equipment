
if __name__ == '__main__':
    import serial
    from colorama import Fore, Style


    def serial_scanner():
        import serial.tools.list_ports

        list_of_serial_ports = serial.tools.list_ports.comports()
        connected = []
        str(connected)
        for element in list_of_serial_ports:
            connected.append(element.device)
            print(connected)
        # connected = str(connected)
        # for element in connected:
        #     print(element)
        return connected

    def selector(connected):
        for i, element in enumerate(connected):
            print(Fore.WHITE + f'Введите {i + 1} если хотите выбрать СОМ-порт {Fore.RED + element}', Fore.WHITE)
        try:
            number_com = int(input())
            if int(number_com) in range(1, len(connected) + 1):
                print("Все норм")
                return connected[int(number_com) - 1]
        except ValueError:
            return False

    flag = 1
    while flag == 1:
        selected_port = selector(serial_scanner())
        if selected_port:
            flag = 0
            print(f'Вы выбрали {Fore.RED + selected_port}', Fore.WHITE)
        else:
            flag = 1
            print('Вы ввели некорректное значение. Исправте ошибку')
    #
    # # a = ('{0:08b}'.format(1))
    # # print(bin,bytearray(a))
    #
    # serialPort = serial.Serial(port="/dev/cu.usbmodem8D70129A53531", baudrate=9600, bytesize=8, timeout=2,
    #                            stopbits=serial.STOPBITS_ONE)
    # serialString = ""  # Used to hold data coming over UART
    #
    # # a = ('{0:08b}'.format(1))
    #
    # # serialPort.write(b'')
    #
    # while 1:
    #     # Wait until there is data waiting in the serial buffer
    #     if serialPort.in_waiting > 0:
    #
    #         # Read data out of the buffer until a carraige return / new line is found
    #         serialString = serialPort.readline()
    #
    #         # Print the contents of the serial data
    #         try:
    #             print(serialString.decode("Ascii"))
    #         except:
    #             pass