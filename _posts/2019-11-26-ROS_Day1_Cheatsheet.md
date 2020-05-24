---
layout: post
title: ROS Day 1 Cheatsheet (Workspace & Package)
---

รวมคำสั่งต่างๆที่ใช้ในการอบรม ROS วันที่ 1


การสร้าง Workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws && catkin_make
```


การสร้าง package
```
cd ~/catkin_ws/src
catkin_create_pkg my_turtlesim std_msgs rospy roscpp
cd ~/catkin_ws && catkin_make
```


