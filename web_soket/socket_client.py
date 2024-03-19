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


start = input("If you are goring to run both scripts in on computer input 1, otherwise press 2: ")

if start == "1":
    host = "0.0.0.0"
elif start == "2":
    host = input("Enter IP address of server: ")
else:
    print("You don`t choose valid option!!!")
    exit(-1)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000

client_socket.connect((host, port))
print(f"Connected to {host}:{port}")
client_socket.settimeout(0.2)


t1 = thread.Thread(target=send_message)

t2 = thread.Thread(target=res_message)

t1.start()
t2.start()

t1.join()
t2.join()

client_socket.close()
