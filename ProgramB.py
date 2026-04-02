import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and a port
host = '127.0.0.1'
port = 5200
server_socket.bind((host, port))
server_socket.listen(1)
print("Program B is listening")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024).decode()
#convert string
upper_data = data.upper()

print("New sentence:", upper_data)
conn.send(upper_data.encode())

conn.close()
server_socket.close()