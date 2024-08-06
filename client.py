import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:8888")
num_string = str(random.randint(5000, 10000)/100)
socket.send_string(num_string)
letter_grade = socket.recv()

print(f"Letter Grade = {letter_grade.decode()}")