from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='g1_control_pkg',
            executable='g1_low_level_node',
            output='screen'),
    ])