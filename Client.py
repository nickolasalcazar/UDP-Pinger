from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

# Send 10 pings to server

# Send the ping message using UDP

# If server responds,
#	Print the response message from server
# 	Print the round trip time (RTT) in seconds

# Else print "Request timed out"
# Client waits 1 sec for a reply before assuming packet loss





# Send message to UDP Pinger Server
# Define address of other socket
address = ("127.0.0.1", 12000)

message = "Working 123".encode()

serverSocket.sendto(message, address)

# Receive response
response  = serverSocket.recvfrom(1024)
print(response[0].decode())
