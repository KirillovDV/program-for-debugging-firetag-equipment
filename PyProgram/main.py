from colorama import Fore, Style
from serial_port_tools import serial_scanner, comports, interpreter
from literals import main_menu, second_menu, info
import os


def clear():  # функция отчистки терминала/командной строки
    os.system('cls' if os.name == 'nt' else 'clear')


print(Style.RESET_ALL)
clear()  # Отчистака терминала/командной строки


def menu():  # Главное меню

    while True:
        menu_choice = input(Fore.WHITE + main_menu)  # Запрос ввода пункта меню (внешний вид из фала literals.py)
        menu_choice = menu_choice.lower()  # Приведение введенного значения к нижнему регистру

        if menu_choice == 'exit':  # Если введено "Exit"
            clear()  # Отчистака терминала/командной строки
            exit()  # Выход из программы

        if menu_choice == 'start':  # Если введено "Start"
            clear()  # Отчистака терминала/командной строки
            main()  # Вызов функции main()
            break  # Выход из цикла

        if menu_choice == 'help':  # Если введено "Start"
            clear()  # Отчистака терминала/командной строки
            help()  # Вызов функции main()
            break  # Выход из цикла

        else:  # Если введенно некорректное значение
            clear()  # Отчистака терминала/командной строки
            print(Fore.RED + "Введено некорректное значение", Fore.WHITE)
            menu()  # Вызов функции menu()


def main():  # Второе меню
    while True:
        menu_choice = input(second_menu)  # Запрос ввода пункта меню (внешний вид из literals.py)
        menu_choice = menu_choice.lower()  # Приведение введенного значения к нижнему регистру
        if menu_choice == 'com':
            clear()  # Отчистака терминала/командной строки
            print('\n\n')
            comports()  # Вывод обнаруженных COM (serial) портов (из serial_port_tools.py)
            input('\nНажмите \'Enter\', что бы выйти в меню')
            clear()  # Отчистака терминала/командной строки
            main()
            break  # Выход из цикла

        if menu_choice == 'start':
            clear()  # Отчистака терминала/командной строки
            configurator()
            break  # Выход из цикла

        if menu_choice == 'exit':
            clear()  # Отчистака терминала/командной строки
            exit()

        if menu_choice == 'menu':
            clear()  # Отчистака терминала/командной строки
            menu()  # Вызов главного меню (выход назад)
            break  # Выход из цикла

        else:
            clear()  # Отчистака терминала/командной строки
            print(Fore.RED + "Введено некорректное значение", Fore.WHITE)


# def configurator(): print('Сейчас вам будет предложенно выбрать COM (serial) порт, к которому подключено ваше
# устройство. ' 'Далее вы перейдете к настройке устройства. \nЕсли вы не увидите подключенное устройство,
# введите \'info()\'' 'и следуйте инструкциям\n\n')
#
#     def selector(connected):
#         for i, element in enumerate(connected):
#             print(Fore.WHITE + f'Введите {i + 1} если хотите выбрать СОМ-порт {Fore.RED + element}', Fore.WHITE)
#         try:
#             number_com = int(input())
#             if int(number_com) in range(1, len(connected) + 1):
#                 print("Все норм")
#                 return connected[int(number_com) - 1]
#         except ValueError:
#             return False
#
#     flag = 1
#     while flag == 1:
#         selected_port = selector(serial_scanner())
#         if selected_port:
#             flag = 0
#             print(f'Вы выбрали {Fore.RED + selected_port}', Fore.WHITE)
#         else:
#             flag = 1
#             print('Вы ввели некорректное значение. Исправте ошибку')
#
#     flag = 1
#     fl_er, massive = interpreter.numbers_to_bin(interpreter.input_numbers())
#     while flag == 1 and fl_er == True:
#         # если функция выдала ошибку то мы спрашиваем у пользователя и вводим флаг,
#         # отвечающий за продолжения или выход из цикла
#         try:
#             flag = int(input('Если вы хотите ввести данные заново введите 1, выйти - введите 0: ——> '))
#         except ValueError:
#             flag = 1
#             print('Вы ввели некорректное значение')
#         else:
#             # если ошибки нет, то выходим из цикла
#             flag = 1
#             # TODO
#         print(massive)
#     input("Eckb pjbnnt lf tap enter")
#     com_writer(massive, selected_port)


def configurator():
    print('Сейчас вам будет предложенно выбрать COM (serial) порт, к которому подключено ваше устройство. '
          'Далее вы перейдете к настройке устройства. \nЕсли вы не увидите подключенное устройство, '
          'введите \'info\' '
          'и следуйте инструкциям\n\n')

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

    interpreter()




def help():
    print("справка по работе программы\n")
    print(info)
    input('\nНажмите \'Enter\', что бы выйти в меню')
    clear()
    menu()


if __name__ == '__main__':
    menu()
