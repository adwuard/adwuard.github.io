---
title: "Making Smallest Linux Computer"
excerpt: "Making Smallest Linux Computer. <br/><img src='/images/projects/SmallestLinuxComputer/1.jpg' width='550'>"
collection: projects
date: 2022-04-09
tags:
  - DIY Electronics
  - Hardware System Design
  - ARM
  - Layout
---

# Overview
This project is aim to design a minimal Linux Computer with ARM SoC. The SoC that will be used in this project will be Rockchip RV1126. It offers a balance of performance and power efficiency The RV1126 have amazing video capability. ISP, Dual 4 Lane MIPI Interface. 4 Core running at 1.6GHZ. And on board AI with 2Tops. Making it ideal for embedded AI applications.

## Objectives
- Design a compact and efficient Linux computer.
- Utilize the Rockchip RV1126 SoC.
- Ensure the system is capable of running a full Linux distribution.
- Optimize for low power consumption.

## Main Components
- Rockchip RV1126 SoC  (409 Pins 0.65 Ball Pitch)
- 1GB DDR3 RAM (x2 512MB)
- 8GB eMMC storage
- USB 2.0 OTG port for USB Device Applications
- 14MP Camera MIPI Interface

## Steps
1. **Design the PCB**: Create a schematic and layout for the PCB using a tool like KiCad.
2. **Assemble the Components**: Solder the components onto the PCB.
3. **Install Linux**: Flash a Linux distribution onto the eMMC storage.
4. **Test the System**: Verify that all components are working correctly and the system is stable.

## Challenges

- Ensuring compatibility with various Linux distributions.
- Managing heat dissipation in a compact form factor.
- Optimizing power consumption without sacrificing performance.

## Conclusion

This project aims to push the boundaries of what is possible with small form factor Linux computers. By leveraging the capabilities of the Rockchip RV1126 SoC, we hope to create a powerful yet efficient system suitable for a variety of applications.

## Gallery

![PCB Design](/images/projects/SmallestLinuxComputer/pcb_design.jpg)
![Assembled Board](/images/projects/SmallestLinuxComputer/assembled_board.jpg)
![Running Linux](/images/projects/SmallestLinuxComputer/running_linux.jpg)