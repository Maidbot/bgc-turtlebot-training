# bgc-turtlebot-training
BGC course for commanding a turtlebot to follow movement patterns.

<br />

## Steps
Make sure you open up your virtual machine (like the pre-workshop slides help you set up!)

1. Open a terminal session by double-clicking on the `terminal` icon on the desktop.
1. Make sure you're in the home folder by entering `cd ~` (change directory).
1. Download the workship code by entering `git clone https://github.com/Maidbot/bgc-turtlebot-training.git`
1. Navigate into downloaded code by entering `cd bgc-turtlebot-training`.
1. On the desktop, double-click the `Gazebo Playground` to launch the simulator.
1. To run the workshop code, enter `python main.py`. You should see the robot move!
1. You can edit your pattern by entring `kate directions.json`. **Don't forget to save your changes!**  
<br/>

-------------
# Commands
You can give your robot commands by editing the `directions.json` file. Commands look like this:

```
[DRIVE, ROTATE, DURATION]
```

### Driving Speed
`DRIVE` is one of three values representing backwards, stopped and forwards:

```
backwards: -1
stop: 0
forwards: 1
```

### Rotation Speed
`ROTATE` is one of three values representing rotating to the left, moving straight, or rotating to the right:
```
left:   1
center: 0
right: -1
```

### Duration
`DURATION` is how long the command should last (in seconds). Try to keep it under `10`!

<br/>

## Example 
There's an example in the `directions.json` file you can use. 

Here's an explanation of what each line means (everything after the `#` is a _comment_, not real code):

```js
{  # This is the start of the file

  "testPattern": # This is the name of a pattern your robot will follow
  [ 
    [0, -1,  1],    # This means "rotate right for 1 second"
    [1,  0, 10],    # This means "drive forwards for 10 seconds"
    [0,  1,  1],    # This means "rotate left for 1 second"
    [1,  1,  2.5]   # This means "drive forwards while rotating to the left for 2.5 seconds"
                    # Make sure the last command does not have a comma (",") at the end! 
  ], 
  
  "myPattern": # This is the name of a pattern your robot will follow
  [  # This is the start of the commands for myPattern
  # Enter your commands here!
  ], # This is the end of the commands for myPattern

}  # This is the end of the file
```

# Frequently Asked Questions

## How do I make my text bigger? I can't see it!
You can hit `ctrl` and `+` at the same time.

## Can I copy/paste into the virtual machines?
Sometimes yes, but it depends on your system. You might not be able to.
