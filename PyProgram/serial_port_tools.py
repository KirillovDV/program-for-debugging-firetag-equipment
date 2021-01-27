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
