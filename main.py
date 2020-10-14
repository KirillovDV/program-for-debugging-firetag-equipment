import serial
from serialports import *

print(f"найденно подключенных устройств: {len(serial_ports)}")
print (serial_ports)

# def serial_ports_list(lst):
#     for elements in serial_ports:
#         print(serial_ports)
