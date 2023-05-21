import socket

def client_program():
    server_ip = "192.168.178.23"
    server_port = 65432

    print("Trying to connect to server...")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    message = input(" -> ")
    print("_______________________")

    while message.lower().strip() != "bye":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("<-- " + data)
        message = input(" -> ")

    client_socket.close()

if __name__ == "__main__":
    client_program()
