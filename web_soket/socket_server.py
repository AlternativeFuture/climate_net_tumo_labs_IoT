import socket
import threading as thread


def send_message():
    while True:
        message = input("You: ")
        client_socket.send(message.encode())


def res_message():
    while True:
        try:
            received_message = client_socket.recv(1024).decode()
            print(f"Client: {received_message}")
        except TimeoutError:
            continue


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'

port = 5000
server_socket.bind((host, port))

server_socket.listen()

print(f"Server listening on {host}:{port}")
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")


client_socket.settimeout(0.2)


t1 = thread.Thread(target=send_message)

t2 = thread.Thread(target=res_message)

t1.start()
t2.start()

t1.join()
t2.join()

client_socket.close()
server_socket.close()
