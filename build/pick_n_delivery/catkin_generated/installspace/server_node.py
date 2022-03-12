#!/usr/bin/env python2
import socket
import threading
import rospy
from pick_n_delivery.msg import NewGoal

DISCONNECT_MSG = "DISCONNECT"
HEADER = 64
FORMAT = 'utf-8'
PORT = 9000
SERVER="192.168.1.103"
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR = (SERVER,PORT)
server.bind(ADDR)



def client_handle(conn,addr):
	connesso = True
	while connesso:
		msg = conn.recv(256).decode(FORMAT)
		if(msg):
			data=msg.strip().split(",")
			if(len(data)>1):
				x=float(data[0])
				y=float(data[1])
				theta = float(data[2])
				print("x= "+data[0]+"\ny= "+data[1]+"\ntheta= "+data[2]+"\n")
				msg="pippo"
				new = NewGoal(x,y,theta)
				pub.publish(new)
				conn.send(msg.encode(FORMAT))
				print("mandato"+str(msg))
			msg = conn.recv(256).decode(FORMAT)
			if msg == DISCONNECT_MSG:
				connesso = False
			
	conn.close()


	
def start():
	server.listen()
	rospy.init_node('server', anonymous=True)
	pub = rospy.Publisher('New_Goal', NewGoal, queue_size=10)
	rate = rospy.Rate(10)
	while True:
		conn , addr = server.accept()
		thread = threading.Thread(target= client_handle, args = (conn,addr))
		thread.start()
		
		
start()
