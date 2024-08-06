# CS-361-Asignment-7

Client requests data from socket.send_string(num_string). REQ is a method that is a socket type within the zmq methods of constant.py. This allows the socket to be created to send that string. num_string is generated as a random number (a placeholder for the actual data from the program, so that I could test any random decimal number would convert correctly to the proper letter grade.

Server calls data from client by socket.recv(). There is a float attached to it so that the logic can interpret 'grade' as a number when assigning a letter grade. It then sends the new letter grade as a string back to client, which has its own socket.recv() to print out the new letter grade.

Both files have a send_string and recv to exchange the information.

This can be adjusted for a series of grades sent/received with a for loop. Will implement if necessary for the program.

<img width="517" alt="image" src="https://github.com/user-attachments/assets/ebcb1a89-1f04-4e33-b2a8-59c0338fd8c3">
