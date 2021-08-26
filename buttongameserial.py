import serial
import sys
import pyautogui
import time

print(len(sys.argv))

pyautogui.FAILSAFE = False

serial_port = sys.argv[1] if len(sys.argv) > 1 else '/dev/ttyACM0'
baud_rate = int(sys.argv[2]) if len(sys.argv) > 2 else 9600
ser = serial.Serial(serial_port, baud_rate)


while True:
    fulltext = ""
    command = ser.read()
    if command:
        ser.flushInput()
        print("new command:", str(command.decode()))

        if str(command.decode()) == '1':
            print("jumping")
            pyautogui.press("up")
            time.sleep(0.6)

        elif str(command) == '2':
            print("crawling")
            pyautogui.press("down")

        else:
            print("Not a valid command")
