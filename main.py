#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import pow, atan2, sqrt
import json 

class TurtleBot:
    def __init__(self):
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/teleop',
                                                  Twist, queue_size=10)
        self.rate = rospy.Rate(2)
        self.your_pattern = {}

    def navigate(self):
        """Moves the turtle to the goal."""

        with open('directions.json') as directions: 
            self.your_pattern = json.load(directions)


        for i in self.your_pattern['yourPattern']: 
            linear = i[0]
            rotational = i[1]
            duration = i[2]
            itr = 0
            while itr < duration:
                msg = {
                    'linear': {
                        'x': linear,
                        'y': 0,
                        'z': 0
                    },
                    'angular': {
                        'x': 0,
                        'y': 0,
                        'z': rotational / 2
                    }
                }
                self.velocity_publisher.publish(msg)
                # Publish at the desired rate.
                self.rate.sleep()
                itr += 1
            
        # If we press control + C, the node will stop.
        rospy.spin()

if __name__ == '__main__':
    try:
        tb = TurtleBot()
        tb.navigate()
    except rospy.ROSInterruptException:
        pass
