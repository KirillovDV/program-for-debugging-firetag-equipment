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


"""Первое правило - пользователь всегда долбоящер, который вбивает не те числа и все ломает
Мы обрабатываем их ошибки ввода внутри функции - это другие типы данных или интовые числа,
которые выходят за границы допустимых диапозонов. Именно для этого я ввел 
флаг ошибки, ты будешь его принимать и зацикливать ввод данных пока пользователь
не введет их правильно.
"""


# ID = 1-128 type: int
# team = 1-4 type: int
# damage = 1,2,4,5,7,10,15,17,20,25,30,35,40,50,75,100   type: int
# FF = 0,1 type: int
# HP = 1-256 type: int
# capacity = 1-256 type: int
# ammo = 1-256 type: int

def input_numbers():
    ID = input('Ведите ID (1-128): ——> ')
    team = input('Ведите команду (1-4):  ')
    damage = input('Ведите урон (1,2,4,5,7,10,15,17,20,25,30,35,40,50,75,100): ——> ')
    ff = input('Ведите учет дружественного огня (0-1): ——> ')
    hp = input('Ведите кол-во жизней (1-256): ——> ')
    capacity = input('Ведите кол-во патронов в магазине (1-256): ——> ')
    ammo = input('Ведите ко-во магазинов (1-256): ——> ')
    return [ID, team, damage, ff, hp, capacity, ammo]


class Interpreter:
    def numbers_to_bin(self, massive_variable):
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
        # массив для вывода ошибок
        massive_print = ['>ID<', '>Команда<', '>Урон<', '>Дружественный огонь<',
                         '>Ко-во жизней<', '>Ко-во патронов в магазине<', '>Ко-во магазинов<']
        # цикл перебора переменных
        for i, variable in enumerate(massive_variable):
            try:
                variable = int(variable)
                if variable in massive_right[i]:
                    # если число есть в диапазоне то обрабатываем его
                    a = bin(massive_right[i].index(variable))[2:]  # переводим в двоичную систему и отсекаем 0b
                    variable = '0' * (8 - len(a)) + a  # дописываем нули до 8 бит
                    massive_variable[i] = variable  # записываем в тот же массив
                else:
                    # если нет то сообщаем об ошибке через флаг, даже если она всего лишь одна
                    flag_error = True
                    print('Паблитто Даунитто, ты ввел недопустимые значения в ', massive_print[i])
            except ValueError:
                print('Паблитто Даунитто, ты ввел недопустимый формат в ', massive_print[i])

        return flag_error, massive_variable

    # флаг для работы цикла
    flag = 1
    while flag == 1:
        fl_er, massive = numbers_to_bin(input_numbers())

        if fl_er:
            # если функция выдала ошибку то мы спрашиваем у пользователя и вводим флаг,
            # отвечающий за продолжения или выход из цикла
            flag = int(input('Если вы хотите ввести данные заново введите 1, выйти - введите 0: ——> '))
        else:
            # если ошибки нет, то выходим из цикла
            flag = 0


if __name__ == '__main__':
    Interpreter.numbers_to_bin(input_numbers())


