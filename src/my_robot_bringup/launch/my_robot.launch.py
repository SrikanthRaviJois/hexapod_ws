from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    ld = LaunchDescription()

    controller_node = Node(
            package="my_robot_controller",
            executable="controller_node",
            name="controller_node"
        )
    
    gazebo_ros = ExecuteProcess(
            cmd=['gazebo', '--verbose'],
            output='screen') 

    ld.add_action(controller_node)
    ld.add_action(gazebo_ros)
    return ld
    