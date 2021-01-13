# bgc-turtlebot-training
BGC course for training a turtlebot to go a custom route.

<br />

You can download this code to your VM by using: 
`git clone https://github.com/Maidbot/bgc-turtlebot-training.git`
<br/>
<br/>
<br/>

-------------
# DEFINITIONS:
## linear speed:
### backwards -1
### stop: 0
### forwards: 1


------
## rotational speed
### left: -1
### center: 0
### right: 1
-----
## duration
### duration in seconds: 0 - 10
------
## FORMAT: linear speed | rotational speed | duration

<br/>
<br/>
<br/>

# Example file to edit for directions.json
```{
  "testPattern": [
    [0,-1,1],
    [1,0,10],
    [0,1,1],
    [1,0,10]
  ],
  "yourPattern": [
    
  ]
}
```
Notes:


launch Gazebo_Playground from desktop

Run command in terminal session: roslaunch turtlebot_navigation amcl_demo.launch map_file:=/opt/ros/indigo/share/turtlebot_gazebo/maps/playground.yaml

Open separate terminal session and open rviz and load config file.

teleop if running will prevent nav.

rostopic pub /cmd_vel_mux/input/navi geometry_msgs/Twist "linear: x y z angular: x y z" -r 1 
