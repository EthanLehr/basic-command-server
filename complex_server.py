import math
import socket
from datetime import datetime
import random
import pyautogui
import os
import subprocess
import webbrowser

HOST = "0.0.0.0"  # Symbolic name meaning all available interfaces
PORT = 8820  # Arbitrary non-privileged port
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)

conn, addr = socket.accept()
print('Connected by', addr)
while True:
    data = conn.recv(50)
    print(data.decode())
    if data.decode() == "screenshot":
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'screenshot.png')

    if data.decode() == "open chrome":
        subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])

    if data.decode() == "open youtube":
        webbrowser.open("http://youtube.com", new=1)

    if data.decode() == "RAND":
        print(random.randint(1,10))

    if data.decode() == "send screenshot":
        file = open("screenshot.png", 'rb')
        size = os.path.getsize("screenshot.png")
        print(size)
        num_of_full_iteration = size // 1024 #floor divition
        size_of_part_iteration = size % 1024
        b = file.read(1024)
        tot_num_of_iteration = math.ceil(size / 1024)
        conn.sendall((tot_num_of_iteration).to_bytes(69, byteorder='big'))
        for i in range(num_of_full_iteration):
            conn.sendall((1024).to_bytes(4, byteorder='big'))
            conn.sendall(b)
            b = file.read(1024)
        conn.sendall((size_of_part_iteration).to_bytes(4, byteorder='big'))
        conn.sendall(b)
        file.close()

    if data.decode() == "show folder":
        list_dir = os.listdir()
        conn.sendall(str(list_dir).encode())


    if data.decode() == "done":
        break
conn.close()


