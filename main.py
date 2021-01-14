#!/usr/bin/env python
import sys
import json

import rospy
from geometry_msgs.msg import Twist

class TurtleBot:
    def __init__(self):
        rospy.init_node('turtlebot_bgc_planner', anonymous=True)

        # Publisher will publish messages to control the velocity of the robot
        self.velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi',
                                                  Twist, queue_size=10)
        self.rate = rospy.Rate(20)

    def movement_message(self, lin_x = 0, ang_z = 0):
        """Formats the movement messages."""
        msg = Twist()
        msg.linear.x = lin_x
        msg.angular.z = ang_z
        return msg
        
    def handle_movement(self, input_data):
        """Handles publishing velocity messages from the input given."""
        # Get the command input
        linear = input_data[0]
        rotational = input_data[1]
        duration = rospy.Duration(input_data[2])

        # Convert into a ROS message (with proper units)
        adjusted_rotation_speed = rotational / 2  # convert to radians / second
        msg = self.movement_message(linear, adjusted_rotation_speed)
        
        # Publish the message until the duration has elapsed
        end_time = rospy.Time.now() + duration
        while rospy.Time.now() < end_time:
            self.velocity_publisher.publish(msg)
            self.rate.sleep()

    def pause_between_movement(self):
        """Pauses the robot for a second to allow for it to move stably."""
        msg = self.movement_message()
        self.velocity_publisher.publish(msg)
        rospy.sleep(1)

    def navigate(self, pattern_name):
        """Moves the turtle to the goal."""
        with open('directions.json') as directions: 
            patterns = json.load(directions)

        # Making sure the pattern exists
        if pattern_name not in patterns:
            raise ValueError("Pattern {} does not exist!".format(pattern_name))

        # Sleeping to allow for the get_rostime to return a proper value. 
        rospy.sleep(1)
        
        # replace yourPattern with testPattern to see an example.
        for input_data in patterns[pattern_name]: 
            self.handle_movement(input_data)
            self.pause_between_movement()

if __name__ == '__main__':
    try:
        pattern_name = sys.argv[1]
    except:
        pattern_name = "squarePattern"  # Default pattern to run

    try:
        tb = TurtleBot()
        tb.navigate(pattern_name)
    except rospy.ROSInterruptException:
        pass
