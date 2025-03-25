#! /usr/bin/env python3
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('service_client')
rospy.wait_for_service('/move_turtlebot_in_circle_custom')
turtlebot_move_service_client = rospy.ServiceProxy('/move_turtlebot_in_circle_custom', MyCustomServiceMessage)
turtlebot_move_object = MyCustomServiceMessageRequest()
turtlebot_move_object.duration = 5

result = turtlebot_move_service_client(turtlebot_move_object)
print(result)
