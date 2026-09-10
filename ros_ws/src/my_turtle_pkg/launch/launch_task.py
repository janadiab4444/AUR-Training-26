import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('my_turtle_pkg'),
        'config',
        'params.yaml'
    )

    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        Node(
            package='my_turtle_pkg',
            executable='go_to_goal_node',
            name='go_to_goal',
            parameters=[config]
        ),
        Node(
            package='my_turtle_pkg',
            executable='delayed_client_node', 
            name='delayed_client'
        )
    ])