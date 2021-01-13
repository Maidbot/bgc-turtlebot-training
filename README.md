# bgc-turtlebot-training
BGC course for training a turtlebot to go a custom route.

http://wiki.ros.org/turtlesim/Tutorials/Go%20to%20Goal


launch Gazebo_Playground from desktop

Run command in terminal session: roslaunch turtlebot_navigation amcl_demo.launch map_file:=/opt/ros/indigo/share/turtlebot_gazebo/maps/playground.yaml


Open separate terminal session and open rviz and load config file.

teleop if running will prevent nav.

rostopic pub /cmd_vel_mux/input/navi geometry_msgs/Twist "linear: x y z angular: x y z" -r 1 


#####################
# DEFINITIONS:
## linear speed:
### backwards -1
### stop: 0
### forwards: 1
#####################
## rotational speed
### left: -1
### center: 0
### right: 1
####################
## duration
### duration in seconds: 0 - 10
###################
# FORMAT: linear speed | rotational speed | duration
# EXAMPLE
# 
{
  "testPattern": [
    [0,-1,1],
    [1,0,10],
    [0,1,1],
    [1,0,10]
  ],
  "yourPattern": [
    
  ]
}

`git clone https://github.com/Maidbot/bgc-turtlebot-training.git`
