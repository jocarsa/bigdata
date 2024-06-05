import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected to client: {addr[0]}:{addr[1]}")

        data = conn.recv(1024).decode('utf-8')
        print("Received data:", data)

        response = "Server received your message: " + data
        conn.sendall(response.encode('utf-8'))

        conn.close()

# Example usage
host = '192.168.1.74'  # Change to desired host IP or hostname
port = 12345  # Change to desired port number
start_server(host, port)
