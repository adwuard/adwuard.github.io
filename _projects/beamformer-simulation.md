---
title: "Design Beamforming Mic Array "
excerpt: "Discover the fundamentals of designing a beamforming microphone array with this comprehensive guide. Learn how to simulate beamforming using Matlab, explore various microphone array configurations. <br/><img src='/images/projects/beamforming/1.png' width='350'>"
collection: projects
date: 2023-06-01
tags:
    - Mic Array 
    - Beamforming
    - Simulation
    - Matlab
    - Audio Projects
    - DSP
    - Signal Processing
    - Resource
---

If you're just diving into the world of mic array [beamforming](https://en.wikipedia.org/wiki/Beamforming) and want to learn how to simulate it using Matlab, you're in the right place! 


Andrea Vitali has written an excellent [design guide]((https://www.st.com/resource/en/application_note/an4426-digital-mems-microphones-in-beamforming-applications-stmicroelectronics.pdf)) that explains how to combine signals from multiple omnidirectional microphones to create a virtual microphone that captures sound from a specific direction while rejecting sounds from other directions. This technique is known as beamforming. Here's a breakdown of the key points from the guide:

# Introduction
[MEMS microphones](https://www.st.com/en/mems-and-sensors/mems-microphones.html) typically capture sound from all directions, which is great for some applications but not ideal when you want to focus on a specific sound source. To achieve directionality, you can arrange multiple omnidirectional microphones in specific configurations. 



### Common Mic Patterns
In addition to the Additive and Differential Microphone Arrays, there are several other common microphone array patterns used in beamforming:

- **Uniform Linear Array (ULA)**: This configuration arranges microphones in a straight line with equal spacing between them. It is simple to implement and commonly used for its straightforward geometry and ease of analysis.
  - **Additive Microphone Array (AMA)**: Also called the "broadside" configuration, this array captures broadband sound arriving from the side of the microphone line. This setup involves two microphones spaced D millimeters apart, with their outputs simply added together. It captures sound from ±90 degrees and rejects sound from 0 and 180 degrees at specific frequencies.
  - **Differential Microphone Array (DMA)**: Also known as the "endfire" configuration, this array captures sound arriving from the ends of the microphone line.
    - **First-Order Differential Microphone Array (DMA) Endfire Configuration**: Here, two microphones are spaced D millimeters apart, with the output of the second microphone subtracted from the first. This configuration rejects sound from ±90 degrees and captures sound from 0 and 180 degrees at specific frequencies.
    - **Second-Order Differential Microphone Array (DMA) Endfire Configuration**: This more complex setup further enhances directionality and frequency selectivity.
- **Uniform Rectangular Array (URA)**: Microphones are arranged in a rectangular grid pattern. This setup allows for more complex beamforming capabilities and can capture sound from multiple directions.
- **Uniform Circular Array (UCA)**: Microphones are placed in a circular pattern with equal spacing. This configuration provides 360-degree coverage and is useful for applications requiring omnidirectional sound capture.
- **Concentric Circular Array**: Multiple circular arrays with different radii are used to enhance directionality and frequency selectivity. This setup can provide more precise beamforming capabilities. But this usually requires more mics. Hardware gets expensive quickly.

These patterns offer various advantages depending on the specific application and desired beamforming characteristics.


# Simulation and Validation
**Code：**
[![GitHub](https://img.shields.io/badge/GitHub-BF_Simulate-blue?
logo=github&style=for-the-badge)](https://github.com/adwuard/bf-simulate)   

<img src='/images/projects/beamforming/1.png' style="width:80%">  
   
Matlab code examples to validate the performance of different configurations. For instance:
- **BFtest.m**: Configures variables and runs simulations.
  ``` matlab
  % run ONE of the following lines
  % BFtype=0; Nmic=2; D=0.03; Ts=1/48e3; NT=0; % broadside configuration
  BFtype=1; Nmic=3; D=0.015; Ts=1/48e3; NT=0;  % 1st ord end-fire, Dipole
  % BFtype=1; Nmic=2; D=0.004; Ts=0; NT=0; % 1st ord end-fire, Dipole
  % BFtype=1; Nmic=2; D=0.0214; Ts=1/16e3; NT=1; % 1st ord end-fire, Cardioid 16kHz PCM
  % BFtype=1; Nmic=2; D=0.0071; Ts=1/48e3; NT=1; % 1st ord end-fire, Cardioid 48kHz PCM
  % BFtype=1; Nmic=2; D=0.004; Ts=1/1.024e6; NT=12; % 1st ord end-fire, Cardioid 1.024MHz PDM
  % BFtype=1; Nmic=3; D=0.004; Ts=1/1.024e6; NT=12; % 2nd ord end-fire, Cardioid 1.024MHz PDM
  % then run the configuration utility (config=0 makes it interactive)
  config=1; % 1 if vars are set here: BFtype(0-1), Nmic(1-8), D[m], Ts[s] and NT
  BFconfig; % set position, weight and time delay of each microphone
  % run ANY of the desired simulation scripts
  BFsim2D; % 2D sim with planar/circular wavefronts at given frequency
  BFsim3D; % 3D sim with circular wavefronts at given frequency
  BFsimAF; % 2D sim, plot of intensity vs angle of arrival vs frequency
  BFsimAFc; % 2D sim, same as BFsimAF but plots a ring instead of a plane
  %%%% BFsimA3; % 3D sim, intensity vs angle of arrival at given frequency
  ```
- **BFsim2D.m**: Simulates sound intensity distribution in a 2D plane.
- **BFsimAF.m**: Simulates sound intensity distribution at different frequencies and angles of incidence.




### Conclusion
When designing a beamforming microphone array, key factors to consider include **microphone spacing**, **sampling rate**, **sensitivity** and **directivity** characteristics of the microphones. These parameters significantly impact the array's performance.

By adjusting the spacing between microphones and applying appropriate time delays, various beamforming effects can be achieved. The guide offers detailed parameter settings and validation methods for practical applications, making it an invaluable resource for beginners and experienced practitioners alike.

Happy simulating!


## Extending Topics of Beamforming
These topics provide deeper insights and practical approaches to advanced beamforming applications.
- **DOA (Direction of Arrival)**: Techniques to estimate the direction from which a sound source is arriving.
  - **Phase and Correlation-Based Methods**: Techniques that utilize phase differences and correlation between microphone signals to enhance beamforming accuracy and robustness.
- **Adaptive Beamforming**: Methods to dynamically adjust the beamforming pattern based on the environment and signal conditions.
- **Localization and Tracking**: Implementing Kalman filtering and particle filtering approaches to accurately locate and track sound sources.
- **Real-time Optimization**: Strategies for optimizing calculations to achieve low-latency processing in real-time applications.

These advanced topics can significantly improve the performance and versatility of beamforming systems, making them suitable for a wide range of applications, from consumer electronics to professional audio equipment.


# Resources
Here are some additional resources that I used in learning and designing the beamformer:

## Hardware
- **USB Mic-Array for Rapid Prototyping**: A hardware solution I designed to accelerate the prototyping process of microphone arrays. [Learn more](/projects/USB%20Mic-Array%20for%20Rapid%20Prototyping/)

## Books
  - **Microphone Array Signal Processing** by Jacob Benesty， Jingdong Chen， Yiteng Huang · 2008
  - **Springer Handbook of Speech Processing** by Jacob Benesty， M. M. Sondhi， Yiteng Huang
  - **Digital Speech Transmission- Enhancement, Coding and Error Concealment** by Peter Vary， Rainer Martin · 2006

## Python Repos
- **[pyroomacoustics](https://github.com/LCAV/pyroomacoustics)** - Pyroomacoustics is a package for audio signal processing for indoor applications. It was developed as a fast prototyping platform for beamforming algorithms in indoor scenarios.
- **[Acoular](https://github.com/acoular/acoular)** - Acoustic testing and source mapping software

- **[Beamforming-for-speech-enhancement](https://github.com/AkojimaSLP/Beamforming-for-speech-enhancement)** - a series of simple implementations (DSB, MVDR and CGMM-MVDR) for speech enhancement.

## Other:
  - **STMicroelectronics Application Notes**: [AN4426 - Digital MEMS Microphones in Beamforming Applications](https://www.st.com/resource/en/application_note/an4426-digital-mems-microphones-in-beamforming-applications-stmicroelectronics.pdf)
  - **Matlab Documentation**: [Matlab Array Processing Toolbox](https://www.mathworks.com/help/phased/beamforming.html)
  - **IEEE Xplore Digital Library**: [Research Papers on Beamforming](https://ieeexplore.ieee.org/Xplore/home.jsp)

