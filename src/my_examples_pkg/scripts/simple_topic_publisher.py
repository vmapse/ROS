#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('cmd_publisher')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)

var = Twist()
var.linear.x = 0.5
var.angular.z = 0.3

while not rospy.is_shutdown():
    pub.publish(var) 
    rate.sleep()      
