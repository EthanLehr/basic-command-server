import socket
from datetime import datetime
import random

HOST = "0.0.0.0"  # Symbolic name meaning all available interfaces
PORT = 8820  # Arbitrary non-privileged port
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)

conn, addr = socket.accept()
print('Connected by', addr)
while True:
    data = conn.recv(10)
    print(data.decode())
    if data.decode() == "time":
        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        conn.send(str(len(date_time)).encode())
        conn.send(date_time.encode())

    if data.decode() == "WHORU":
        name = ["my name is maor edri"]
        print("my name is maor edri")

    if data.decode() == "RAND":
        print(random.randint(1,10))
    else:
        break
    conn.sendall(data)
conn.close()


