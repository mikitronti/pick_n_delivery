#!/usr/bin/env python
import time
import rospy
import math
from pick_n_delivery.msg import NewGoal
from std_msgs.msg import String, Float32
import numpy
from geometry_msgs.msg import TransformStamped, PoseStamped
import tf2_ros
from tf2_msgs.msg import TFMessage

class params:
	pubblicato = 0
	nav = 0
	seq = 0

DEBUG = 0
ARRIVATO = "Arrivato"
BLOCCATO = "Bloccato"

new_goal_msg = PoseStamped();

cur_pos = numpy.empty(2,float)
tar_pos = numpy.empty(2,float)
old_pos = numpy.empty(2,float)

def position_callback(tf):												#il nodo aggiorna la posizione del robot
	tok=tfBuffer.can_transform("map","base_link",rospy.Time(0))
	if tok != 0:
		tst= TransformStamped()
		tst=tfBuffer.lookup_transform("map","base_link",rospy.Time(0))
		old_pos[0] = cur_pos[0]
		old_pos[1] = cur_pos[1]
		cur_pos[0] = tst.transform.translation.x
		cur_pos[1] = tst.transform.translation.y
		if DEBUG == 1:
			print("posizione aggiornata\n")
		
		
def move_to_goal_callback(new_goal):									#la funzione aggiorna la destinazione del robot
	
	rospy.loginfo("Mi muovo")
	
	new_goal_msg.header.seq = p.seq
	p.seq+=1
	new_goal_msg.header.stamp = rospy.Time.now()
	new_goal_msg.header.frame_id = "/map"
	
	new_goal_msg.pose.position.x = new_goal.x
	new_goal_msg.pose.position.y = new_goal.y
	new_goal_msg.pose.position.z = 0
	
	new_goal_msg.pose.orientation.x = 0
	new_goal_msg.pose.orientation.y = 0
	new_goal_msg.pose.orientation.z = 0
	new_goal_msg.pose.orientation.w = new_goal.theta
	
	p.nav = 1
	p.pubblicato = 1
	
	tar_pos[0] = new_goal_msg.pose.position.x
	tar_pos[1] = new_goal_msg.pose.position.y
	
	
		
		
def timer1_callback(event= None):										#la funzione controlla se il robot e' arrivato alla destinazione
	if DEBUG == 1:
		print(str(p.nav)+"sono il check dell'arrivo\n")
	if p.nav != 0:
		if math.sqrt( math.pow(cur_pos[0] - tar_pos[0],2) + math.pow(cur_pos[1] - tar_pos[1],2)) < 1.2 :
			rospy.loginfo("Sono arrivato a destinazione !!!")
			pub_arr.publish(ARRIVATO)
			p.nav = 0
			

def timer2_callback(event= None ):										#la funzione controlla euristicamente se il robot si e' bloccato
	if DEBUG == 1:
		print(str(p.nav)+"sono il check del blocco\n")
	if p.nav != 0:
		#if math.sqrt( math.pow(cur_pos[0] - old_pos[0],2) + math.pow(cur_pos[1] - old_pos[1],2)) < 0.5:
		pos1 = cur_pos[0]
		time.sleep(0.5)
		pos2 = cur_pos[0]
		if pos1 == pos2:
			rospy.loginfo("MI sono bloccato !!!")
			pub_arr.publish(BLOCCATO)
			p.nav = 0
		
if __name__ == "__main__":

	
	try:
		p=params()
		rospy.init_node("set_goal", anonymous=True) 
		tfBuffer = tf2_ros.Buffer();
		listen = tf2_ros.TransformListener(tfBuffer);
		rate = rospy.Rate(10)
		
		pub = rospy.Publisher("/move_base_simple/goal",PoseStamped,queue_size=10)	#pubblicazione topic
		pub_arr = rospy.Publisher("/Arrived",String,queue_size=10)
		
		sub = rospy.Subscriber("New_Goal",NewGoal,move_to_goal_callback)			#sottoscrizione topic
		sub_tf = rospy.Subscriber("/tf",TFMessage,position_callback)
		
		timer1 = rospy.Timer(rospy.Duration(0.5),timer1_callback)					#check periodici della posizione
		timer2 = rospy.Timer(rospy.Duration(50),timer2_callback)
		
		print(str(p.pubblicato))
		print(str(p.nav))
		
		while not rospy.is_shutdown():
			if p.pubblicato!=0:
				print("mando il messaggio \n")
				pub.publish(new_goal_msg)
				p.pubblicato = 0
			rate.sleep()
			
	except rospy.ROSInterruptException:
		pass
