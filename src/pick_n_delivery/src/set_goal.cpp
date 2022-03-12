#include <ros/ros.h>
#include <vector>
#include <string>
#include "pick_n_delivery/NewGoal.h"
#include "geometry_msgs/PoseStamped.h"
#include "tf/tf.h"
#include "ros/ros.h"
#include "tf2_msgs/TFMessage.h"
#include <sstream>

#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/TransformStamped.h>
#include "std_msgs/String.h"
//#include <nav_msgs/Odometry.h>
//#include <sensor_msgs/LaserScan.h>
#include <tf2_msgs/TFMessage.h>

std::vector<float> tar_pos(2,0);
std::vector<float> old_pos(2,0);
std::vector<float> cur_pos(2,0);

std::string ARRIVATO = "Arrivato";
std::string BLOCCATO = "Bloccato";

std_msgs::String stat;
geometry_msgs::PoseStamped new_goal_msg;

tf2_ros::Buffer tfBuffer;

size_t n = 10;

int message_published=0;
int navigando=0;

// salva la posizione corrente del robot 

void pose_callback(const tf2_msgs::TFMessage& tf){
	int tok;
	tok= tfBuffer.canTransform("map","base_link",ros::Time(0));
	
	if(tok){
		geometry_msgs::TransformStamped tfst;
		tfst = tfBuffer.lookupTransform("map","base_link",ros::Time(0));
		cur_pos[0] = tfst.transform.translation.x;
		cur_pos[1] = tfst.transform.translation.y;
	}	
	
}

// invia una nuova posizione da raggiungere

void setgoal_callback(const pick_n_delivery::NewGoal& new_goal){
	
	new_goal_msg.header.seq = n;
	n++;
	
	new_goal_msg.header.stamp=ros::Time::now();
	new_goal_msg.header.frame_id= "/map";
	
	new_goal_msg.pose.position.x = new_goal.x;
	new_goal_msg.pose.position.y = new_goal.y;
	new_goal_msg.pose.position.z = 0;
	
	new_goal_msg.pose.orientation.x = 0;
	new_goal_msg.pose.orientation.y = 0;
	new_goal_msg.pose.orientation.z = 0;
	new_goal_msg.pose.orientation.w = new_goal.theta;
	
	message_published=1;
	navigando=1;
	tar_pos[0]= new_goal.x;
	tar_pos[1]= new_goal.y;
	
}
/*
void dist_callback(geometry_msgs::PoseStamped& posiz){
	ROS_INFO("Calcolo la distanza dalla posizione\n");
	float dist = sqrt(pow((cur_pos[0]-posiz.pose.position.x),2) + pow((cur_pos[1]-posiz.pose.position.y),2));
	pub_dist.publis(dist);
}
*/
void check1_callback(const ros::TimerEvent& event){
	if(navigando){
		ROS_INFO("Controllo se mi muovo \n");
		float dist=sqrt(pow((cur_pos[0]-old_pos[0]),2) + pow((cur_pos[1]-old_pos[1]),2));
		if(dist < 0.8){
			ROS_INFO("Sono bloccato!!!");
			stat.data = BLOCCATO;
			//pub_arr.publish(stat);
		}
		dist=sqrt(pow((cur_pos[0]-tar_pos[0]),2) + pow((cur_pos[1]-tar_pos[1]),2));
		if(dist < 1.5 ){
			ROS_INFO("Destinazione raggiunta!!!\n");
			navigando=0;
			stat.data = ARRIVATO;
			//pub_arr.publish(stat);
				
		}
			
	}
}

void check2_callback(const ros::TimerEvent& event){
	if(navigando){
		ROS_INFO("Vediamo se sta passando troppo tempo \n");
		float dist= sqrt(pow((cur_pos[0]-old_pos[0]),2) + pow((cur_pos[1]-old_pos[1]),2));
		if(dist < 0.5){
			ROS_INFO("TIMEOUT: La posizione non può essere raggiunta !!!!\n");
		}
	}
}
 

int main(int argc,char** argv){

	ros::init(argc,argv,"Set_goal");

	ros::NodeHandle n;

	ros::Publisher pub  = 	 n.advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal",1000);
	
	ros::Publisher pub_arr = n.advertise<std_msgs::String>("/Arrived",1000);
	
	//ros::Publisher pub_goal= n.advertise<std::String>("/Listener",1000);
	//ros::Publisher pub_dist= n.advertise<float>("/Distpub",1000);
	

	tf2_ros::TransformListener tflistener(tfBuffer);

	ros::Rate loop_rate(10);

	ros::Subscriber sub = n.subscribe("New_Goal",1000,setgoal_callback);
	ros::Subscriber sub_tf = n.subscribe("tf",1000,pose_callback);
	//ros::Subscriber sub_dist = m.subscribe("Distsub",dist_callback);

	ros::Timer timer1=n.createTimer(ros::Duration(0.5), check1_callback);
	ros::Timer timer2=n.createTimer(ros::Duration(50), check2_callback);  

	int c=0;
	while(ros::ok()){
		if(message_published){
			ROS_INFO("Pubblico una vuova posizione");
			pub.publish(new_goal_msg);
			message_published=0;
		}
		ros::spinOnce();
		loop_rate.sleep();
		c++;
	}
	
	return 0;
}
