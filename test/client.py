__author__ = 'bruce'
import zmq
import os
import time
context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7788")
socket.send(str(os.getppid()))
print socket.recv_string()