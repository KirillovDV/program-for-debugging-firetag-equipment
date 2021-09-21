from colorama import Fore, Style


def serial_scanner():  # Todo comment
    import serial.tools.list_ports

    list_of_serial_ports = serial.tools.list_ports.comports()
    connected = []
    for element in list_of_serial_ports:
        connected.append(element.device)
        # print(connected)
    return connected


def selector(connected):
    for i, element in enumerate(connected):
        print(f'Введите {i + 1} если хотите выбрать СОМ-порт {element}')
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
        print(f'Вы выбрали {str(selected_port)}')
    else:
        flag = 1
        print('Вы ввели некорректное значение. Исправте ошибку')


# def comports():
#     for element in serial_scanner():
#         print(Fore.RED + element, Fore.CYAN)
#
# comports()