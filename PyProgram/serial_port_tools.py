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


def interpreter():
    def numbers_to_bin():
        # флаг ошибки
        flag_error = False
        # массив допустимых значений
        massive_right = [range(1, 129),
                         range(1, 5),
                         [1, 2, 4, 5, 7, 10, 15, 17, 20, 25, 30, 35, 40, 50, 75, 100],
                         [0, 1],
                         range(1, 257),
                         range(1, 257),
                         range(1, 257)]
        # массив для надписей при вводе
        input_text = ['Ведите ID (от 1 до 128): ——> ',
                      'Ведите команду (от 1 до 4): ——> ',
                      'Ведите урон (1 / 2 / 4 / 5 / 7 / 10 / 15 / 17 / 20 / 25 / 30 / 35 / 40 / 50 / 75 / 100): ——> ',
                      'Ведите учет дружественного огня (0 - нет; 1 - да): ——> ',
                      'Ведите кол-во жизней (от 1 до 256): ——> ',
                      'Ведите кол-во патронов в магазине (от 1 до 256): ——> ',
                      'Ведите ко-во магазинов (от 1 до 256): ——> ']
        # массив для вывода ошибок
        massive_print = ['>ID<', '>Команда<', '>Урон<', '>Дружественный огонь<',
                         '>Ко-во жизней<', '>Ко-во патронов в магазине<', '>Ко-во магазинов<']
        # пустой массив для вывода из функции
        massive_variable = []
        # цикл перебора переменных
        for i in range(7):
            try:
                variable = int(input(
                    input_text[
                        i]))  # это строчка нужна для ввода и обработки ошибки, когда пользователь вводит не цифры
                if variable in massive_right[i]:
                    # if проверяет есть ли число в диапазоне правильных значений - если да,то обрабатываем его
                    a = bin(massive_right[i].index(variable))[2:]  # переводим в двоичную систему и отсекаем 0b
                    variable = '0' * (8 - len(a)) + a  # дописываем нули до 8 бит
                    massive_variable.append(variable)  # записываем в тот же массив в формате str
                else:
                    # если числа нет в диапазоне допустимых значений, то сообщаем об ошибке через флаг, даже если ошибка всего одна
                    # flag_error = True
                    print(Fore.RED + 'Паблитто Даунитто, ты ввел недопустимые значения в ', massive_print[i],
                          Fore.WHITE)
                    break
            except ValueError:
                # обработка ошибки, когда пользователь вводит не цифры
                # flag_error = True
                print(Fore.RED + 'Паблитто Дауниттос, ты ввел недопустимый формат в ', massive_print[i], Fore.WHITE)
                break
        # return flag_error, massive_variable
        if len(massive_variable) == 7:
            return massive_variable
        else:
            return False

    massive = False
    while not massive:
        # если функция выдала ошибку то мы спрашиваем у пользователя и вводим флаг,отвечающий за продолжения или
        # выход из цикла
        massive = numbers_to_bin()
        if not massive:
            flag = 1
        else:
            flag = 0
        while flag == 1:
            vvod = input('Если вы хотите ввести данные заново введите 1, выйти - введите 0: ——> ')
            if vvod == '1':
                flag = 0
            elif vvod == '0':
                flag = 0
                massive = True
            else:
                flag = 1
                print('Вы ввели некорректное значение')


