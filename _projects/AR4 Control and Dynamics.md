---
title: "AR4 Control and Dynamics: Enhancing Robot Arm Performance"
excerpt: "Explore the AR4 Control and Dynamics project, featuring custom robot controllers, improved motor control, and simplified wiring. Learn how to build and optimize a robot arm.<br/><img src='/images/projects/6-DOF-AR4/1.jpg' width='250'>"

collection: projects
date: 2023-12-06
tags:
  - Robotics
  - Kinematics
  - Control and Dynamics
  - Mechanical Engineering
  - CNC Machining
  - DIY Build
  - Open Source
  - CAN Protocol
---

# Overview

Welcome to the AR4 Control and Dynamics project! This open-source initiative builds upon the original AR4 robot arm design by introducing several enhancements aimed at improving performance, control, and ease of use. By participating in this project, I will not only learn how to build a robot arm from scratch but also gain valuable insights into the fields of robotics, kinematics, and control theory. The modifications made in this project focus on simplifying the wiring, enhancing motor control, and improving overall system efficiency.

For more information on the original AR4 design, visit [Annin Robotics](https://www.anninrobotics.com/).


# Project Goals

This project aims to achieve several key objectives:

- Understand the process of building a robot arm from parts.
- Gain experience in machining and CNC manufacturing, and understand part designs. And sourcing and making my own parts does help me learn a lot.
- Learn the basics of robotics dynamics and control theory through this open-source project.
  - Write my own Forward and Inverse Kinematics solver. 
- Explore motor selection and compare the performance of stepper motors, sun gears, harmonic gears, and brushless motors along with their controllers. Make optimal motor choice base on torque requirements
- Implement positive design improvements throughout the project.

# Improvements Based on the Original AR4

This project introduces several significant improvements I made over the original AR4 design:

<img src="/images/projects/6-DOF-AR4/6.jpg" style="width:80%;">

- **Custom Miniature Motor Closed-Loop Stepper Motor Controller:**
  - **Pros:**
    - Reduces wiring complexity from 72 wires to just 4 (Power(+/-) and CAN(+/-)).
    - Low profile design eliminates the need for a bulky controller box.
    - Features a 16-bit encoder for precise control and no lost steps.
    - Enhanced torque and acceleration control.

- **CAN Bus Enabled:**
  - Simplifies communication using Ethernet or USB to CAN bus converters.
  - Leverages industry-standard protocols for broader compatibility.

- **Faster Control Frequency:**
  - Replaces the sequential motor control loop in Teensy with a more efficient design.
  - Allows for faster and more accurate actuation of multiple motors.

- **Improved Axis 6 with Magnetic Switch:**
  - Prevents damage to the limiting switch from motor multi-turns.

- **Python Enabled:**
  - Direct CAN bus control eliminates the need for a controller box and Teensy.
  - Facilitates learning kinematics programming and ROS control planning using Python.

- **Cost Efficiency:**
  - Eliminates the need for controller drivers and Teensy, reducing space and complexity in the electronic design.


# Video Demo - Zeroing Sequence
<iframe width="560" height="315" src="https://www.youtube.com/embed/C2str8d0TIA?si=4LI0sLHhDSoVcf4i" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Build Details
### Completed Build

<img src="/images/projects/6-DOF-AR4/3-4.jpg" style="width:80%;">

### J6 Controller, CAN, and Power Breakout Board

<img src="/images/projects/6-DOF-AR4/3.jpg" style="width:50%;">

### J2/J3 Controller Board

<img src="/images/projects/6-DOF-AR4/3-1.jpg" style="width:50%;">

### J4/J5 Controller Board

<img src="/images/projects/6-DOF-AR4/3-7.jpg" style="width:50%;">

### CAN and Power Breakout Board

<img src="/images/projects/6-DOF-AR4/3-2.jpg" style="width:50%;">

### More Angles

<img src="/images/projects/6-DOF-AR4/3-3.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/3-6.jpg" style="width:50%;">

# Electronics

Custom small CAN and Power breakout board, using XT30(2+2) connector.

<img src="/images/projects/6-DOF-AR4/4-1.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/4-2.jpg" style="width:50%;">

Custom mount for the breakout board, each motor may be placed differently.

<img src="/images/projects/6-DOF-AR4/4-3.jpg" style="width:50%;">

All the custom encoded controller boards attached to each motor.

<img src="/images/projects/6-DOF-AR4/4-4.jpg" style="width:50%;">

# Build Process

<img src="/images/projects/6-DOF-AR4/5-1.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/5-2.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/5-3.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/5-10.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/5-5.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/5-6.jpg" style="width:50%;">
<img src="/images/projects/6-DOF-AR4/5-7.jpg" style="width:50%;">

### J5 Design

The use of a lead screw and belt mechanism allows for the motor to be positioned at the back, effectively reducing the weight stress on the endpoint. This design choice significantly enhances the overall efficiency and performance of the robot arm.

<img src="/images/projects/6-DOF-AR4/5-8.jpg" style="width:50%;">

### Wiring: Connecting CAN and Power

<img src="/images/projects/6-DOF-AR4/5-9.jpg" style="width:50%;">

