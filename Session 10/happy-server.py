import socket

port = 8080
ip = "192.168.1.45"

# Creating the listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Optional for avoiding the problem of server already in use

ls.bind((ip, port)) # Bind the socket to the ip and port

ls.listen() # Configured as listener

print("The server is configured!")

while True:
    print("Waiting for clients to connect")

    try:
        (cs, cs_ip_port) = ls.accept()

    except KeyboardInterrupt: # When the running of the code is stopped
        print("Server stopped by the user")

        ls.close()

        exit()

    else:

        print("A client has connected to the server")

        msg_bytes = cs.recv(2048)
        msg = msg_bytes.decode() # Changes to a human readable string

        print(f"Received message: {msg}")

        response = "Hello I'm the HAPPY SERVER ;)\n"
        cs.send(response.encode())

        cs.close()
