import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 5000

server_socket.bind((host, port))
server_socket.listen()

print(f"Server listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")
client_socket.settimeout(0.2)

while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == 'bye':
        break

    try:
        received_message = client_socket.recv(1024).decode()
        print(f"Client: {received_message}")
        if received_message.lower() == 'bye':
            break
    except TimeoutError:
        continue


client_socket.close()
server_socket.close()

