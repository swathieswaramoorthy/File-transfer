import socket
import os

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = '127.0.0.1'
server_port = 12345

# Connect to the server
client_socket.connect((server_address, server_port))

# Specify the file to send
filename = 'sample.txt'  # Change this to your file name

# Send the file name to the server
client_socket.send(filename.encode())

# Open the file in read-binary mode
with open(filename, 'rb') as f:
    # Read the file data in chunks
    bytes_read = f.read(1024)
    while bytes_read:
        client_socket.send(bytes_read)
        bytes_read = f.read(1024)

print(f"File {filename} sent successfully.")

# Close the socket
client_socket.close()
