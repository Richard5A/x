import socket
import threading

HOST = '192.168.178.23'
ME = "192.168.178.21"
PORT = 65432  # The port used by the server
PORT_R = 65434


def send_command():
    print("Starting send_command...")
    while True:
        inp = input("Input command repyl>")
        print("Connecting...")
        send_socket.sendall(bytes(inp, 'UTF-8'))
        print("Command sent")
    send_socket.close()


def listen_for_response():
    print("Starting listen_for_response...")
    while True:
        print("Listening..")
        listen_socket.listen()
        conn, _ = listen_socket.accept()
        with conn:
            data = conn.recv(1024)
            print(data.decode())


# create the socket outside the loop
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # set the socket options
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ME, PORT_R))
    s.listen()
    s.close()

thread_listen = threading.Thread(target=send_command, name="Listen Thread")
thread_response = threading.Thread(target=listen_for_response, name="Response Thread")

send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_socket.connect((HOST, PORT))
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((ME, PORT_R))

thread_listen.start()
thread_response.start()
