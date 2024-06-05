import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, server!"
    client_socket.sendall(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print("Server response:", response)

    client_socket.close()

# Example usage
host = '192.168.1.74'  # Change to server's host IP or hostname
port = 12345  # Change to server's port number
start_client(host, port)
