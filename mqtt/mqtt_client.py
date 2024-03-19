import time
import warnings
import paho.mqtt.client as mqtt

local_host = False

if local_host:
    broker_address = 'localhost'
else:
    broker_address = '54.234.125.32'

broker_port = 1883


def connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'Connected to broker \n    Host: {broker_address} Port: {broker_port}')
    else:
        print('Failed to connect to broker')

    client.subscribe('Chat/Python')


def message(client, userdata, msg):
    sender_name, mess = msg.payload.decode().split(':', 1)
    if mess.strip() == 'left the chat':
        print(f'{sender_name.strip()} left the chat')
    else:
        print(f'{sender_name.strip()}: {mess.strip()}')


warnings.filterwarnings('ignore', category=DeprecationWarning)
client_paho = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

client_paho.on_connect = connect
client_paho.on_message = message

client_paho.connect(broker_address, broker_port, 60)

client_paho.loop_start()
time.sleep(0.5)

print('If you want to left the chat, type exit')
username = input('Enter your name: ')

try:
    while True:
        message = input('Enter message:')
        if message.lower() == 'exit':
            client_paho.publish('Chat/Python', f'{username}: left the chat')
            time.sleep(1)
            break
        client_paho.publish('Chat/Python', f'{username}: {message}')
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
