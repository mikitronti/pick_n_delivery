#!/usr/bin/env python

import socket
import threading
import rospy
import _thread
from pick_n_delivery.msg import NewGoal
from std_msgs.msg import String, Float32



class params:
	to_mitt =0
	to_dest =0
	robot = 0	#flag che indica se il robot e' occupato o meno
	x = 0
	y = 0
	theta = 0
	
	
	

def checkBool(conn):		#il server controlla se il robot sta andando dal destinatario o dal mittente e invia
	if p.to_mitt != 0:		#questa info al client
		msg = "vado dal mitt"
		conn.send(msg.encode(FORMAT))
	elif p.to_dest != 0:
		msg = "vado dal dest"
		conn.send(msg.encode(FORMAT))


def arr_callback(arr_msg, conn):			#quando arriva dal topic /Arrived un messaggio se il robot e' arrivato lo comunica al client
	print("\nho ricevuto"+arr_msg.data)		#se si e' bloccato reinoltra l'ultima destinazione salvata
	if arr_msg.data == ARRIVATO:
		if p.to_mitt != 0:
			msg = "PRONTO"
			if DEBUG != 0:
				print(str(conn))
			conn.send(msg.encode(FORMAT))
			p.to_mitt = 0
			
		elif p.to_dest != 0:
			msg = "DEST"
			conn.send(msg.encode(FORMAT))
			if DEBUG != 0:
				print(str(conn))
			p.to_dest=0
			
	else :
		msg = NewGoal(p.x,p.y,p.theta)
		pub.publish(msg)
	

def client_handle(conn):

	sub = rospy.Subscriber("/Arrived",String,arr_callback,callback_args= conn)	#ogni thread si iscrive alla topic /Arrived
	a=0																#flag che indica se in questo thread il robot e' arrivato dal destinatario
	rif = 0															#flag che indica se in questo thread il robot era occupato e quindi sta servendo un altro client
	connesso = True
	while connesso:
		msg = conn.recv(256).decode(FORMAT)
		if(msg):
			data=msg.strip().split(",")
			if(len(data)>1):
				if data[0] == "mitt":							#invia il robot dal mittente
					print("a= "+str(a))
					if p.robot == 0 or a == 1: 
						p.robot = 1
						p.x=float(data[1])
						p.y=float(data[2])
						p.theta = float(data[3])
						if DEBUG != 0:
							print("x= "+data[1]+"\ny= "+data[2]+"\ntheta= "+data[3]+"\n")
						msg = "ok"
						rif = 0
						new = NewGoal(p.x,p.y,p.theta)
						pub.publish(new)
						conn.send(msg.encode(FORMAT))
						p.to_mitt=1
						if DEBUG != 0:
							print("mandato"+str(msg))
							print("robot ="+str(p.robot)) 
						a = 0
		
					else:										#se il robot e' occupato manda OCCUPATO al client
						conn.send(OCCUPATO.encode(FORMAT))
						rif = 1
				
					
				elif data[0] == "dest":							#invia il robto al destinatario
						p.x= float(data[1])
						p.y= float(data[2])
						p.theta = float(data[3])
						if DEBUG != 0:
							print("x= "+data[1]+"\ny= "+data[2]+"\ntheta= "+data[3]+"\n")
						msg="vado dal dest"
						new = NewGoal(p.x,p.y,p.theta)
						pub.publish(new)
						conn.send(msg.encode(FORMAT))
						p.to_dest=1
						if DEBUG != 0:
							print("mandato"+str(msg))
						a=1
			
			
			if msg == DISCONNECT_MSG:							#il server si disconnette dal client
				p.robot = 0
				connesso = False
	
			if rif == 0:	
				checkBool(conn)
			
	conn.close()


	
if __name__ == "__main__":
	
	DEBUG = 1
	
	ARRIVATO = "Arrivato"
	BLOCCATO = "Bloccato"
	DISCONNECT_MSG = "DISCONNECT"
	OCCUPATO = "NO"
	HEADER = 64
	FORMAT = 'utf-8'
	PORT = 9200
	#SERVER="192.168.1.103"
	SERVER = "192.168.43.186"
	server= socket.socket()
	ADDR = (SERVER,PORT)
	server.bind(ADDR)
	server.listen(5)
	p=params()
	l=[]
	rospy.init_node('server', anonymous=True)
	pub = rospy.Publisher('New_Goal', NewGoal, queue_size=10)
	rate = rospy.Rate(10)
	threadCount = 0

	while True:													#il server accetta una connessione e lancia un nuovo Thread
		conn , addr = server.accept()
		l.append(conn)
		_thread.start_new_thread(client_handle, (conn, ))
		threadCount+=1
		print(l)
		print(str(threadCount))

	
	
