from Client0 import Client

print("-----| Practice 2, Exercise 1 |-----")

ip = "192.168.1.45"
port = 8080

c = Client(ip, port)

c.ping() # It's .ping() because is a method
print(f"IP: {c.ip}, Port: {c.port}")