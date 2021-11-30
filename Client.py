from socket import *
import time
import datetime

serverSocket = socket(AF_INET, SOCK_DGRAM)

# Define address of other socket
address = ("127.0.0.1", 12000)

# Send 10 pings to server
for i in range(10):
  message = f"Ping {i+1} {datetime.datetime.now().time()}";
  serverSocket.sendto(message.encode(), address)

  serverSocket.settimeout(1);
  timeSent = datetime.datetime.now();

  try:
    response = serverSocket.recvfrom(1024)
    roundtrip = (datetime.datetime.now() - timeSent).total_seconds()
    print(f"{response[0].decode()} | roundtrip: {roundtrip} seconds")
  except error:
    print(f"Request {i+1} timed out")
