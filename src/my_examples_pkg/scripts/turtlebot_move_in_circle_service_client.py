#! /usr/bin/env python3
import rospy
from std_srvs.srv import Empty, EmptyRequest# you import the service message python classes generated from Empty.srv.
rospy.init_node('service_client')
rospy.wait_for_service('/move_turtlebot_in_circle')# Wait for the service client /move_turtlebot_in_circle to be running
turtlebot_move_service_client = rospy.ServiceProxy('/move_turtlebot_in_circle', Empty)# Create the connection to the service
turtlebot_move_object = EmptyRequest()
result = turtlebot_move_service_client(turtlebot_move_object)
print (result)