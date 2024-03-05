import json
from socket import *

def send_command(command, serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(command.encode())
    response = clientSocket.recv(1024).decode()
    print('From Server:', response)
    clientSocket.close()

def build_json_request(method, num1, num2):
    request = {
        "method": method,
        "num1": num1,
        "num2": num2
    }
    return json.dumps(request)

serverName = 'localhost'
serverPort = 12000

command = input("Enter command (random, add, subtract): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

json_request = build_json_request(command, num1, num2)
send_command(json_request, serverName, serverPort)