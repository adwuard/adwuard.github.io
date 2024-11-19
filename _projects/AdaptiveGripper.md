---
title: "Adaptive Robot Gripper"
excerpt: "Designing a flexible finger with silicone material and a torque feedback motor controller. This provides a low-cost robot gripper with a large gripping distance. <br/><img src='/images/projects/AdaptiveGripper/1.jpg' width='550'>"
collection: projects
date: 2024-07-24
tags:
  - Robotics
  - DIY Electronics
  - DIY Project
  - CNC Machining
  - 3D Printing
  - Control and Dynamics
  - Motor Controller
  - STM32
  - Robot Gripper
---




# Overview
<img src="/images/projects/AdaptiveGripper/1.jpg" width="650">  
I have always wanted to build my own power gripper. Selecting a good gripper is not an easy task. The first consideration is its capability and intended use. Some grippers are suitable for small, delicate tasks, while others are designed for grabbing larger, heavier objects. Additionally, some grippers, like the Robotiq Grippers, come with torque feedback for more accurate gripping force. There is no one-size-fits-all solution. Most available options are either too expensive or not adaptive enough to cover a wide range of scenarios and applications. This is why I am designing my own gripper. This should be an enjoyable and rewarding project.

# The gripper I envision will have the following features:
- Low cost and 3D printable
- Reliable and doesn't require much maintaining
- Adaptive soft silicone fingers that provide better grip and adapt to different surface curvatures
- CAN and Ethernet controlled
- ROS2 supported

# Motion Study
## Chain of Transmission
The transmission chain for the adaptive gripper is designed to ensure precise and efficient motion. It consists of the following components:

1. **Stepper Motor**: Provides the initial driving force.
2. **1:10 Reduction Gearbox**: Reduces the speed and increases the torque of the motor.
3. **1:1 Belt Drive**: Transfers the motion from the gearbox to the lead screw without altering the speed or torque.
4. **8mm Pitch Lead Screw**: Converts the rotational motion into linear motion.
5. **Finger on Linear Guide Rail**: The final component that moves linearly to grip objects. The linear guide rail provides enhanced stability and accuracy, ensuring precise and reliable gripping performance.

<iframe width="560" height="315" src="https://www.youtube.com/embed/O1reG3t5D7k?si=ywxng9yhqmV2fDN3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## What I Learned:
- Achieving an optimal balance between weight, size, speed, and lead screws pitch distance.
- The adaptive finger is made of a soft material. While torque feedback is not as accurate as with a rigid body, by collecting data on motor sensing current and stepper motor distance changes, we can model an estimated gripping force. It's not as accurate. But I believe it is sufficient enough for most use cases.
- For soft material design, the fencing spine-like features provide adaptive gripping capabilities. The tip section and middle section offer different gripping forces. The tip is more solid, while the middle section is more flexible, allowing it to curve and wrap around the gripped object. It's a quite geneious geometry and design.
- This was my first time using an Ethernet to CAN adapter. Socket programming allows remote access to the gripper over Ethernet, while it is also compatible with direct CAN wiring.
- This was my first time using a double-sided lead screw, which involved sourcing parts and cutting them to the required length.
- Tolerance control of each part is crucial. The most challenging aspect is the installation of the lead screw. The position of the lead screw and the placement of the nuts significantly affect the accuracy of the finger. Designing in tight spaces and minimal parts required is a fun challenge.

## Making it ROS2 Supported
To integrate the adaptive gripper with ROS2, several steps need to be undertaken to ensure seamless operation and compatibility with robotic systems:
- Convert the final gripper CAD model to URDF XACRO format.
- Define collision checks and avoidance mechanisms.
- Develop a driver for the CAN protocol and implement a ROS2 node for gripper control.

---

# The build
## All the printed parts in ABS
<img src="/images/projects/AdaptiveGripper/6.jpg" width="650">

## Fully assembled gripper, CAN cable connected
<img src="/images/projects/AdaptiveGripper/4.jpg" width="650">

## Stepper Motor Controller
The stepper motor controll board is encoded. Step close loop control, Preventing step loss.  
<img src="/images/projects/AdaptiveGripper/11.jpg" width="650">


## Rendered Image, Mounted on UR5 6-DoF Robot
<img src="/images/projects/AdaptiveGripper/9.jpg" width="650">
<img src="/images/projects/AdaptiveGripper/10.jpg" width="650">