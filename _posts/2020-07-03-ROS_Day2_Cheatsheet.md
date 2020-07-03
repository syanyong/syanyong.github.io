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


