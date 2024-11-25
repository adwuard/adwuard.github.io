---
title: "USB Mic-Array for Rapid Prototyping"
excerpt: "Discover how a modular USB mic array can streamline the development of audio hardware and algorithms. Ideal for rapid prototyping with low-latency audio streaming and flexible design options.<br/><img src='/images/projects/mic_array/1.jpg' width='350'>"
collection: projects
date: 2023-08-24
tags:
  - Speech Processing
  - Speech Recognition
  - Hardware Design
  - USB Development
  - USB UAC 1.0
  - STM32
  - Low-Latency Audi
---

# Overview
When building a smart audio product, a mic array is often needed to offer better performance and audio enhancements such as beam-forming algorithms to improve far-field audio pickup.

Designing new mic array hardware and new algorithms is challenging. Microphones usually use PDM and I2S interfaces and are connected directly to hardware SoCs or MCUs. Getting a real-time stream for rapid algorithm development is hard.

# Problems when developing new mic array hardware and algorithms

When designing new mic arrays and algorithms, deploying algorithms into SoCs/MCUs often involves cross-compiling and a more complicated debugging workflow when dealing with real-time audio.

```text
Audio DSP on SoCs or MCU is hard to debug: 
Multi-Channel PDM Mics -> I2S -> SoCs [processing] -> Enhanced Audio
```

A better approach for rapid algorithm development is to gain access to raw audio and rapidly develop audio projects in Python, C/C++, or Matlab, which offer a lot more visualization and debugging capabilities.

```text
At Audio Interface, ensuring low latency raw audio streams to PC:
Multi-Channel PDM Mics -> I2S -> MCU -> USB [Raw Audio] -> PC 

At PC, algorithm prototyping and debug visualization made easy:
PC -> Python/Matlab/C/C++
```

This is why creating a modular USB mic significantly simplifies the prototyping process.
<img src='/images/projects/mic_array/1.jpg'/>

## What’s Also Available on the Market?
### ~~1. Multi-Channel Audio Interfaces~~
**Cons:**
- Uses analog signals, making it impossible to test with digital microphones.
- Often requires ASIO drivers, which are cumbersome to use on Linux or Windows, especially when accessing from Python or Matlab.
- Can become expensive as the channel count increases.

### ~~2. XMOS ASIC IC Solutions~~
**Pros:**
- Supports a wide variety of digital audio interfaces.
- Provides rapid and custom solutions for various audio products.
**Cons:**
- Limited availability, with potential production issues due to MOQs and long lead times.
- Requires the proprietary XDC IDE, which can be difficult to set up and develop with.

---
## Why These Market Solutions Don't Fit My Needs

I need a microphone that is:

- **Cost-effective and widely available:** Utilizing STM32.
- **Plug-and-play:** A USB microphone that complies with UAC and streams directly to a PC.
- **Ultra-low latency:** Ensuring minimal delay in audio transmission.
- **PDM audio interface:** Allowing testing of different MEMS microphones. Swapping mic modules should be easy.
- **Phase-correct sampling:** Essential for building beamforming algorithms. Ensuring hardware trace length, clocking, buffering, and USB transmission are sample-aligned and phase-correct.
- **Modular design:** Enabling the creation of different adapter boards to experiment with various mic array arrangements and mechanical designs.
- **High sampling rate:** Offering 48KHz and 16KHz sampling rates, which are sufficient for most real-time speech processing applications.

# The Design
System Diagram:  
<img src='/images/projects/mic_array/system-diagram.jpg'/>

`Adapter board` and `swappable PDM mics` can easily be transformed into different shapes and arrangements, allowing for quick PDM mic testing.
<div style="display: flex; justify-content: space-around;">
    <img src='/images/projects/mic_array/7.jpg' style="height: 250px;"/>
    <img src='/images/projects/mic_array/8.jpg' style="height: 250px;"/>
</div>

The assembly:
<div style="display: flex; justify-content: space-around;">
    <img src='/images/projects/mic_array/6.jpg' style="height: 250px;"/>
    <img src='/images/projects/mic_array/5.jpg' style="height: 250px;"/>
</div>

---
# What I Learned
### Why Does My Digital Mic Sound Noisy? Use LDO Power Regulators for Low Noise!
- During hardware development, I noticed that my mic samples were noisy and didn't meet the data sheet's specifications. I discovered that this was due to using a shared DC-DC regulator with the MCU, which caused switching noises under higher loads.
- After revising the hardware design and implementing a dedicated LDO for the mic, along with ensuring a good ground plane and decoupling capacitors, the audio noise floor dropped significantly.
- Bottom Line: Although digital mics are less susceptible to noise compared to analog ones, they still require good power and analog design techniques to minimize ADC noise.

### New to Audio Hardware Protocols. Learning `I2C`, `PDM`, and STM32 `SAI` Interfaces
- Gaining knowledge in these protocols helped me understand how raw audio transfers over hardware interfaces, clocking requirements, and how different hardware interfaces can be related or converted. This knowledge will enable me to create more complex audio projects and optimize audio hardware designs and chip selection in the future.

### First STM32 Project, Understanding MCUs
- Without prior experience with STM32 and MCUs, it took some time to grasp how MCUs work, including:
    - Hardware protocol interfaces and register manipulations, and how to create drivers for different protocols.
    - Types of NVIC interrupts, their relationship to software and hardware interfaces, and how to use them effectively for project needs.
    - System clock management.
    - Debugging processes and techniques.
- Overall, completing this project helped me connect the dots from my operating systems class in college. The relationship between hardware and software is much clearer now, and this level of understanding is something I wouldn't have achieved while developing with some even more complex OS such as Linux kernel or Linux drivers.

### Complex clocking. Ensuring Low-Latency Raw Audio Streams
To guarantee low-latency raw audio streams from the microphone to the PC via USB, it is crucial to ensure accurate sampling frequency (clocking) of the codec. Reducing sampling frequency errors can be achieved by improving the clocking accuracy of the codec.

- **DMA Buffer Timing:** The DMA buffer timing and STM32 USB interface should be DMA mapped and triggered with an accurate timer. This reduces frame loss issues and provides a better low-latency raw stream.
- **Trace Length Consistency:** If your design includes widely spread microphones, ensure all PDM mics have identical clock/data trace lengths. This will minimize data errors.

### Comply to USB UAC 1.0
Although STM32 provides UAC middleware with a demo for 1 mic and 1 speaker, significant optimizations are required for multi-channel support. The STM32 USB controller operates at USB 2.0 FS (12Mbps).

```
Bandwidth: 12Mbps
Audio Data Size: 48000 (Fs) * 8 (channels) * 2 (16-bit) = 7.68 Mbps
Approximately 64% of the available bandwidth is used.
```

USB asynchronous audio data packets consume 64% of the bandwidth. In practical terms, the actual average throughput can vary based on the nature of the data, specific devices, and environmental factors. For most consumer devices under typical conditions, achieving around 70-85% of the theoretical maximum is reasonable for USB 1.1 Full Speed. **This nearly maxes out the STM32's USB bandwidth, necessitating extensive optimization of asynchronous transfer and timing to ensure smooth, uninterrupted audio.**

Additionally, the STM32's UAC middleware lacks support for several optional but important features such as USB Feature Unit (FU), Sampling Rate Converter Unit (RU), volume control, mute functionality, sampling rate options, and filter features. While these are optional in the UAC protocol, they are essential for practical use cases and need to be implemented.

## Technologies and Tools Used
- Hardware:
    - STM32, ARM, MCU, I2S, I2C, PDM,
    - Hardware design (EE and ME)
    - Altium Design: for schematic design, layout, BOM, and fabrication.
- Software:
    - Implemented codec driver
    - USB device protocol UAC/HID compliance, and emulation
    - Low latency audio pipelining