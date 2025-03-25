#! /usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyResponse# you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    print ("My_callback has been called")
    vel.linear.x = 0.5
    vel.angular.z = 0.5
    pub.publish(vel)
    return EmptyResponse()

rospy.init_node('service_server')
my_service = rospy.Service('/move_turtlebot_in_circle', Empty , my_callback)# create the Service called my_service with the d

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rospy.spin()# maintain the service open.