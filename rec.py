import socket

def client_program():
    server_ip = "127.0.0.1"
    server_port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    message = input(" -> ")

    while message.lower().strip() != "bye":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Received from server: " + data)
        message = input(" -> ")

    client_socket.close()

if __name__ == "__main__":
    client_program()
