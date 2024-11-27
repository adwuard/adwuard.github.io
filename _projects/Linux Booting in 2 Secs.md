---
title: "Linux Booting in 2 Seconds"
excerpt: "Discover how to achieve a lightning-fast Linux boot time of just 2 seconds. Learn about the techniques used to minimize image size and enhance performance. Perfect for projects requiring quick startup and efficient resource usage. <br/><img src='/images/projects/FastLinuxBoot/3.jpg' width='350'>"
collection: projects
minute_read: 8
date: 2024-07-07
tags:
  - Linux
  - Buildroot
  - U-Boot
  - Kernel
  - Boot Optimization
  - ARM SoC
  - Rockchip
  - Firmware Engineering
  - Synthsizer
  - DIY Projects
  - DIY Electronics
  - Embedded Systems
---

## Source Code
[![GitHub](https://img.shields.io/badge/GitHub-rv1106_tracker_screen-blue?logo=github&style=for-the-badge)](https://github.com/adwuard/rv1106-tracker-screen)   
![GitHub stars](https://img.shields.io/github/stars/adwuard/rv1106-tracker-screen?style=social&style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/adwuard/rv1106-tracker-screen?style=social&style=for-the-badge)

# **Overview**
In collaboration with [SoloLinker](https://www.sololinker.com/en/1956.html), we present the SoloLinker-A Dev Board, a compact and powerful SoC board. Powered by the [Rockchip RV1106](https://www.rock-chips.com/uploads/pdf/2022.8.26/192/RV1126%20Brief%20Datasheet.pdf) single-core SoC running at 1.2GHz, this board features a small footprint with impressive capabilities. It includes **256MB of integrated DDR memory**, **EMMC or SPI Flash for storage**, a **0.5Tops AI engine**, and supports **WiFi, camera, USB OTG, and SD card interfaces**. This makes it ideal for small projects requiring these interfaces, offering an excellent power consumption to performance ratio.

<img src="/images/projects/FastLinuxBoot/3.jpg" style="width:80%">

### Potential Project Ideas with this dev board:
- AI Camera with MIPI camera and NPU AI Applications
- Small low-power WiFi-enabled projects
- USB 2.0 UVC Camera, USB UAC Audio, USB MTP File System, etc.
- Small display projects
- Small AI computing stick

---

# **Problem and Solution**

>**The goal is to achieve a minimal size and a minimal Linux system, ensuring a lightning-fast boot time of just 2 seconds**.

The aim is to create a minimal Linux image that optimizes both image size and boot-up time. This approach allows the use of cheaper and smaller NAND Flash, reducing the Bill of Materials (BOM) cost. Additionally, the rapid boot-up time enhances the user experience and makes the system more responsive for various "gadget-like" applications.


--- 
  
# **Optimizations of Linux Firmware**
By focusing on essential components and eliminating unnecessary features, we can achieve a lean and efficient system.

### **Know Your Limitations**
- Use `dmesg` and other boot log messages to check and analyze the boot-up process.
- Understand the hardware limitations and optimize accordingly.
- Profile the system to identify and address performance bottlenecks.
- Document the changes and optimizations for future reference and reproducibility.

### **U-Boot**
- Configure U-Boot to initialize only essential peripherals.
- Enable fast boot options and disable unnecessary features.

### **Kernel**
- Customize the kernel configuration to include only necessary drivers.
- Use kernel compression techniques to reduce the kernel size.
- Apply patches and optimizations for faster boot times.
- Keep long initialization drivers as modules and load modules on demand to reduce initial boot time.

### **Root Filesystem (RootFS)**
- Monitor and profile the boot process to identify and eliminate bottlenecks.
- Optimize init scripts to minimize startup time.
- Create a minimal root filesystem with only essential libraries and binaries.
- Use lightweight init systems like BusyBox.
- Optimize the filesystem layout for faster access and reduced size. Use a lightweight filesystem like SquashFS for read-only partitions.
- Optimize the boot script for minimal delay.

### **Image Packing**
- Create a partition layout that optimizes space and access time.
- Ensure proper alignment of partitions to disk usage.
- Compress the root filesystem to reduce the image size.
- Use tools like `genext2fs` or `mksquashfs` for creating the filesystem images.

### **It is a Continuous Process**
Optimization is an ongoing effort. Regularly review and refine the system to maintain optimal performance. 
Stay updated with the latest tools and techniques, and continuously profile the system to identify new bottlenecks. 

- Test the image thoroughly to ensure all components are functioning correctly.

---

# **Image Partitions for 256MB NAND Flash**
## **Compiled Partitions and Sizes**
<img src="/images/projects/FastLinuxBoot/2.png" style="width:80%">

## **Packing the Partitions into One Update File**
```shell
mtdparts=spi-nand0:256K(env),1M@256K(idblock),1M(uboot),5M(boot),235M(rootfs)
```

---

# **Results after Boot Optimizations**
After implementing the above optimizations, the boot time was reduced to about **2.2 seconds**! The final image size was also significantly reduced to a **16MB** RootFS, with a total image size of **22MB**. This guarantees a fast flashing process, making it suitable for smaller NAND Flash storage. The system is now more responsive and efficient, providing a good starting template for various projects.  

<img src="/images/projects/FastLinuxBoot/1.jpg" style="width:80%">

---

# **Example Project Demo**
With this minimal firmware, I created a UI hosting app for my [Tracker Synthesizer Project](/projects/Tracker%20Synthsizer/). This app serves as a UI host for the tracker keyboard and reroutes audio from USB audio to the internal speaker.

While there are alternative UI hosts built with Raspberry Pi, this solution offers unbeatable boot-up time and minimal BOM cost.

### **BSP Changes for this Application:**
- Minimal [SDL (Simple DirectMedia Layer)](https://www.libsdl.org/) Render Engine Library Build
- Small RGB Display -> `/dev/fb0` framebuffer driver and SDL support
- Touch Panel Driver -> `/dev/event`
- USB Host Audio/HID/Serial Support
- ALSA Audio Routing

<img src="/images/projects/FastLinuxBoot/demo.jpg" style="width:80%">
