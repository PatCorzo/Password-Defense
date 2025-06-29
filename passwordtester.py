import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def start_server():
    # Create socket object using IPv4 and TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            print(f"Server is listening on {HOST}:{PORT}...")
            
            conn, addr = s.accept()  # Wait for a client to connect
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)  # Receive data
                    if not data:
                        break
                    print(f"Received from client: {data.decode()}")
                    conn.sendall(data)  # Echo back the data
        except Exception as e:
            print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()


