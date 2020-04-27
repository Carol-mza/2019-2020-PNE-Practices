import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.45"

while True:
    m = input("Message to send: ") # -- Ask the user for the message

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # -- Create the socket

    s.connect((IP, PORT)) # -- Establish the connection to the Server

    s.send(str.encode(m)) # -- Send the user message

    s.close() # -- Close the socket