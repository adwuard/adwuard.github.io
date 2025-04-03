---
title: 'Accelerate PicoCalc Debugging with PicoProbe'
excerpt: "This guide demonstrates how to bypass the repetitive manual steps of firmware flashing on the PicoCalc by leveraging the Pico Probe's GDB debugging capabilities. Say goodbye to pressing hard-to-reach buttons and enjoy a hands-free, efficient workflow for debugging and firmware updates."
date: 2025-04-03
comments: true
tags:
    - PicoCalc 
    - DIY Electronics
    - Guide
    - Documentation
    - RP2040
    - Open Source Hardware
toc: true
toc_label: "Table of Contents"
toc_sticky: true
header:
  overlay_image: /images/overlays/unsplash/faded_gallery-7stSlxNAmfc-unsplash.jpg
  caption: "Photo credit: [**Faded Gallery @ Unsplash**](https://unsplash.com/@faded_gallery?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)"  
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
---

> Faster Debugging and Firmware Flashing for PicoCalc


<img src="https://static.wixstatic.com/media/3833f7_ef04ec7a5e684f79974e9c2f786361c2~mv2.png/v1/fill/w_960,h_480,al_c,lg_1,q_90,enc_avif,quality_auto/PicoCalc_fig17.png
" style="width: 50%;">

# My Problem
I recently acquired a new PicoCalc, the latest release from Clockwork Pi. This innovative device boasts a stunning IPS screen, a responsive QWERTY keyboard, built-in speakers, and a high-capacity battery. It supports Raspberry Pi Pico models 1/1H/1W/2/2W, making it a versatile tool for developers and hobbyists alike.

While exploring the SDK and working on code development and debugging, I encountered a challenge with the recommended firmware flashing method. The official process involves using the boot select button to mount the device as a drive, then dragging and dropping the new firmware. Although this method is straightforward, it requires manually powering off the device, pressing the hard-to-reach boot select button hidden beneath the case, and then powering it back on. This repetitive process can be cumbersome and time-consuming.

Enter the Raspberry Pi Pico Probe—a cost-effective solution that offers full GDB debugging capabilities and a seamless, hands-free firmware flashing experience. In this guide, I’ll walk you through the steps to set up the Pico Probe with your PicoCalc for a smoother development workflow.
## What You'll Need

To get started, ensure you have the following items and tools ready:

### Hardware
- **PicoCalc**: A versatile development device. [Learn more about PicoCalc](https://www.clockworkpi.com/picocalc).
- **Raspberry Pi Pico Probe**: A cost-effective debugging tool that includes debug connectors. [Purchase here](https://www.raspberrypi.com/products/debug-probe/).
- **3-Pin 2.54mm Header Pin** (optional): If you're using the Pico 1H, the default package already includes connectors, so no soldering is required.

### Tools
- **Small File or Cutting Pliers**: For minor adjustments or trimming PicoCalc casing.
- **Soldering Station** (optional): Required only if you're working with Pico models like 1/1W/2/2W that need SWD port soldering.

With these items in hand, you'll be ready to streamline your debugging and firmware flashing process.


--- 

# Setting Up Hardware

## Soldering the Debug Probe (If Required)
If you're using the default PicoCalc configuration, which includes the Pico 1H, you're in luck—it comes pre-equipped with a debugging connector, so no soldering is necessary. However, if you're working with other Raspberry Pi Pico models (e.g., Pico 1, 1W, 2, or 2W) that lack a pre-installed connector, you'll need to solder a 3-pin 2.54mm header pin to enable debugging.

<img src="/images/posts/2025-04-03-accelerate-PicoCalc-debugging/1.jpg" style="width: 50%;" alt="Pico 1H with debugging connector">
<img src="/images/posts/2025-04-03-accelerate-PicoCalc-debugging/2.jpg" style="width: 50%;" alt="Soldering a 3-pin header">

## Modifying the Casing
To accommodate the SWD wire, you'll need to make a small modification to the PicoCalc's bottom casing. Use a file or cutting pliers to create a clean, precise hole. This ensures the wire can pass through without compromising the device's aesthetics or functionality.

<img src="/images/posts/2025-04-03-accelerate-PicoCalc-debugging/3.jpg" style="width: 80%; margin-right: 10px;" alt="Casing modification for SWD wire">

## Clean Finish
Once the modifications are complete, you'll have a neat and functional setup. The SWD wire will exit through the newly created hole, maintaining a tidy appearance while ensuring easy access for debugging.

<img src="/images/posts/2025-04-03-accelerate-PicoCalc-debugging/4.jpg" style="width: 50%;" alt="Cleanly modified PicoCalc casing">
<img src="/images/posts/2025-04-03-accelerate-PicoCalc-debugging/5.jpg" style="width: 50%;" alt="SWD wire exiting through the casing">


---

# Setting Up the Pico Probe

Follow the official [Pico Probe documentation](https://www.raspberrypi.com/documentation/microcontrollers/debug-probe.html) to install OpenOCD on your system (Windows/Linux/Mac). Once set up, the Pico Probe allows you to keep the PicoCalc powered by its battery while flashing firmware seamlessly.

---
## Flashing Firmware
Use the following commands to flash firmware onto your PicoCalc:

### For Pico 1 Models
```shell
sudo openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000" -c "program hello_serial.elf verify reset exit"
```

### For Pico 2 Models
```shell
sudo openocd -f interface/cmsis-dap.cfg -f target/rp2350.cfg -c "adapter speed 5000" -c "program hello_serial.elf verify reset exit"
```
---
## Debugging with OpenOCD and GDB

Start the OpenOCD server:
```shell
sudo openocd -f interface/cmsis-dap.cfg -f target/rp2040.cfg -c "adapter speed 5000"
```

In a separate terminal, navigate to your binary's directory and attach GDB to the OpenOCD server:
```shell
gdb blink.elf
> target remote localhost:3333
> monitor reset init
> continue
```

---
## Serial Debugging

The PicoCalc includes a built-in serial converter. For serial debugging, connect a USB Type-C cable directly to the PicoCalc instead of using the Pico Probe's UART debug probe.

---
  
# Conclusion
By following this guide, you can significantly enhance your PicoCalc development experience, saving time and effort while enjoying the full potential of the Pico Probe's debugging capabilities.