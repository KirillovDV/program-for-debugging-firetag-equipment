from colorama import Fore


def serial_scanner():
    import serial.tools.list_ports

    list_of_serial_ports = serial.tools.list_ports.comports()
    connected = []
    str(connected)
    for element in list_of_serial_ports:
        connected.append(element.device)
    # connected = str(connected)
    # for element in connected:
    #     print(element)
    return connected


def comports():
    for element in serial_scanner():
        print(Fore.RED + element, Fore.CYAN)


def com_writer(massive, selected_port):
    import serial
    ser = serial.Serial(selected_port, 9600, timeout=1)
    for e in massive:
        ser.write(bytes(e, encoding='utf8'))
        result = ser.readline()
        print(result.decode('utf-8'))
    ser.close()