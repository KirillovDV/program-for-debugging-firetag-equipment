import serial
if __name__ == '__main__':
    # import serial_port_scaner
    # from serial_port_scaner import selected_port
    #
    # print(selected_port)
    from colorama import Fore, Style
    # from serial_port_tools import serial_scanner, comports, numbers_to_bin, reader, com_writer
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

            if menu_choice == 'reader':
                clear()  # Отчистака терминала/командной строки
                reader()
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
