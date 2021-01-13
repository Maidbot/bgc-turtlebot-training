#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import json 

class TurtleBot:
    def __init__(self):
        rospy.init_node('turtlebot_bgc_planner', anonymous=True)
        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/cmd_vel_mux/input/navi',
                                                  Twist, queue_size=10)
        self.rate = rospy.Rate(20)
        self.your_pattern = {}

    def movement_message(self, lin_x = 0, ang_z = 0):
        """Formats the movement messages."""
        msg = Twist()
        msg.linear.x = lin_x
        msg.linear.y = 0
        msg.linear.z = 0
        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = ang_z
        return msg
        
    def handle_movement(self, input_data):
        """Handles publishing velocity messages from the input given."""
        linear = input_data[0]
        rotational = input_data[1]
        duration = rospy.Duration(input_data[2])
        end_time = rospy.Time.now() + duration
        while rospy.Time.now() < end_time:
            adjusted_rotational = rotational / 2
            msg = self.movement_message(linear, adjusted_rotational)
            self.velocity_publisher.publish(msg)
            # Publish at the desired rate.
            self.rate.sleep()

    def pause_between_movement(self):
        """Pauses the robot for a second to allow for it to move stably."""
        msg = self.movement_message()
        self.velocity_publisher.publish(msg)
        rospy.sleep(1)

    def navigate(self):
        """Moves the turtle to the goal."""
        with open('directions.json') as directions: 
            self.your_pattern = json.load(directions)

        # Sleeping to allow for the get_rostime to return a proper value. 
        rospy.sleep(1)
        
        # replace yourPattern with testPattern to see an example.
        for input_data in self.your_pattern['yourPattern']: 
            self.handle_movement(input_data)
            self.pause_between_movement()

if __name__ == '__main__':
    try:
        tb = TurtleBot()
        tb.navigate()
    except rospy.ROSInterruptException:
        pass
