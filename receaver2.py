import socket

HOST = '10.10.11.208'  # The server's hostname or IP address
ME = '10.10.14.46'
HOST = '192.168.178.23'
ME = "192.168.178.21"
PORT = 65432  # The port used by the server
PORT_R = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ME, PORT_R))
    print("Waiting for first connection...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        print(data.decode())
    s.close()

while True:
    # SEND
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        inp = input("Input command >")
        print("Connecting...")
        s.connect((HOST, PORT))
        s.sendall(bytes(inp, 'UTF-8'))
        print("Command sent")
        s.close()

    # LISTEN
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ME, PORT_R))
        print("Listening..")
        s.listen()
        conn, _ = s.accept()
        with conn:
            data = conn.recv(1024)
            print(data.decode())
        s.close
