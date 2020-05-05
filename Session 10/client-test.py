from Client0 import *

ip = "192.168.1.45"
port = 8080

c = Client(ip, port)

for i in range(5):
    c.debug_talk((f"Message: {i}"))
