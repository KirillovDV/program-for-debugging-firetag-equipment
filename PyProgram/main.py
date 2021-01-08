
from colorama import Fore, Back, Style
from serial_port_scanner import serial_scanner

from menus import main_menu
import os


# —————————————————————— Main (first) menu of the program ——————————————————————


def menu():
    while True:
        menu_choice = input(Fore.WHITE + main_menu)
        menu_choice = menu_choice.lower()

        if menu_choice == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        if menu_choice == 'start':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Введено некорректное значение")
            menu()


def main():
    while True:
        menu_choice = input('''
Для вывода доступных COM портов введите 'сom' 
Для начала настройки платы введиете 'start'
Для выхода из программы введите 'exit'
Для выхода в меню введите 'menu'
    
——> ''')
        menu_choice = menu_choice.lower()
        if menu_choice == 'com':
            os.system('cls' if os.name == 'nt' else 'clear')
            comports()
            main()

        if menu_choice == 'start':
            os.system('cls' if os.name == 'nt' else 'clear')
            start()
            break

        if menu_choice == 'exit':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        if menu_choice == 'menu':
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
            break

        else:
            print("Введено некорректное значение")


def comports():
    for element in serial_scanner():
        print(Fore.RED + element, Fore.WHITE)


def start():

    def selector(connected):
        for i, element in enumerate(connected):
            print(Fore.WHITE + f'Введите {i + 1} если хотите выбрать  СОМ-порт {Fore.RED + element}', Fore.WHITE)
        number_com = int(input())
        return connected[number_com - 1]

    selected_port = selector(serial_scanner())
    print(f'Вы выбрали {Fore.RED + selected_port}', Fore.WHITE)

    main()


def help():
    print("справка по работе программы")


if __name__ == '__main__':
    menu()
