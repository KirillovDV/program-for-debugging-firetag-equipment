import serial_port_scanner
from serial_port_scanner import serial_scanner

# import os


def menu():
    while True:
        menu_choice = input('''
____________________________________________
|                                          |
|   ,--.   ,--.                            |
|   |   `.'   | ,---. ,--,--, ,--.,--.     |
|   |  |'.'|  || .-. :|      \|  ||  |     |
|   |  |   |  |\   --.|  ||  |'  ''  '     |
|   `--'   `--' `----'`--''--' `----'      |
|                                          |
|                                          |
|  Для начала настройки введите 'start'    |
|  Для получения справки введите 'help'    |
|  Для выхода из программы введите 'exit'  |
|__________________________________________|    
    
——> ''')
        menu_choice = menu_choice.lower()

        if menu_choice == 'exit':
            exit()

        if menu_choice == 'start':
            main()
            break

        else:
            print("Введено некорректное значение")


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
            print(serial_scanner())
            main()

        if menu_choice == 'start':
            start()
            break

        if menu_choice == 'exit':
            exit()

        if menu_choice == 'menu':
            menu()
            break

        else:
            print("Введено некорректное значение")


def start():

    def choose(connected):
        for i, element in enumerate(connected):
            print(f'Введите {i + 1} если хотите выбрать  СОМ-порт {element} ')
        number_com = int(input())
        return connected[number_com - 1]

    choose_com = choose(serial_scanner())
    selected_port = choose_com
    print(f'Вы выбрали {selected_port}')




def help():
    print("справка по работе программы")


if __name__ == '__main__':
    menu()
