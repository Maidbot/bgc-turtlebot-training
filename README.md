# bgc-turtlebot-training
BGC course for training a turtlebot to go a custom route.

<br />

## Steps
1. Open a terminal session and navigate with `cd ~` to the root directory.
1. Download this code to your VM by using git with: `git clone https://github.com/Maidbot/bgc-turtlebot-training.git`
1. Navigate into the `bgc-turtlebot-training` directory created in the step above with `cd ~/bgc-turtlebot-training`
1. Launch the `Gazebo Playground` on the desktop. 
1. In the open terminal type `python main.py`
1. Launch Kate to start editing these files. `kate main.py` or `kate directions.json`
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