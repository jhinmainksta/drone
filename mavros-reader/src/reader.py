#!/usr/bin/env python3

import rospy
from mavros_msgs.msg import State

def callback(data):
  rospy.loginfo(rospy.get_caller_id() + " armed: %s", data.armed)

def reader():
  rospy.init_node('mavros-reader')

  rospy.Subscriber("mavros/state", State, callback)

  rospy.spin()

if __name__ == '__main__':
  reader()
