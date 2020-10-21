import serial
from serialports import *

print(f"найденно подключенных устройств: {len(serial_ports)}\n")

for i in serial_ports:
    print(i)

