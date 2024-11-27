---
title: "Designing the Smallest Linux Computer"
excerpt: "Explore the journey of designing a compact and efficient Linux computer using the Rockchip RV1126 SoC. This project covers everything from PCB layout to firmware engineering, overcoming challenges in high-speed design, power management, and thermal optimization. <br/><img src='/images/projects/SmallestLinuxComputer/8.jpg' width='350'>"
collection: projects
date: 2022-04-09
minute_read: 7
tags:
    - DIY Electronics    
    - Hardware System Design
    - Hardware Design
    - PCB Design
    - High Speed Design
    - FEA
    - Thermal Analysis
    - ARM
    - Layout
    - Firmware
    - Buildroot
    - Linux
    - Kernel
---

# Overview
This project aims to design a minimal Linux computer using an ARM SoC. The chosen SoC for this project is the Rockchip RV1126, which offers a balance of performance and power efficiency. The RV1126 boasts impressive video capabilities, including an ISP, dual 4-lane MIPI interface, 4 cores running at 1.6GHz, and onboard AI with 2 TOPS, making it ideal for embedded AI applications.



# Objectives
- Design a compact and efficient Linux computer.
- Utilize the Rockchip RV1126 SoC.
- Set up Buildroot and Kernel Driver, developing a full Board Support Package (BSP).
- Achieve Linux boot-up.
- Optimize for low power consumption.


# Main Features for the Miniature Design
- Rockchip RV1126 SoC (409 pins, 0.65mm ball pitch)
- 1GB DDR4 RAM (2x 512MB)
- 8GB eMMC storage
- USB 2.0 OTG port for USB device applications
- 14MP camera MIPI interface  
- 2 Tops AI Engine
- PDM Mics

# 6 Layers PCB Layout Design
<img src="/images/projects/SmallestLinuxComputer/1-1.jpg" style="width:50%;">


# Challenges for Miniature Hardware Design
- **Complex Board Design**: This project involves one of the more complex board designs, incorporating numerous high-speed protocols that I am not entirely familiar with.
- **Power Management**: The reference design's PMIC power solution occupies too much space. I optimized it by integrating PWM-controlled DC-DC converters and LDOs. Additionally, the kernel driver needs to be adapted accordingly.
- **DDR Design**: The reference design's DDR layout consumes excessive space. To improve routing, I performed bank swaps and data pin swaps. It is uncommon to deviate from reference designs or templates, as they are often validated and guaranteed to work. However, for this miniature design, these optimizations are necessary. Following standard DDR4 routing guidelines, a stress test before the production run is essential.
- **High-Speed Design Considerations**: High-speed designs, such as DDR, eMMC, and MIPI, require meticulous attention during layout. By studying more documentation on DDR and similar technologies, I created better DRC classes and rules for routing constraints.
- **Signal Integrity Optimization**: Topics such as trace length, length matching, decoupling, termination resistors, crosstalk prevention, board stack-up, and maintaining good ground planes are crucial when optimizing signal integrity.

    - Here are two publications that significantly enhanced my understanding of high-speed designs:
        - [High Speed Digital Design: A Handbook of Black Magic 1st Edition - by Howard Johnson (Author), Martin Graham (Author)](https://www.amazon.com/High-Speed-Digital-Design-Handbook/dp/0133957241)
        - [2010 高速电路设计实践-王剑宇](https://weread.qq.com/web/bookDetail/bc6325b059ff42bc6d91d73)

- **Thermal Management**: Designing a compact system presents significant challenges in thermal management. The limited board space and high-power components make heat dissipation difficult. It is crucial to understand and document the power requirements, estimate thermal performance, and ideally conduct a Finite Element Analysis (FEA) for thermal analysis. Additionally, designing dedicated heatsinks or incorporating fans may be necessary to ensure adequate cooling.
- **Continuous Improvement and Optimization**: Miniature designs require constant evaluation and engineering validation. The process involves continuous optimization and improvement. Persistence and attention to detail are essential to achieve a successful design.  
  - **Design iterations and improvements**  
     <img src="/images/projects/SmallestLinuxComputer/4.jpg" style="width:50%;">

---
# Fabricated PCB Board
Look how tiny it is! Even smaller than the Raspberry Pi Zeros 😊
<img src="/images/projects/SmallestLinuxComputer/8.jpg" style="width:50%;">
<img src="/images/projects/SmallestLinuxComputer/5.jpg" style="width:50%;">

--- 

# Firmware Engineering
The firmware engineering process involves creating the BSP, kernel, Buildroot image, and peripheral drivers. Below are the steps to create new BSP firmware for a new board design:

It's a huge topic on its own. I won't go through too much detail on developing custom firmware. But here I will quickly summarize what's needed for building a new BSP package.

## Steps to Create BSP Firmware

1. **Board Bring-Up**:
     - Start with the hardware schematics and ensure all components are correctly placed and connected.
     - Power up the board and check for any hardware issues.

2. **Bootloader Configuration**:
     - Configure and compile the bootloader (e.g., U-Boot) for the new board.
     - Ensure the bootloader can initialize the hardware and load the kernel.

3. **Kernel Configuration**:
     - Configure the Linux kernel for the new board, enabling necessary drivers and features.
     - Compile the kernel and ensure it boots on the new hardware.

4. **Buildroot Setup**:
     - Set up Buildroot to create a minimal root filesystem for the new board.
     - Include necessary libraries and applications required for the project.

5. **Driver Development**:
     - Develop and integrate drivers for any custom hardware components.
     - Test and debug the drivers to ensure proper functionality.

6. **Testing and Optimization**:
     - Perform extensive testing to ensure the firmware is stable and performs well.
     - Optimize the firmware for power consumption and performance.

By following these steps, you can create robust BSP firmware for your new board design, ensuring it meets the project's objectives and requirements.

## Linux Booted!!
Will be doing more CPU and DDR and NPU stress tests.
<img src="/images/projects/SmallestLinuxComputer/7.jpg" style="width:50%;">