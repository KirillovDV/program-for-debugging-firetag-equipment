from serial_port_scanner import serial_scanner

def menu():
    while True:
        menu_choice = input('''
Для начала настройки введите 'start'
Для получения справки введите 'help'
Для выхода введите 'exit'
    
——> ''')
        menu_choice = menu_choice.lower()

        if not menu_choice:
            print('Вы ничего не ввели')

        if menu_choice == 'exit':
            exit()

        if menu_choice == 'start':
            print('QQ')
            break

        else:
            print('Повторите ввод')


def main():
    menu_choice = input('''
Для вывода доступных COM портов введите 'сom' 

    ——> ''')
    menu_choice = menu_choice.lower()
    if menu_choice == 'com':
        serial_scanner()


def help():
    pass

# def help():
#     pass


if __name__ == '__main__':
    main()
