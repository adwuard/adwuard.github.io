---
title: "A Humanoid Robot, Designed From Scratch"
excerpt: "14Dofs Robot Arm"
collection: wip_projects
layout: archive
author_profile: true
date: 2025-01-01
Tags:
  - Robotics
  - Custom Keyboards
header:
  teaser: /projects/14-DOF-Robot/render/1.jpeg
  overlay_image: /images/overlays/unsplash/steve-johnson-Yyb10fO2BjQ-unsplash.jpg
  caption: "Photo credit: [**Steve Johnson @ Unsplash**](https://unsplash.com/@steve_j?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)"  
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
---

> This is currently a secret "Work In Progress Project".

## Table of Contents
- [Introduction](#introduction)
- [Objective](#objective)
- [Design and Build Process](#design-and-build-process)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Work](#future-work)
- [Conclusion](#conclusion)


## Introduction
As of 2024, the popularity of AI and robotics has increased dramatically. With my personal interest in these fields, building this project will provide a better understanding of the robotics and AI industries.

Building a robot from scratch involves a multitude of tasks and diverse fields. This might be the most ambitious project I have undertaken. The cost and the amount of engineering required make it a whole new realm of "Home DIY Projects." 
The main reason for going through the entire process is to gain a deep understanding of kinematics, dynamics, and control theory, from hardware engineering to high-level AI applications. This project will help me get a better picture of what goes into building a humanoid robot from scratch.


<img src="/images/projects/14-DOF-Robot/render/1.jpeg" style="width:50%;">


# Objective
- Design and build a complete Dual Arm robot from scratch, enjoying the engineering process.
- Ensure it is low cost, durable, and reliable for robotics research purposes.
- Make it lightweight with a good power-to-load performance ratio.
- Ensure ROS2 support.
- Weighing less than 4.5 kg and capable of handling a 2.5 kg payload on the end effector.



# Hardware Design Process
## Choosing Motors

Selecting the right motors is crucial for the robot's performance and accuracy. For this project, I chose Brushless Field-Oriented Control (FOC) motors due to their high efficiency, precise control, and excellent torque-to-weight ratio.

### Factors Considered
1. **Power and Torque**: These directly affect the robot's ability to handle payloads and perform tasks accurately. Higher torque ensures the robot can lift and manipulate heavier objects, while adequate power ensures smooth and consistent operation.
2. **Efficiency**: Brushless FOC motors are known for their high efficiency, which reduces energy consumption and heat generation, leading to longer operational times and better performance.
3. **Control Precision**: FOC technology enables precise control of the motor's position, speed, and torque, which is essential for tasks requiring high accuracy and repeatability. The choice of motor and type of reduction mechanism significantly impacts gear backlash and precision.
4. **Weight**: The weight of the motors impacts the overall weight of the robot. Lighter motors help achieve a better power-to-load performance ratio, making the robot more agile and responsive.

### Motor Selection Process
1. **Define Requirements**: Establish the torque and power requirements based on the robot's design and intended tasks, considering payload capacity and the range of motion needed for each joint.
2. **Evaluate Motor Options**: Compare different brushless FOC motors based on their specifications, including torque, power, efficiency, and weight.


### Script for Selecting the Best Motor for Each Joint

#### Download Script
[![Download Script](https://img.shields.io/badge/Motor%20Torque%20Optimization-Python%20Script-purple?style=for-the-badge)](/images/projects/14-DOF-Robot/script/motor-torque.py)

To streamline the motor selection process, I developed a script that evaluates various motor options based on predefined criteria. This script takes into account factors such as estimated joint weight, motor weight, and link size to determine if the motor torque is sufficient for the build.
By inputting these parameters, the script quickly identifies the most suitable motor for each joint, ensuring optimal performance and efficiency. This approach simplifies the decision-making process and helps in achieving a balanced design.
<img src="/images/projects/14-DOF-Robot/torque/1.jpg" style="width:100%;">

--- 

# Designing Robot Joint Links
Designing the robot joint links involves several key steps to ensure optimal performance and durability. The process begins with defining the requirements for each joint, including the range of motion, load capacity, and material constraints. Using CAD software, I create detailed models of each joint link, focusing on minimizing weight while maintaining structural integrity.

---

# Using FEA Tool for Optimization
Finite Element Analysis (FEA) optimizes the weight and mechanical strength of each part by simulating various load conditions and stress distributions. This process involves iterating through design configurations to reduce material without compromising strength.  
<img src="/images/projects/14-DOF-Robot/FEA/1.png" style="width:80%;">

---

# CAD Designs
# Motor Design
<img src="/images/projects/14-DOF-Robot/motor/motor.jpg" style="width:100%;">

# Gripper Design
<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <img src="/images/projects/14-DOF-Robot/gripper/1.png" style="width:50%;">
  <img src="/images/projects/14-DOF-Robot/gripper/2.png" style="width:50%;">
  <img src="/images/projects/14-DOF-Robot/gripper/3.png" style="width:50%;">
  <img src="/images/projects/14-DOF-Robot/gripper/5.png" style="width:50%;">
  <img src="/images/projects/14-DOF-Robot/gripper/6.png" style="width:50%;">
  <img src="/images/projects/14-DOF-Robot/gripper/4.png" style="width:50%;">
</div>



## Single Arm
<img src="/images/projects/14-DOF-Robot/render/7.png" style="width:50%;">
<img src="/images/projects/14-DOF-Robot/render/5.jpeg" style="width:50%;">

## Dual Arm with Body
<img src="/images/projects/14-DOF-Robot/render/2.png" style="width:50%;">
<img src="/images/projects/14-DOF-Robot/render/3.jpeg" style="width:50%;">
<img src="/images/projects/14-DOF-Robot/render/4.jpeg" style="width:50%;">

## Rendered Design
<img src="/images/projects/14-DOF-Robot/render/1.jpeg" style="width:50%;">



---

# Kinematics Design

## Robotic Arm Workspace Analysis

### Yoshikawa Index
The **Yoshikawa Index** is a measure of a manipulator's ability to change the position and orientation of its end effector. Higher values indicate greater flexibility and ease of movement, which is crucial for optimal path planning. This index helps identify configurations with high flexibility, ensuring smooth movements and reducing the likelihood of encountering singularities.

<img src="/images/projects/14-DOF-Robot/index-analysis/Yoshikawa Index, Non-Voxelized.jpg" style="width:100%;">

### Workspace Analysis and Visualization
Analyzing the workspace of the robotic arm involves visualizing the areas that the arm can reach and the flexibility of its movements. This analysis helps in understanding the limitations and potential improvements in the design.

<img src="/images/projects/14-DOF-Robot/index-analysis/dual arm-front.jpg" style="width:100%;">
<img src="/images/projects/14-DOF-Robot/index-analysis/front.jpg" style="width:100%;">

### Findings and Potential Hardware Improvements
- The overall reach in front of the chest is somewhat limited by the elbow.
- The end effector's 3DOF, where J4 is farther from J5/J6, results in the end effector's rotational posture "Yoshikawa Index" being more constrained in specific positions.
- The most flexible movement overall is in front of the chest, beyond the elbow joint, which is the most flexible position.

## Design Process
Designing the robot kinematics involves several steps to ensure optimal performance and manipulability:

1. **Define Requirements**: Establish the range of motion, load capacity, and material constraints for each joint.
2. **CAD Modeling**: Create detailed models of each joint link using CAD software, focusing on minimizing weight while maintaining structural integrity.
3. **FEA Optimization**: Use Finite Element Analysis (FEA) to optimize the weight and mechanical strength of each part by simulating various load conditions and stress distributions.
4. **Workspace Analysis**: Perform workspace analysis to visualize the reach and flexibility of the robotic arm. Use indices like the Yoshikawa Index to identify configurations with high flexibility.
5. **Iterate and Improve**: Based on the findings from the workspace analysis, make necessary hardware improvements to enhance the robot's manipulability.

By following this process, the design of the robot kinematics is optimized for better performance, ensuring that the robot can perform tasks efficiently and effectively.

---



# The Build
## Parts
- 7-DoFs high performance accuators /Per-Arm (14 DoFs Total.)
- CNC Alunmimum Designed Parts
- Some 3D printed parts 
- USB to CAN Bus Interface
- Power Bus and connectors. 
- [ORBBEC Femto Bolt](https://www.orbbec.com/products/tof-camera/femto-bolt/) ToF Camera


# Build Process

<img src="/images/projects/14-DOF-Robot/the-build/1.jpeg" style="width:100%; height:auto;">
<img src="/images/projects/14-DOF-Robot/the-build/1.2.jpeg" style="width:100%; height:auto;">

Power Connectors and Power Box
- <img src="/images/projects/14-DOF-Robot/the-build/2.5.jpeg" style="width:80%; height:auto;">
- <img src="/images/projects/14-DOF-Robot/the-build/2.4.jpeg" style="width:80%; height:auto;">



<img src="/images/projects/14-DOF-Robot/the-build/2.2.jpeg" style="width:80%; height:auto;">
<img src="/images/projects/14-DOF-Robot/the-build/2.3.jpeg" style="width:80%; height:auto;">
<img src="/images/projects/14-DOF-Robot/the-build/2.6.jpeg" style="width:80%; height:auto;">
<img src="/images/projects/14-DOF-Robot/the-build/2.7.jpeg" style="width:80%; height:auto;">
<img src="/images/projects/14-DOF-Robot/the-build/2.8.jpeg" style="width:80%; height:auto;">


# Finished Build
<img src="/images/projects/14-DOF-Robot/the-build/5.2.jpeg" style="width:80%; height:auto;">
<img src="/images/projects/14-DOF-Robot/the-build/5.4.jpeg" style="width:80%; height:auto;">  


---

# Software
## ROS2 Project
This section details the integration of the robot with the Robot Operating System (ROS2). It includes steps to simplify the CAD model, convert it to URDF, configure motion planning, and integrate the real robot hardware with simulation environments like Gazebo and MoveIt!.

This guide provides an overview of the necessary steps for integrating a new robot. Each item is extensive and will not be covered in detail here.

### Simplify the Robot CAD Model and Perform URDF Conversion
- Simplify the CAD model of the robot.
- Convert the simplified model to a URDF (Unified Robot Description Format).

### URDF Robot Model
- Import the URDF model.
- Properly define joints, limits, and controller types.
  - DEMO: Interact with URDF and check if all joints are defined correctly
  - <video width="600" controls>
      <source src="/images/projects/14-DOF-Robot/video/joint-move.mp4" type="video/mp4">
    </video>

- Create a parameter manager for parsing Xacro parameters.
- Configure the IKFast kinematics solver for inverse kinematics.
- Define and configure the controller types.
- Implement collision detection and define constraints.

### Setup Planner
- Configure the motion planner.
By completing the steps above, the robot will be ready for simulation, capable of collision checking, motion planning, and inverse kinematics solving. It will be able to perform actions in a virtual environment.
  - DEMO: Planner working in Rviz
  - <video width="600" controls>
      <source src="/images/projects/14-DOF-Robot/video/motion-planned.mp4" type="video/mp4">
    </video>

### Incorporate Real Robot

<img src="/images/projects/14-DOF-Robot/ros/1.png" style="width:100%;">

#### Hardware Interface
- Implement a hardware interface by creating a node for hardware read and write using the `ros2_control` instance. (Refer to the system diagram below.)

#### Implement CAN Driver Code
- Develop CAN driver code for the actuators.
- Test motors individually without links to ensure the driver is implemented safely. These motors are really powerful, and trust me, it gets really scary if safety is not implemented.

When Implementing the Driver:
  - Select motor IDs and configure motors to corresponding addresses.
  - Improve and optimize each motor's FOC PID parameters to prevent oscillations.
  - Implement the CAN bus IO driver to ensure multi-motor control frequency and benchmark CAN bus data throughput.
- <img src="/images/projects/14-DOF-Robot/the-build/2.1.jpeg" style="width:100%;">


#### Implement `ros2_control` Package's Hardware Interface
- Implement the hardware interface for the `ros2_control` package.
- Define joint limits and control mechanisms.
- Implement read and write functionalities.

#### Integration with Simulation
- Post and listen to joint states and joint commands shared with "Gazebo" or "MoveIt!".
- This integration links the simulation environment with the real robot, allowing the hardware interface to command motors with joint angles while leveraging planning algorithms and solvers implemented in MoveIt!.

#### Improve Hardware Controllers

# Control
<img src="/images/projects/14-DOF-Robot/control/1.png" style="width:80%;">
<img src="/images/projects/14-DOF-Robot/control/2.png" style="width:80%;">



### Additional Resources
- [MoveIt! Integration Examples](https://moveit.picknik.ai/main/doc/examples/examples.html#integration-with-a-new-robot)
- [MoveIt! Multiple Robot Arms Tutorial](https://github.com/moveit/moveit_tutorials/blob/master/doc/multiple_robot_arms/multiple_robot_arms_tutorial.rst)
- [ROS Control Documentation](https://wiki.ros.org/ros_control)
- [ROS2 Control Hardware Interface User Documentation](https://control.ros.org/rolling/doc/ros2_control/hardware_interface/doc/hardware_components_userdoc.html#guidelines-and-best-practices)
