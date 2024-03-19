import socket

def main():
    host = '127.0.0.1'
    port = 12345
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
        
    except KeyboardInterrupt:
        print("Client stopped.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
