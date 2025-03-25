#! /usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
def callback(msg):
    print(msg) #This will print the whole Odometry message
    # print(msg.header) #This will print the header section of the Odometry message
    # print(msg.pose) # #This will print the pose section of the Odometry message
rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()