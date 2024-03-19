import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {client_address}: {data.decode()}")
        client_socket.send(data)
    
    print(f"Connection from {client_address} closed.")
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()