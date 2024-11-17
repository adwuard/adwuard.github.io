---
title: "A Tracker Synthsizer"
excerpt: "Inspired by Dirtyware M8 Tracker Synthsizer. This is a slightly over-engineered tracker keyboard that integrates both Teensy4.1 and a keyboard. <br/><img src='/images/projects/trackerkb/cnc-build/2.jpg'>"
collection: projects
date: 2024-07-20
Tags:
  - Synthesizer
  - Teensy 4.1
  - RP2040
  - CNC Machining
  - DIY Electronics
  - Open Source Hardware
  - Music Production
  - Embedded Systems
  - Custom Keyboards
---

# Now Open-Sourced!
[![GitHub](https://img.shields.io/badge/GitHub-TrackerKB-blue?logo=github)](https://github.com/adwuard/TrackerKB)   
![GitHub stars](https://img.shields.io/github/stars/adwuard/TrackerKB?style=social)
![GitHub forks](https://img.shields.io/github/forks/adwuard/TrackerKB?style=social)

--- 

## Fully Assembled units and parts are available here: 
Small batch custom build. Limited quantity now available and ready to ship!  
[![Ed's Lab Shop](https://img.shields.io/badge/Shop-Ed's_Lab_Shop-blue?style=for-the-badge)](https://edslab.myshopify.com/)   

---

# Video Walkthrough
<iframe width="560" height="315" src="https://www.youtube.com/embed/CM8WWjXYxZA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---


# Overview
This is a slightly over-engineered tracker keyboard that integrates both Teensy4.1 and a keyboard.

<div style="display: flex; flex-direction: row; margin-top: 20px;">
  <img src="/images/projects/trackerkb/render/1.jpg" style="width:75%;">
</div>

# Features
- Built-in USB HUB connected to both Teensy 4.1 and Keyboard
- Keyboard is implemented with RP2040 microcontroller
- Same swappable mechanical keyboard as the original
- High-quality CNC machined case, providing the same handling experience as the original
- Robust connection with USB-C screw lock cable
  
# Hardware Guide
### System Diagram 
<img src="/images/projects/trackerkb/system diagram.jpg" width="550">

## Electronics Build Guide
Layer View          |  PCB (Front) |  PCB (Back)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="/images/projects/trackerkb/pcb-thumbnails/pcb-back-view-revc.jpg" width="350"> | <img src="/images/projects/trackerkb/pcb-thumbnails/pcb-front-view-revc.jpg" width="350"> | <img src="/images/projects/trackerkb/pcb-thumbnails/pcb-layers-view-revc.jpg" width="350">

PCB manufacture requirements: 
- Layers: `2-Layers`
- Board thickness: `1.6mm`
- Board dimensions: 90mm x 97.35mm 

All the components are 0603 footprints. The pads are designed with larger pads, making them great for hand-soldering. The most complex component in this project is the RP2040, which is in a QFN package, so hot-air reflow is required. An alternative approach is to make a custom PCB stencil, which would make the process much easier.

### Soldering
### Soldering Process
- PCB  
<img src="/images/projects/trackerkb/build-process/20240620-DSCF4548.jpg" width="250">
- Stencil and Solder Paste  
<img src="/images/projects/trackerkb/build-process/20240620-DSCF4552.jpg" width="250">
- Pick and Place  
<img src="/images/projects/trackerkb/build-process/20240620-DSCF4557.jpg" width="250">
- Reflow Oven  
<img src="/images/projects/trackerkb/build-process/20240620-DSCF4566.jpg" width="250">

### Tips on Soldering Teensy 4.1 
- Solder the pins that are marked with circles. Only 6 pins are required for soldering. This is enough to hold the board while still being easy to de-solder and repurpose if needed. To solder, add some solder flux onto the pads. Solder one pin first and ensure it's aligned properly. Place the soldering iron on the Teensy through-hole pad, and add a generous amount of solder. Hold the iron longer, around 8-15 seconds, and let the solder sink into the pad below. Then use multi-meter to test continuity between teensy pad and the pad directly below.
  - <img src="/images/projects/trackerkb/build-process/teensy-soldering.png" width="350">

**REV (A/B) Hardware Teensy USB Connection**    
- Make a twisted wire for Teensy USB communication. Solder it and adding adhesive glue is recommended.
  - <img src="/images/projects/trackerkb/build-process/twist-wire.jpg" width="350">   
**REV (C) Hardware Teensy USB Connection**  
- In place soldering pads, solder directly with the Teensy USB Test Points
- <img src="/images/projects/trackerkb/build-process/rev-c-usb-tp-soldering.jpg" width="350">


## PCB Testing
<img src="/images/projects/trackerkb/build-process/20240620-L1008894.jpg" width="550">  

🎉🎉🎉 Great job on finishing the PCB assembly. Now we will go through a checklist and testing process to help you get your tracker keyboard up and running!

- Visually check that all components are soldered properly with no solder bridges or shorts.
- Before connecting to a PC, check that your 5V and 3V3 are not shorted to ground.
- Note that the RP2040 is powered by Teensy's on-board DC converter, so the Teensy must be soldered in order for the RP2040 to work properly.
- Follow the Software Guide section for flashing tutorials.
- You can always open the Device Manager on your PC to check if all devices are being detected properly. Three devices should show up:
  - A `USB 2.0 Hub` device
  - An Tracker `Serial` and `Audio` composite device
  - A `HID Keyboard` device


# Three Versions of Enclosure are Available
### Option 1: CNC Machined Enclosure
Best quality and experience. It's a CNC machined enclosure that offers a great hand-held experience.
```
Bill of Materials
- x4 M3x8mm screws 
- x1 CNC top and bottom case 
- x1 Optional, USB Type-C cable with screw lock (The pitch distance of the two screws is 15mm, and the size is M2 thumb screws)
- x4 8mm x 1.5mm rubber pads
- x1 12mmx12mmx1mm Thermal Pad 
```

<!-- <img src="/images/projects/trackerkb/cnc-build/cnc-cases.jpg" width="460"> -->

### Option 2: Sandwiching Acrylic Enclosure
A 4-layer acrylic sandwiching approach offers handling weight and durability while keeping the price cheaper compared to CNC. Note that the USB lock threads are not available in this design. The `*.dxf` files of each layer are provided for laser cut manufacturing.

How to assemble?
- Stack them up. The hole size on the layer-4 plate is slightly smaller, so screw taps will be created when screwing in the screws.
```
Bill of Materials
- x4 M3x14mm screws 
- x1 Layer 1 Acrylic (3mm thick)
- x1 Layer 2 Acrylic (3mm thick)
- x1 Layer 3 Acrylic (4mm thick)
- x1 Layer 4 Acrylic (3mm thick)
```

<img src="/images/projects/trackerkb/acrylic-build/acylic_stacking.png" width="560">

Assembled (Front)          |  Assembled (Back)
:-------------------------:|:-------------------------:
<img src="/images/projects/trackerkb/acrylic-build/acylic_front.png" width="350"> | <img src="/images/projects/trackerkb/acrylic-build/acylic_back.png" width="350">

### Option 3: 3D Printed Enclosure
This 3D printed design is nearly identical to the CNC version but optimized for 3D printing. Note that the USB lock threads are not available in this design.

How to assemble?
- The hole size on the bottom case is slightly smaller, so screw taps will be created when screwing in the screws.
```
==== Print settings ==== 
- PLA or ABS filament  
- 25% infill  
- Support enabled  

==== Bill of Materials ====  
- x4 M3x8mm screws 
- x1 Printed top and bottom case
```

### Slicer Build Plate
<img src="/images/projects/trackerkb/3d-print-build/3d-printing-plate.jpg" width="350"> 

### Improving Thermal Performance
While the Teensy operates safely with passive cooling, adding additional heat spreaders can further enhance thermal performance.

Here are two additional recommendations that could improve thermal:
- Use ABS to print for better thermal tolerance.
- Copper heat spread. Distributing thermal evenly across the back of the case (see image), Also add some "non-conductive tape" on the "cooper conductive side" to prevent short!

<img src="/images/projects/trackerkb/3d-print-build/thermal-1.png" width="550"> 

### Copper Heat Spread Thermal Analysis:
This validates that cooper heat spread is an effective approach. Ensuring the casing is well below 45C (113F), Guarantees casing is cool/warm to touch.<img src="/images/projects/trackerkb/3d-print-build/thermal-2.png" width="350"> 
<img src="/images/projects/trackerkb/3d-print-build/thermal-3.png" width="350"> 



# Software Guide
Two firmware flashes are required:
1. Tracker Headless firmware on Teensy
2. Keyboard firmware on the RP2040 microcontroller

## 1. Tracker Headless Firmware (Teensy 4.1)
- Pre-compiled Tracker Headless Firmware and flashing guide can be found here: [Headless Firmware](https://github.com/Dirtywave/M8HeadlessFirmware)
- This is a pretty standard process and can be done easily.

## 2. Keyboard Firmware (RP2040 MCU)
The keyboard is implemented with RP2040 keyboard HID implementation. You wouldn't need to build this source file yourself. Pre-built firmware is available for easy flashing.

### Keyboard Firmware Highlights
- Implemented in C++, offering better low-latency input compared to MicroPython.
- Single firmware file. Drag and drop for a simple and fast upload process.
- No more annoying MicroPython disk pop-up every time the device is connected.
- HID key mapping: 
    (key mapping is the same as [M8 WebDisplay's](https://derkyjadex.github.io/M8WebDisplay/) default)

| Tracker Hardware Keys | Mapped HID Keys |
|-----------------------|-----------------|
| Arrow Keys            | Arrow Keys      |
| Option                | Z               |
| Edit                  | X               |
| Shift                 | Left Shift      |
| Play                  | Space Bar       |

### Pre-built keyboard firmware can be found here --> [Keyboard Firmware](software/Release)
### Steps for Flashing Keyboard Firmware:
- Download the single firmware `pico-tracker-keyboard.uf2` file from the [Release](software/Release) Folder.
- "Press and Hold" the `Boot` button on the RP2040 PCB board, connect the USB to your PC, then release the `Boot` button.
- A disk will show up or get mounted, indicating that your RP2040 is in loader mode and ready to load firmware.
- Simply drag and drop the `pico-tracker-keyboard.uf2` firmware file to the mounted disk.
- The RP2040 will then unmount and reboot itself with the new firmware.

