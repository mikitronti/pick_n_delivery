import socket
import numpy
import math
import time
from getpass import getpass


class Utente:
	def __init__(self,nome,pw,x,y,theta):
		self.nome = nome
		self.pw = pw
		self.x = x
		self.y = y
		self.theta = theta
		
		
DEBUG = 1		
PRONTO = "PRONTO"
DISCONNECT_MSG = "DISCONNECT"
HEADER = 64
FORMAT = 'utf-8'
PORT = 9200
SERVER="192.168.1.103"
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
DEST_TIMEOUT = 20 
rif = 0

l=[]
l.append(Utente("PIPPO","ciao",45.0120201111,12.4125871658,1.8))
l.append(Utente("Pluto","mortazza",45.0120201111,12.25,1.8))
l.append(Utente("Pap","yes",32.3018074036,13.5620994568,-0.00534057617188))
l.append(Utente("Minni","top",15.6076612473,14.2355070114,-0.00143432617188))
l.append(Utente("Johnny","madoka",10.0647125244,34.1583137512,-0.00527954101562))
l.append(Utente("amuro","0079",12.5790786743,37.7326850891,37.7326850891))
l.append(Utente("hikaru","macuross",70.1204452515,13.9678087234,-0.00143432617188))
l.append(Utente("Ocelot","metal",87.5139846802,9.73321342468,-0.00143432617188))
l.append(Utente("Solid","snake",99.6203689575,19.0595703125,-0.00143432617188))
l.append(Utente("AI","video",88.5164108276,37.5436820984,-0.00143432617188))



def checkUser():
	a = 0
	user=""
	while(a == 0):
		user=str(input("inserisci il tuo nome:\n"))
		
		print("inserisci la tua password:\n")
		pw = getpass() 
		for elem in l:
			if elem.nome == user and elem.pw == pw:
				user=Utente(elem.nome,elem.pw,elem.x,elem.y,elem.theta)
				a = 1
		if a == 0:
			print("i dati inseriti non sono corretti\n")
	print("ok\n")
	return user

def send(msg):
	message=msg.encode(FORMAT)
	client.send(message)

def invioPacco(user):
	print("Caricare un pacco sul robot\n")
	print("Potete inviare un pacco ai seguenti utenti registrati\n")
	for elem in l:
		if elem.nome != user.nome:
			print(elem.nome+"\n")
	b = 0
	target=""
	while b != 1:
		target=str(input("A chi desiderate mandare il pacco?\n"))
		for elem in l:
			if target == elem.nome and target != user.nome:
				b = 1
		if b == 0:
			print("Inserire un destinatario valido\n")
				
	msg=""
	for elem in l:
		if elem.nome == target:
			msg="dest,"+str(elem.x)+","+str(elem.y)+","+str(elem.theta)
	if DEBUG == 1:
		print(msg)
	send(msg)
	msg=client.recv(256).decode(FORMAT)
	if DEBUG == 1:
		print(msg)
	print("l'invio del pacco e' in corso\n")
	
def chiamaRobot(user):
	print("Attendere prego, Il robopostino sta venendo da voi\n")
	s="mitt,"+str(user.x)+","+str(user.y)+","+str(user.theta)
	if DEBUG == 1:
		print(s)
	send(s)

	
	
	
def main():
	print("Pick n delivery ver 1.0\n")
	print("Autore: \n Michelangelo\n Tronti\n 1839626\n")
	
	user=checkUser()
	b = 0
	while b != 1:
		r=input("Desiderate mandare un pacco? [s/n]\n")
		if str(r) == "s" or str(r) == "S":
			b = 1
			chiamaRobot(user)
		
		elif str(r) == "n" or str(r) == "N" :
		
			print("Chiusura in corso, grazie per aver usato il nostro programma\n")
			print("Arrivederci!\n")
		
			send(DISCONNECT_MSG)
		
			return
		
		else:
			print("inserire un input valido")
	
	while(True):
		msg=client.recv(256).decode(FORMAT).strip()
		if(msg):
			if msg == "PRONTO":
				
				invioPacco(user)
				
			elif msg == "DEST":
				print("Arrivato")
				
				while 1:
					
					resp = input("Che operazione intendete eseguire adesso?\n	 1: Inviare un altro pacco\n	 2: Uscire\n")
					
					if resp == "1":
						print("Attendere il tempo affinche' il precedente destinatario prenda il suo pacco")				
						time.sleep(DEST_TIMEOUT)
						chiamaRobot(user)
						break
					
					elif resp == "2":
						print("Chiusura in corso, grazie per aver usato il nostro programma\n")
						print("Arrivederci!\n")
						send(DISCONNECT_MSG)
						return
						
					
				
					
			elif msg == "ok":
				
				rif = 0
				
				if DEBUG != 0:
					print("rif ="+str(rif))
				
			elif msg == "NO":
				print("Al momento il robopostino non e' diponibile, attendere prego")
				
				rif = 1
				if DEBUG != 0:
					print("rif ="+str(rif))
				
				time.sleep(10)
				chiamaRobot(user)
			
			else:
				
				if DEBUG != 0:
					print(msg)
					print("rif ="+str(rif))
				
				if rif == 0:
				
					a="ok"
				
					if DEBUG != 0:
						print(a)
				
					send(a)
		
	return


main()
