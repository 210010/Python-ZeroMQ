import zmq

# zmq Context
context = zmq.Context()

# Define the socket using the "context"
sock = context.socket(zmq.SUB)  # subsribing to received messages starting with string 1

# define the subscription and messages with prefix to accept.
sock.setsockopt_string(zmq.SUBSCRIBE, "1")
sock.connect("tcp://127.0.0.1:5680")

while True:
    message = sock.recv()
    print(message)
