from colorama import Fore
from serial_port_scanner import serial_scanner
from menus import main_menu, second_menu
import os

os.system('cls' if os.name == 'nt' else 'clear')


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
            print(Fore.RED + "Введено некорректное значение", Fore.WHITE)
            menu()


def main():
    while True:
        menu_choice = input(second_menu)
        menu_choice = menu_choice.lower()
        if menu_choice == 'com':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\n')
            comports()
            main()
            break

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
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Введено некорректное значение", Fore.WHITE)


def comports():
    for element in serial_scanner():
        print(Fore.RED + element, Fore.WHITE)


def start():
    print('Сейчас вам будет предложенно выбрать COM (serial) порт, к которому подключено ваше устройство. '
          'Далее вы перейдете к настройке устройства. \nЕсли вы не увидите подключенное устройство, введите \'help\''
          'и следуйте инструкциям\n\n')

    def selector(connected):
        for i, element in enumerate(connected):
            print(Fore.WHITE + f'Введите {i + 1} если хотите выбрать СОМ-порт {Fore.RED + element}', Fore.WHITE)
        number_com = int(input())
        return connected[number_com - 1]

    selected_port = selector(serial_scanner())
    print(f'Вы выбрали {Fore.RED + selected_port}', Fore.WHITE)


def help():
    print("справка по работе программы")
    print("")


if __name__ == '__main__':
    # import time
    # import serial
    # import datetime
    #
    # ser = serial.Serial('/dev/cu.usbserial-1410')
    # received = []
    #
    # ser.write(b'begin\n')
    # time.sleep(5)
    #
    # start = datetime.datetime.now()
    # for i in range(1, 100):
    #     ser.write(b'test%i\r\n' % i)
    #     time.sleep(0.005)
    #     while ser.inWaiting() > 0:
    #         line = ser.readline()
    #         if line:
    #             received.append(line.decode().strip())
    #
    # print(datetime.datetime.now() - start)
    # print(received)
    # # start()

    menu()
