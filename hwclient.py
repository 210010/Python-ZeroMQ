#
# Hello world client
# connects REQ socket to tcp://localhost:555
# sends "Hello" to server excepts "world" back
#

import zmq
import time

context = zmq.Context()

# socket to talk to server
print("Connecting to hello world server...")
sock = context.socket(zmq.REQ)
sock.connect("tcp://localhost:5555")

# do 10 request and waiting each time for a response

for request in range(10):
    print("Sending request %s ... " % request)
    sock.send(b"Hello")

    # get the reply
    message = sock.recv()
    print("Received reply %s [%s]" % (request, message))
