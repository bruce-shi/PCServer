__author__ = 'bruce'
import zmq
import time
context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind ("tcp://*:7788")
while True:
    try:
        client_id = socket.recv()
        print client_id + "come in"
        time.sleep(10)
        res = 'client : ' + client_id + "finished"
        socket.send(res)
        print res
    except KeyboardInterrupt:
        break
print("Server Exit")