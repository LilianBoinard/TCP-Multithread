import socket
import os
from _thread import *
from colorama import init, Fore
init()


IP = "127.0.0.1"
PORT = 1233
threadCount = 0

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
print("type: Server")
print("\n")
print(Fore.WHITE)

def separator():
    print("--------------------------------------------------------->")

Server = socket.socket()

try:
    Server.bind((IP, PORT))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection...')
separator()
Server.listen(1)

def threaded_client(thread):
    threadCountTest = threadCount
    threadName = thread.recv(2048)
    threadName = threadName.decode('utf-8')
    thread.send(str.encode('Welcome to the Emma Server ' + threadName + ' !\n'))
    separator()
    try:
        while True:

            data = thread.recv(2048)
            serverReceive = str(threadName) + ": " + data.decode('utf-8')
            reply = 'Server received of ' + serverReceive
            print(serverReceive)
            separator()
            if not data:
                break
            thread.sendall(str.encode(reply))
    except:
        print(Fore.RED + "A connection has been lost with " + str(threadName) + Fore.WHITE)
        separator()
    thread.close()
    
while True:
    Client, address = Server.accept()
    print('Connection of Address: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    threadCount += 1
    print('Thread Number: ' + str(threadCount))
    # command = input("test") # A CONTINUER
Server.close()
