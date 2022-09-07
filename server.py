#!/usr/bin/python3         

import socket  
import os             

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',3000))
s.listen(7)

while True:  
    
	sc,addr = s.accept()
	print("Established Connection ...")
	#msg = s.recv(1024)
	#sc.send(msg.encode('utf-8'))
	#print(msg)
	
	while True:

		msg = input("$ ")
		msg = str(msg)
		sc.send(msg.encode('UTF-8'))
		
		
		#get = sc.recv(1024)
		#get = str(get,"UTF-8")
		#print(get)

	#print(msg)


		if msg == "close":
			s.close()
			sc.close()
			print("Closed ...")
			break

	break

# ------------------------------------------------------

#serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#serv.bind(('127.0.0.1',3000))

#serv.listen(1)

#client,addr = serv.accept()


#while True:

	#recibido = client.recv(1024)  

	#if recibido == "close":
		#break

	#print("Recibido:", recibido)
	#client.send(recibido)  
  
#print("Bye") 
  
#client.close()  
#serv.close()  

# -------------------------------------------------------

# create a socket object
#serversocket = socket.socket(
#	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
#host = socket.gethostname()                           

#port = 3000                                           

# bind to the port
#serversocket.bind((host, port))                                  

# queue up to 5 requests
#serversocket.listen(5)                                           

#while True:
   # establish a connection
   #clientsocket,addr = serversocket.accept()      

   #print("Got a connection from %s" % str(addr))
    
   #msg = 'Thank you for connecting'+ "\r\n"
   #clientsocket.send(msg.encode('ascii'))
   #clientsocket.close()




# http://mundogeek.net/archivos/2008/04/12/sockets-en-python/