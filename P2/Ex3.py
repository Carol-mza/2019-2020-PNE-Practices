from Client0 import Client

print("-----| Practice 2, Exercise 3 |-----")

ip = "192.168.1.45"
port = 8080

c = Client(ip, port)

print("Send message to the server: ")
response = c.talk("Testing!")
print(f"Response: {response}")