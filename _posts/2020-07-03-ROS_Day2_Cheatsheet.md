---
layout: post
title: ROS Day 2 Cheatsheet (Node Communication)
---

รวมคำสั่งต่างๆที่ใช้ในการอบรม ROS วันที่ 2


## Example sourcecode
``` python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

vel = Twist()

def main ():
    rospy.init_node('turtle_commander', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    
    while not rospy.is_shutdown():
        # TODO
        print("Turtle is running.")

        # END
        pub.publish(vel)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        main ()
    except rospy.ROSInterruptException:
        pass
```

## Example sourcecode for assignment 
``` python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

vel = Twist()  # Variable Twist

def main ():
    rospy.init_node('turtle_commander', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    
    timestart = time.time()
    while not rospy.is_shutdown():
        timenow = time.time()
        counter = timenow - timestart
        # TODO
        print("Turtle is running.", counter)
        
        if (counter >0 and counter <= 2):
            vel.linear.x = 1
        elif (counter >2 and counter <= 5):
            vel.linear.x = 0
            vel.angular.z = 1
        else:
            vel.linear.x = 0
            vel.angular.z = 0
            break

        # END
        pub.publish(vel)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        main ()
    except rospy.ROSInterruptException:
        pass
```


## Example sourcecode for Publish and Subscrib assignment 
```
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose      # Import Pose object
import time

pos = Pose()   # Assign and set default
vel = Twist()  # Variable Twist

def position_callback(data):
    """Active when recevie info from topic"""
    global pos  # using global keyword to edit variable outside function
    pos = data

def main ():
    rospy.init_node('turtle_commander', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, position_callback)
    
    timestart = time.time()
    state = 0
    while not rospy.is_shutdown():
        timenow = time.time()
        counter = timenow - timestart
        # TODO
        print("Turtle is running.", state, pos)

        PI = 22.0/7.0
        if state == 0 and pos.x < 10:    # state 0 move to x = 10
            vel.linear.x = 1
        elif state == 0 and pos.x >= 10:
            vel.linear.x = 0
            state = 1
            
        elif state == 1 and pos.theta < PI/2: # state 1 rotate
            vel.angular.z = 1
        elif state == 1 and pos.theta >= PI/2:
            vel.angular.z = 0
            state = 2

        elif state == 2 and pos.y < 10:    # state 2
            vel.linear.x = 1
        elif state == 2 and pos.y >= 10:
            vel.linear.x = 0
            state = 3
        else:
            vel.linear.x = 0
            vel.angular.z = 0
            
        # END
        pub.publish(vel)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        main ()
    except rospy.ROSInterruptException:
        pass
```
