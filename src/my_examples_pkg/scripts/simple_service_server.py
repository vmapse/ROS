#! /usr/bin/env python3

import rospy
from std_srvs.srv import Empty, EmptyResponse

def my_callback(request):
    print ("My_callback has benn called")
    return EmptyResponse()

rospy.init_node('service_server')
my_service = rospy.Service('/my_service', Empty, my_callback)
rospy.spin()