import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8888")
grade = float(socket.recv())

print(f"Numerical Grade = {grade}")

if grade >= 93:
    letter_grade = "A"
elif grade >= 90 and grade < 93:
    letter_grade = "A-"
elif grade >= 87 and grade < 90:
    letter_grade = "B+"
elif grade >= 83 and grade < 87:
    letter_grade = "B"
elif grade >= 80 and grade < 83:
    letter_grade = "B-"
elif grade >= 77 and grade < 80:
    letter_grade = "C+"
elif grade >= 73 and grade < 77:
    letter_grade = "C"
elif grade >= 70 and grade < 73:
    letter_grade = "C-"
elif grade >= 67 and grade < 70:
    letter_grade = "D+"
elif grade >= 63 and grade < 67:
    letter_grade = "D"
elif grade >= 60 and grade < 63:
    letter_grade = "D-"
else:
    letter_grade = "F"

socket.send_string(letter_grade)

context.destroy()