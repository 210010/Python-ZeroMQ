import zmq
import sys

# zmq context
context = zmq.Context()


# Define the socket using the "context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# send a "message" using the socket
sock.send_string(" ".join(sys.argv[1:]))
print(sock.recv())
