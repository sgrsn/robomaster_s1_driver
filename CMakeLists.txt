cmake_minimum_required(VERSION 3.0.2)
project(robomaster_s1_driver)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
)

catkin_python_setup()
catkin_package()

catkin_install_python(PROGRAMS
  nodes/robomaster_node
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
