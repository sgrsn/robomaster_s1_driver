#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from robomaster_s1_driver.rm_py_hack.lib import rm_s1_hacker
import threading
import time

class robomaster():
    def __init__(self):
        self.hacker = rm_s1_hacker.RoboMasterHacker()
        self.vx = 0
        self.vy = 0
        self.rz = 0
        threading.Thread(target = self.can_loop, daemon = True).start()

    def can_loop(self):
        start_time = time.time()
        send_interval = 0.01
        while True:
            self.hacker.receive_msg()
            if time.time() - start_time > send_interval:
                self.hacker.send_touch_command()
                self.hacker.twist_robomaster(self.vx, self.vy, self.rz)                
                start_time = time.time()
        
my_rm = robomaster()

def joy_callback(twist):
    my_rm.vx = twist.linear.x
    my_rm.vy = twist.linear.y
    my_rm.rz = twist.angular.z
    
def main():
    rospy.init_node('robomaster', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, joy_callback)
    rospy.spin()
        
if __name__ == '__main__':
    main()