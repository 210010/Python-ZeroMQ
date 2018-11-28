import zmq
import time

# Hello world server
# Binds REP socket to tcp://*:5555
# Except "Hello" from the client and repy "world"

context = zmq.Context()

# socket to talk to clients
sock = context.socket(zmq.REP)
sock.bind("tcp://*:5555")

while True:
    # wait for next message from client
    message = sock.recv()
    print("Received Request: %s" % message)

    # do some work
    time.sleep(1)

    # Reply
    sock.send(b"world")
