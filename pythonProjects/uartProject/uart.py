# UART connecions on raspi 4
# PIN 8 : GPIO 14 : UART0_TX
# PIN 10: GPIO 16 : UART0_RX
# PIN 6 : GND     : GND

# this program demonstrates uart loopback

import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 115200)    #Open port with baud rate

while True:
    ser.write("\r\necho one chr\r\n")           # print a promt to input one chr
    received_data = ser.read()              # read serial port, by default it will read one byte
    print (received_data)                   # print received data
    ser.write(received_data)                # echo the input data
    ser.write("\r\n")
    ser.write("input 10 characters\r\n")    # print a promt to input 10 chr
    received_data = ser.read(10)
    ser.write(received_data)                # echo the input data