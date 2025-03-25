#! /usr/bin/env python3

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("Request Data==> duration="+str(request.duration))
    my_response = MyCustomServiceMessageResponse()
    if request.duration > 0.0:
        my_response.success = True
        i = 0
        while i < request.duration:
            vel.linear.x = 0.5
            vel.angular.z = 0.5
            pub.publish(vel)
            rate.sleep()
            i += 1
            print (i)

    else:
        my_response.success = False
    
    vel.linear.x = 0.0
    vel.angular.z = 0.0
    pub.publish(vel)

    return my_response

rospy.init_node('service_server')
my_service = rospy.Service('/move_turtlebot_in_circle_custom', MyCustomServiceMessage, my_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rate = rospy.Rate(1)
rospy.spin()
