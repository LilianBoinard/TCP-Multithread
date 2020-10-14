import socket
import sys 
from colorama import init, Fore
init()

IP = '127.0.0.1'
PORT = 1233

print(Fore.YELLOW + "\n")
print("----------------------------------------------------------")
print("   ▄████████   ▄▄▄▄███▄▄▄▄     ▄▄▄▄███▄▄▄▄      ▄████████ ")
print("  ███    ███ ▄██▀▀▀███▀▀▀██▄ ▄██▀▀▀███▀▀▀██▄   ███    ███ ")
print("  ███    █▀  ███   ███   ███ ███   ███   ███   ███    ███ ")
print(" ▄███▄▄▄     ███   ███   ███ ███   ███   ███   ███    ███ ")
print("▀▀███▀▀▀     ███   ███   ███ ███   ███   ███ ▀███████████ ")
print("  ███    █▄  ███   ███   ███ ███   ███   ███   ███    ███ ")
print("  ███    ███ ███   ███   ███ ███   ███   ███   ███    ███ ")
print("  ██████████  ▀█   ███   █▀   ▀█   ███   █▀    ███    █▀  ")
print("----------------------------------------------------------")
print("type: Client")
print("\n")
print(Fore.WHITE)

name = str(input("Choose your username: "))

Client = socket.socket()

print('Waiting for connection...')
try:
    Client.connect((IP, PORT))
except socket.error as e:
    print(str(e))
Client.send(name.encode('utf-8'))
Response = Client.recv(1024)
print(Fore.YELLOW)
print(Response.decode('utf-8'))
print(Fore.WHITE + '\n')

while True:
    Input = input('Say Something: ')
    Client.send(str.encode(Input))
    Response = Client.recv(1024)
    print(Response.decode('utf-8'))

Client.close()