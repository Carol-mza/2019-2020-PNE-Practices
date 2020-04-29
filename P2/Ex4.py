from Client0 import Client

print("-----| Practice 2, Exercise 4 |-----")

ip = "192.168.1.45"
port = 8080

c = Client(ip, port)

c.debug_talk("Message 1: ---")
c.debug_talk("Message 2: Testing")