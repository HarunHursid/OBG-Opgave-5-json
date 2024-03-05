import socket
import threading
import json
from random import randint

def handle_client(connection_socket, address):
    print(f"Handling connection from {address}")
    while True:
        data = connection_socket.recv(1024).decode()
        if not data:
            break
        try:
            data = json.loads(data)
            response = switch_case(data)
            connection_socket.send(json.dumps(response).encode())
        except json.JSONDecodeError:
            connection_socket.send(json.dumps({"error": "Invalid JSON"}).encode())
    

def switch_case(data):
    method = data.get("method", "").lower()
    if method == "random":
        num1 = data.get("num1")
        num2 = data.get("num2")
        random_num = randint(min(num1, num2), max(num1, num2))
        return {"Random number between first and second number": random_num}
    elif method == "add":
        num1 = data.get("num1")
        num2 = data.get("num2")
        add_num = num1 + num2
        return {"first + second number": add_num}
    elif method == "subtract":
        num1 = data.get("num1")
        num2 = data.get("num2")
        sub_num = num1 - num2
        return {"first - second number": sub_num}
    else:
        return {"error": "Invalid method"}

def start_server():
    server_port = 12000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(5)
    print('Server is ready to listen')
    while True:
        connection_socket, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(connection_socket, addr)).start()

if __name__ == "__main__":
        start_server()


