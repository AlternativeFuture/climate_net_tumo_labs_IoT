import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 5000

client_socket.connect((host, port))
print(f"Connected to {host}:{port}")
client_socket.settimeout(0.2)

while True:
    try:
        received_message = client_socket.recv(1024).decode()
        print(f"Server: {received_message}")
        if received_message.lower() == 'bye':
            break
    except TimeoutError:
        continue

    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == 'bye':
        break

client_socket.close()

