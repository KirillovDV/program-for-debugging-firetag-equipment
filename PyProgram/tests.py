def serial_scanner():
    import serial.tools.list_ports

    list_of_serial_ports = serial.tools.list_ports.comports()
    connected = []
    str(connected)
    for element in list_of_serial_ports:
        connected.append(element.device)
    # connected = str(connected)
    print(f"Connected COM (serial) ports: {connected} ")


# ID = 1-128 type: int
# team = 1-4 type: int
# damage = 1,2,4,5,7,10,15,17,20,25,30,35,40,50,75,100   type: int
# FF = 0,1 type: int
# HP = 1-256 type: int
# capacity = 1-256 type: int
# ammo = 1-256 type: int
def black_box(ID, team, damage, FF, HP, capacity, ammo):
    flag_error = False
    # ID
    if 0 < ID < 129:
        a = bin(ID - 1)[2:]
        ID = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите ID в диапазоне 1-128')
    # team
    if 0 < team < 5:
        a = bin(team - 1)[2:]
        team = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите команду в диапазоне 1-4')
    # damage
    mas = [1, 2, 4, 5, 7, 10, 15, 17, 20, 25, 30, 35, 40, 50, 75, 100]
    if damage in mas:
        a = bin(mas.index(damage))[2:]
        damage = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите урон в диапазоне 1,2,4,5,7,10,15,17,20,25,30,35,40,50,75,100')
    # FF
    if FF in [0, 1]:
        a = bin(FF)[2:]
        FF = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите дружественный огонь в диапазоне 0-1')
    # HP
    if 0 < HP < 257:
        a = bin(HP - 1)[2:]
        HP = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите ко-во жизней в диапазоне 1-256')
    # capasity
    if 0 < capacity < 257:
        a = bin(capacity - 1)[2:]
        capacity = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите ко-во патронов в магазине в диапазоне 1-256')
    # ammo
    if 0 < ammo < 257:
        a = bin(ammo - 1)[2:]
        ammo = '0' * (8 - len(a)) + a
    else:
        flag_error = True
        print('Введите ко-во магазинов в диапазоне 1-256')

    return flag_error, [ID, team, damage, FF, HP, capacity, ammo]


def concatenation(P1, P2, P3, P4, I1):
    P_b1 = bin(int(P1, 2))
    P_b2 = bin(int(P2 + P3 + P4, 2))
    P_b3 = bin(int(I1, 2))
    return [P_b1, P_b2, P_b3]
    # return bytes(int(P,2))


print(concatenation('00000001', '11', '0', '0101', '1101'))

if __name__ == '__main__':
    serial_scanner()