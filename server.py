import zmq


# zmq context
context = zmq.Context()

# define the socket using the context
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

# Run a simple echo server
while True:
    message = sock.recv()
    sock.send_string("Echo : " + str(message))
    print("Echo: " + str(message))
