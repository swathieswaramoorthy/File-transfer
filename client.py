import socket
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = '127.0.0.1'
server_port = 12345

client_socket.connect((server_address, server_port))

filename = 'sample.txt'  

client_socket.send(filename.encode())

with open(filename, 'rb') as f:
   
    bytes_read = f.read(1024)
    while bytes_read:
        client_socket.send(bytes_read)
        bytes_read = f.read(1024)

print(f"File {filename} sent successfully.")


client_socket.close()
