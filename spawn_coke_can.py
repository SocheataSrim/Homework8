import os

from gazebo_msgs.srv import SpawnEntity
import rospy  # Import rospy

def spawn_coke_can():
  rospy.init_node('spawn_coke_can')  # Added this line
  spawn_client = rospy.ServiceProxy('/gazebo/spawn_entity', SpawnEntity)

  # Replace with the path to your coke_can.sdf file
  coke_can_sdf_path = "/home/roeunsea/my_robot/coke_can.sdf"  # Update this line!

  with open(coke_can_sdf_path, "r") as f:
    coke_can_sdf = f.read()

  spawn_client('coke_can', coke_can_sdf, '', '', '')  # Replace with your model name and path

if __name__ == '__main__':
  spawn_coke_can()
  rospy.spin()

