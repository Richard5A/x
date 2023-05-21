import socket
import threading

HOST = '192.168.178.23'
ME =   "192.168.178.21"
PORT = 65432  # The port used by the server
PORT_R = 65434


def send_command():
    print("Starting send_command...")
    while True:
        inp = input("Input command repyl>")
        print("Connecting...")
        send_socket.sendall(bytes(inp, 'UTF-8'))
        print("Command sent")

        if inp == "BREAK OUT":
            break
    send_socket.close()


def listen_for_response():
    print("Starting listen_for_response...")
    while True:
        print("Listening..")
        listen_socket.listen()
        connection, _ = listen_socket.accept()
        with connection:
            data = connection.recv(1024)
            print(data.decode())


send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_socket.connect((HOST, PORT))

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((ME, PORT_R))

listen_socket.listen()
conn, _ = listen_socket.accept()
print(conn.recv(1024).decode())

thread_listen = threading.Thread(target=send_command, name="Listen Thread")
thread_response = threading.Thread(target=listen_for_response, name="Response Thread")


thread_listen.start()
thread_response.start()
