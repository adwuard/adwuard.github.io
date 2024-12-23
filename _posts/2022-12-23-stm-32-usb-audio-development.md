---
title: "USB Multi-Channel Microphone: STM32 USB Stack Development"
excerpt: "This is a detail guide, and debug process for my development process of my USB Mic Array Project. Exploring the USB UAC Device Stack of STM32 Processors."
date: 2022-09-01
comments: true
tags:
    - Audio
    - DSP
    - STM32
    - MCU
    - USB Development
    - USB Device
    - ARM
---

> This document details the development process and debugging journey of my USB Microphone Array Project. It explores the intricacies of the USB Audio Class (UAC) device 
stack on STM32 processors.

*** Please note that this documentation is not a structured guide for solving specific problems. Instead, it offers a glimpse into my development process, outlining the challenges and solutions encountered while implementing multi-channel microphone arrays on the STM32 platform.


<img src="/images/projects/mic_array/1.jpg" style="width:50%;">

Project Detail ---> [![Project](https://img.shields.io/badge/USB_Mic_Array_Project-blue?style=for-the-badge)](/projects/USB%20Mic-Array%20for%20Rapid%20Prototyping/)   


---

# STM32 USB Audio
## USB Device Library Interface Structure
![Untitled](/images/posts/2022-12-23-stm-32-usb-audio-development/Untitled.png)

## Audio Class Implementation

- The driver also supports basic Audio Control requests. To keep the driver simple, only two
requests have been implemented. However, other requests can be supported by slightly
modifying the audio core driver.
- The Audio transfers are based on isochronous endpoint transactions. Audio control
requests are also managed through control endpoint (endpoint 0).
In each frame, an audio data packet is transferred and must be consumed during this frame
(before the next frame). The audio quality depends on the synchronization between data
transfer and data consumption. This driver implements simple mechanism of
synchronization relying on accuracy of the delivered I2S clock. At each start of frame, the

The Audio transfers are based on isochronous endpoint transactions. Audio control
requests are also managed through control endpoint (endpoint 0). In each frame, an audio data packet is transferred and must be consumed during this frame (before the next frame). The audio quality depends on the synchronization between data transfer and data consumption. This driver implements simple mechanism of synchronization relying on accuracy of the delivered I2S clock. At each start of frame, the driver checks if the consumption of the previous packet has been correctly performed and aborts it if it is still ongoing. To prevent any data overwrite, two main protections are used:
• Using DMA for data transfer between USB buffer and output device registers (I2S).
• Using multi-buffers to store data received from USB.
Based on this mechanism, if the clock accuracy or the consumption rates are not high enough, it will result in a bad audio quality. This mechanism may be enhanced by implementing more flexible audio flow controls like USB feedback mode, dynamic audio clock correction or audio clock generation/control using SOF event.

### USBD_ADUIO Driver

This driver uses an abstraction layer for hardware driver (i.e. HW Codec, I2S interface, I2C
control interface...). This abstraction is performed through a lower layer (i.e.
usbd_audio_if.c) which you can modify depending on the hardware available for your
application.

**Implementing USBD Audio Driver**

1. Configure the audio sampling rate (define `USBD_AUDIO_FREQ`) through the file
`usbd_conf.h`,
2. Call the `USBD_AUDIO_Init()` function at startup to configure all necessary firmware
and hardware components (application-specific hardware configuration functions are
also called by this function). The hardware components are managed by a lower layer
interface (i.e. `usbd_audio_if.c`) and can be modified by user depending on the
application needs.
3. The entire transfer is managed by the following functions (no need for user to call any
function for out transfers): – `usbd_audio_DataIn()` and `usbd_audio_DataOut()` which update the audio buffers with the received or transmitted data. For Out transfers, when data are received, they are directly copied into the audiobuffer and the write buffer (wr_ptr) is incremented.
4. The Audio Control requests are managed by the functions USBD_AUDIO_Setup() and
USBD_AUDIO_EP0_RxReady(). These functions route the Audio Control requests to
the lower layer (i.e. usbd_audio_if.c). In the current version, only SET_CUR and
GET_CUR requests are managed and are used for mute control only.

**Known Limitations:**

- If a low audio sampling rate is configured (define USBD_AUDIO_FREQ below 24 kHz)
it may result in noise issue at pause/resume/stop operations. This is due to software
timing tuning between stopping I2S clock and sending mute command to the external
Codec.
- Supported audio sampling rates range from 96 kHz to 24 kHz (non-multiple of 1 kHz
values like 11.025 kHz, 22.05 kHz or 44.1 kHz are not supported by this driver). For
frequencies multiple of 1000 Hz, the Host will send integer number of bytes each frame
(1 ms). When the frequency is not multiple of 1000Hz, the Host should send non
integer number of bytes per frame. This is in fact managed by sending frames with
different sizes (i.e. for 22.05 kHz, the Host will send 19 frames of 22 bytes and one
frame of 23 bytes). This difference of sizes is not managed by the Audio core and the
extra byte will always be ignored. It is advised to set a high and standard sampling rate
in order to get best audio quality (i.e. 96 kHz or 48 kHz). Note that maximum allowed
audio frequency is 96 kHz (this limitation is due to the Codec used on the Evaluation
board. The STM32 I2S cell enables reaching 192 kHz).



### USB Audio States
Different states triggers I2S DMA interrupt and USB DMA transfer to start/stop. Implement DMA callbacks and handle audio data.
```c
//  States:
  // AUDIO_CMD_START 0x01 Audio player is initialized and ready.
  // AUDIO_CMD_PLAY 0x02 Audio player is currently playing.
  // AUDIO_CMD_STOP 0x04 Audio player is stopped.
```

### USB Control Transfer Functions

**Device reset**
When the device receives a reset signal from the USB, the library resets and initializes both
application software and hardware. This function is part of the interrupt routine.

**Device suspend**
When the device detects a suspend condition on the USB, the library stops all the ongoing
operations and puts the system in suspend state (if low power mode management is
enabled in the usbd_conf.c file).

**Device resume**
When the device detects a resume signal on the USB, the library restores the USB core
clock and puts the system in idle state (if low power mode management is enabled in the
usbd_conf.c file).

## STM32 USB Stack files and source code explained. 

- `usbd_core (.c, .h)`  This file contains the functions for handling all USB communication and state machine.
- `usbd_req(.c,.h)`  This file includes the requests implementation listed in Chapter 9 of the specification.
- `usbd_ctlreq(.c,.h)` This file handles the results of the USB transactions.
- `usbd_conf_template(.c,.h)` Template file for the low layer interface file, should be customized by user and included with application file.
- `usbd_def(.c, .h)` Common library defines
- `usbd_audio (.c, .h)` This driver is the audio core. It manages audio data transfers and control requests. It does
not directly deal with audio hardware (which is managed by lower layer drivers).
- `usbd_audio_if (.c, .h)` This driver manages the low layer audio hardware. usbd_audio_if.c/.h driver manages the
Audio Out interface (from USB to audio speaker/headphone). user can call lower layer
Codec driver (i.e. stm324xg_eval_audio.c/.h) for basic audio operations (play/pause/volume
control...).


## Steps for Developing USB Audio on STM32: "The Pipeline Flow"
Here's a breakdown of the steps involved in developing a USB audio application on an STM32 microcontroller:

###  1. Initiation of Audio Stream:
- Once the host sets the USB command audio streaming interface to "1," the STM32 device begins transmitting PCM samples.

### 2. PDM to PCM Conversion:
- A MEMS microphone generates PDM samples via the I2S channel.
- These samples are transferred to an intermediate buffer using `DMA`.
- The PDM library converts the PDM samples into PCM samples.
- The application writes these PCM samples to a recording circular buffer.

### 3. Data Request and Transmission:
- Every millisecond, the host requests a USB data packet from the recording endpoint.
- The application copies one data packet into the USB FIFO.
- The STM32 USB IP transmits the data to the host.

### 4. Data Synchronization and Zero Padding:
- Depending on data synchronization, the application might send slightly more or less than one sample.
- If no data is ready for transmission, the application sends a zero-padded packet.

## USB Capture and Playback Lifecycle and Call Stack
### USB Audio Record Start Event Flow
following srquence diagram shows the flow on capture audio streaming.
![Untitled](/images/posts/2022-12-23-stm-32-usb-audio-development/Untitled%201.png)

### Audio Playback Start Event Flow
following srquence diagram shows the flow on playback audio streaming.
![Untitled](/images/posts/2022-12-23-stm-32-usb-audio-development/Untitled%202.png)



# USB Descriptors - Packet Size
Now the macros. Add `AUDIO_IN_EP` and `MIC_PACKET_SZE` to the *usbd_audio.h* file:
```
#define AUDIO_IN_EP            0x81U
#define MIC_PACKET_SZE(frq)    (uint8_t)(((frq * 1U * 2U)/1000U) & 0xFFU), \
                               (uint8_t)((((frq * 1U * 2U)/1000U) >> 8) & 0xFFU)
```

`AUDIO_IN_EP` is endpoint #1, having the `IN` direction. `0x81` is equal to `10000001` in binary, and the MSB here is set to 1, indicating the `IN` direction of the endpoint. First 4 bits contain the number of the endpoint, which is 1.

`MIC_PACKET_SZE` defines the packet size, derived from the sample frequency, number of channels and the bit depth. It also splits the result into two 8-bit values since the descriptor bit fields are 8-bit (so is the array, containing the descriptor). USB FS sends packets at the 1 kHz rate, and we should specify how much audio data should be sent in one such transfer. This yields us the formula to calculate this value:

```
wMaxPacketSize = (fs * Ch * bit) / 1000 Hz
```
where:
- fs — sampling frequency in Hz
- Ch — number of audio channels 
- bit — bit depth in bytes


---


# Analyzing and Debugging ISOC USB Packets

Wireshark is an invaluable tool for analyzing USB packets, especially when dealing with the intricacies of Isochronous (ISOC) transfers. By examining asynchronous packets within an ISOC stream, developers can gain crucial insights into:

- Data Streaming Robustness: Identifying potential data loss, jitter, or other anomalies that might disrupt the smooth flow of audio data.
- USB Transfer Timing: Analyzing the precise timing of packet transmissions to ensure they meet the stringent requirements of real-time applications.
This analysis helps developers pinpoint and resolve issues related to data integrity and timing, ultimately leading to a more reliable and efficient USB audio implementation.

![Untitled](/images/posts/2022-12-23-stm-32-usb-audio-development/Untitled%203.png)


---

# References
[STM32-USB Device Library Doc](https://www.st.com/resource/en/user_manual/um1734-stm32cube-usb-device-library-stmicroelectronics.pdf)

[Hackaday.io-stm32f4-usb-microphone](https://hackaday.io/project/181868-stm32f4-usb-microphone/details)

[Introduction to USB with STM32](https://wiki.st.com/stm32mcu/wiki/Introduction_to_USB_with_STM32)

[STM32 USB FS Reference Manual](https://www.aimagin.com/pub/media/bss/productattachment/stm32f417ig_reference_manual-2.pdf)