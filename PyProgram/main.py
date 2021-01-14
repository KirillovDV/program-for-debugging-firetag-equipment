from colorama import Fore
from serial_port_tools import serial_scanner, comports
from literals import main_menu, second_menu, help
import os
import interpreter

os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки


def menu():  # Главное меню

    while True:
        menu_choice = input(Fore.WHITE + main_menu)  # Запрос ввода пункта меню (внешний вид из фала literals.py)
        menu_choice = menu_choice.lower()  # Приведение введенного значения к нижнему регистру

        if menu_choice == 'exit':  # Если введено "Exit"
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            exit()  # Выход из программы

        if menu_choice == 'start':  # Если введено "Start"
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            main()  # Вызов функции main()
            break  # Выход из цикла

        else:  # Если введенно некорректное значение
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            print(Fore.RED + "Введено некорректное значение", Fore.WHITE)
            menu()  # Вызов функции menu()


def main():  # Второе меню
    while True:
        menu_choice = input(second_menu)  # Запрос ввода пункта меню (внешний вид из literals.py)
        menu_choice = menu_choice.lower()  # Приведение введенного значения к нижнему регистру
        if menu_choice == 'com':
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            print('\n\n')
            comports()  # Вывод обнаруженных COM (serial) портов (из serial_port_tools.py)
            input('\nНажмите \'Enter\', что бы выйти в меню')
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            main()
            break  # выход из цикла

        if menu_choice == 'start':
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            configurator()
            break

        if menu_choice == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            exit()

        if menu_choice == 'menu':
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            menu()
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Отчистака терминала/командной строки
            print(Fore.RED + "Введено некорректное значение", Fore.WHITE)


def configurator():
    print('Сейчас вам будет предложенно выбрать COM (serial) порт, к которому подключено ваше устройство. '
          'Далее вы перейдете к настройке устройства. \nЕсли вы не увидите подключенное устройство, введите \'help\''
          'и следуйте инструкциям\n\n')

    def selector(connected):
        for i, element in enumerate(connected):
            print(Fore.WHITE + f'Введите {i + 1} если хотите выбрать СОМ-порт {Fore.RED + element}', Fore.WHITE)
        number_com = input()
        return connected[int(number_com) - 1]

    selected_port = selector(serial_scanner())
    print(f'Вы выбрали {Fore.RED + selected_port}', Fore.WHITE)

    flag = 1
    while flag == 1:
        fl_er, massive = interpreter.numbers_to_bin(interpreter.input_numbers())

        if fl_er:
            # если функция выдала ошибку то мы спрашиваем у пользователя и вводим флаг,
            # отвечающий за продолжения или выход из цикла
            flag = int(input('Если вы хотите ввести данные заново введите 1, выйти - введите 0: ——> '))
        else:
            # если ошибки нет, то выходим из цикла
            flag = 0
        print(massive)
        print(f'type of "massive is {type(massive)}"')
        massive = [bin(i) for i in massive]
        print(massive)
        print(f'type of "massive is {type(massive)}"')


def help():
    print("справка по работе программы")
    print(help)


if __name__ == '__main__':

    menu()
