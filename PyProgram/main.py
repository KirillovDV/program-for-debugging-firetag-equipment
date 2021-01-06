from serial_port_scanner import serial_scanner
# import os


def menu():
    while True:
        menu_choice = input('''
Для начала настройки введите 'start'
Для получения справки введите 'help'
Для выхода из программы введите 'exit'
    
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
    menu_choice = input('''
Для вывода доступных COM портов введите 'сom' 
Для начала настройки платы введиете 'start'
Для выхода из программы введите 'exit'
Для выхода в меню введите 'menu'

——> ''')
    menu_choice = menu_choice.lower()
    if menu_choice == 'com':
        serial_scanner()
        main()

    if menu_choice == 'start':
        pass

    if menu_choice == 'exit':
        exit()

    if menu_choice == 'menu':
        menu()

    else:
        print("Введено некорректное значение")


def help():
    pass


if __name__ == '__main__':
    menu()
