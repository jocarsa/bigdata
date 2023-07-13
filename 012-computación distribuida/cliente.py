import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = "Hello, server!"
    numero = 1.0000000034
    for i in range(0,1000000000):
        numero *= 1.000000000054
    message = str(numero)
    client_socket.sendall(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print("Server response:", response)

    client_socket.close()

# Example usage
host = '192.168.1.74'  # Change to server's host IP or hostname
port = 12345  # Change to server's port number
start_client(host, port)
