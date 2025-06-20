cmake_minimum_required(VERSION 3.5)
project(g1_control_pkg)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# include_directories(include include/common include/nlohmann )
# link_directories(src)

# Include unitree_sdk2 headers
include_directories(
  include
  include/common
  include/nlohmann 
  /opt/unitree_robotics/include
  /opt/unitree_robotics/include/ddscxx
)

# Link to unitree_sdk2 libraries
link_directories(
  /opt/unitree_robotics/lib
)



set (
  DEPENDENCY_LIST
  unitree_go
  unitree_hg
  unitree_api
  rclcpp
  std_msgs
  rosbag2_cpp
)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(unitree_go REQUIRED)
find_package(unitree_hg REQUIRED)
find_package(unitree_api REQUIRED)
find_package(rosbag2_cpp REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

add_executable(g1_low_level_node src/g1_low_level.cpp src/common/motor_crc_hg.cpp)
ament_target_dependencies(g1_low_level_node ${DEPENDENCY_LIST})


add_executable(g1_audio_client_node src/audio/g1_audio_client.cpp)
ament_target_dependencies(g1_audio_client_node ${DEPENDENCY_LIST})
target_link_libraries(g1_audio_client_node
  unitree_sdk2
  ddsc
  ddscxx
)

install(TARGETS 
  g1_low_level_node
  g1_audio_client_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
