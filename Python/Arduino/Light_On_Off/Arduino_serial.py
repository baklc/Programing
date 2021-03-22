import serial
ard = serial.Serial('COM3',9600)
def on():
    ard.write('0'.encode())
def off():
    ard.write('1'.encode())