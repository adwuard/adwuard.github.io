---
title: "Microphone Array Testing and Performance Evaluation"
excerpt: "Explore detailed methods and conditions for testing microphone arrays, including sensitivity, frequency response, and advanced AI speech enhancement. This guide offers insights into optimizing microphone array performance for various applications."
date: 2022-09-01
comments: true
tags:
    - Audio Testing
    - Speech Quality
    - DSP
    - Audio Standards
    - Speech Processing
    - Testing
    - Algorithm
    - Audio Lab
    - Microphone Array
---

Hey folks! If you're into smart devices, you know how crucial microphones and microphone arrays are for wake-up and recognition features. This guide is here to help you evaluate microphone arrays performance. We'll cover everything from measurement methods to key metrics for both individual mics and arrays, all aimed at boosting your product design and algorithm performance.


After reading my previous post, you will understand how to set up the environment and adhere to industry standards for testing.
[A Guide to Audio Testing, Automation, and Standards](/guide-to-audio-testing-and-standards/)

--- 

> This guide will provide hands-on testing with a Mic-Array System.


Microphone arrays are everywhere – in robots, TVs, air conditioners, and smart speakers. This guide focus on the testing enclosed product device.

- The cavity affects both the array and individual mics. Start by measuring individual mic performance, including sensitivity, frequency response, distortion, noise floor, and cavity sealing.
- The array's overall performance hinges on the individual mics' performance and installation. Look at frequency response consistency, delay, correlation, and phase consistency.
- Basic algorithm tests (DOA, AEC) help verify some performance aspects of the mic array.

# **2. Terms and Definitions**

| **Term** | **Definition** |
| --- | --- |
| Sensitivity | The mic's output voltage ratio to the sound pressure at a specified position, noted as S. |
| Equivalent Noise Level | The mic's inherent noise without any sound waves, usually measured with A-weighting. |
| Signal-to-Noise Ratio (SNR) | The ratio of the target signal's energy to the noise signal in the mic output. |
| Frequency Response (FR) | The curve showing how mic sensitivity changes with frequency. |
| Frequency Response Consistency | The frequency response difference between channels in a mic array. |
| Total Harmonic Distortion (THD) | The ratio of harmonic content to the total voltage in the mic's output. |
| Delay Consistency | The delay difference between channels in a mic array. |
| Channel Correlation | The correlation degree between signals of any two channels in a mic array. |
| Phase Consistency | The phase deviation between channels in a mic array. |
| Sealing | Tests for internal and external sealing by comparing sound pressure levels with and without the audio hole blocked. |
| Clipping | The sound pressure level at which the mic clips when playing audio. |
| Reverberation | The time or EDT value compared with real data to analyze reverberation introduced during signal collection. |
| Microphone Array Data Integrity | Ensuring the mic array's data is valid, accurate, and not lost.

# **3. Measurement Conditions and Methods**

## Measurement Conditions

For accurate results, ensure the mic is working under these conditions:

- Standard atmospheric conditions: 15-35℃, 25%-75% humidity, 86kPa~106 kPa air pressure.
- Rated power supply if needed.
- Place the mic in a free field with sound waves at a 0° angle to the reference axis.
- Use a sinusoidal sound pressure level of 1Pa (94 dBSPL) at the reference point.
- Keep background noise low (< 40dBSPL) and minimize room reverberation.

## Measurement Methods

Preheat the microphones with preamplifiers according to the manufacturer's instructions. Ensure that the nonlinearity influence of the sound source is below 0.5dB. If necessary, use a narrowband filter to measure only the fundamental frequency response.

Position the reference speaker 1 meter from the microphone, with the distance adjustable as needed. Calibrate the reference speaker's output frequency response using a standard microphone, then measure the performance of the test microphone. Use various signals such as sine waves, logarithmic sweeps, and white noise depending on the test requirements.

Room specifications:
- Size: 3.5m x 3.5m
- RT60 Time: 200ms ± 20ms

Install the microphone array on a rotating platform to test performance from different directions.

## Measurement Equipment

- Sound Level Meter: Measures sound pressure level at the device's mic.
- Tape Measure: Measures test distance and angle.
- Laptop: Plays test audio.
- Device Stand: Ensures the position and height of test and playback equipment.
- Reference Speaker: Audio equipment.

# **Measurements and Method**

### Sensitivity

Play a 1kHz sine signal and measure the mic's output voltage ratio to the sound pressure at the calibration position (1kHz, 1Pa (94dBSPL)).

### Equivalent Noise Level

Without any sound, collect audio and calculate the A-weighted equivalent noise level. If the mic's sensitivity is unknown, use the noise level to measure this parameter.

### Signal-to-Noise Ratio (SNR)

Measure the ratio of the mic's 1kHz sensitivity to its inherent noise (A-weighted).


### Enclosed Microphone Frequency Response

Test mic with product enclosure and acoustic cavity.

Play a logarithmic sweep signal from 20 to 20kHz and measure the mic's output sound pressure level. Calculate the frequency response curve and compare it with the standard curve to ensure it meets the required specifications.


### PCB Board only Microphone Frequency Response

If the whole device mic frequency response doesn't meet the standard, remove the acoustic cavity and measure the bare board mic's frequency response.

### Microphone Array Frequency Response Consistency

Play a logarithmic sweep signal from 20 to 20kHz and calculate the mean error of each frequency point. Provide the consistency curve between array channels.

### Total Harmonic Distortion (THD)

Play a 1kHz sine signal and calculate the total harmonic distortion at 1kHz.

### Delay Consistency

Play white noise and calculate the delay difference between channels. Provide the delay difference curve.

### Microphone Array Channel Correlation

Play white noise and calculate the correlation between each pair of channels in a 1-2 minute audio file. Provide the correlation curve.

### Microphone Array Phase Consistency

Play white noise and provide the phase curve of each channel.

### Microphone External Sealing Test

Block the mic's sound inlet hole with soundproof sealing glue. Play a logarithmic sweep signal from 20 to 20kHz and measure the mic's output sound pressure level.

### Microphone Array Data Clipping

Play white noise and adjust the playback signal sound pressure level to determine if each channel clips. Provide the clipping sound pressure level.

### Reverberation Introduction Analysis

Play a logarithmic sweep signal from 20 to 20kHz and calculate the reverberation time or EDT.

### Microphone Array Data Integrity and Long-Term Stability

Conduct long-term tests to evaluate the microphone array's stability over time. Measure the performance metrics periodically and provide the trend analysis.

### Microphone Array's MIC Channel Correlation

Play white noise echo and calculate the correlation between the MIC channel and the reference channel in a 1-2 minute audio file.

### Microphone Array's MIC Channel Phase Consistency

Play white noise echo and calculate the phase difference or delay between the MIC channel and the reference channel.

--- 
# Additional Tests to Consider
As AI systems become more complex, it's important to understand how AI module performance relates to raw signal performance. You may want to create custom test cases to gain a better understanding of the relationship between raw acoustic performance and AI performance.

### AI Speech Enhancement

Test the AI's ability to enhance speech by comparing raw audio input to AI-enhanced audio output. Measure algorithm latency and evaluate performance using real speech signals, MOS (Mean Opinion Score), and POLQA (Perceptual Objective Listening Quality Analysis) scores.

### Sound Source Localization Test (DOA)

Stand at various positions or play white noise within the array's range. Use a localization demo to calculate and provide the localization trend and localization output.

### Echo Cancellation Test (AEC)

Play white noise or sweep signals through the device's speaker. Obtain the microphone and reference channel outputs and use an AEC demo to provide the echo cancellation effect and convergence curve.


### Beamforming (BF)

Test the mic array from different angle, and with beamforming algorithm enabled, test and see 
if the beamforming algorithm can effectively isolate the sound source. Measure the signal-to-noise ratio (SNR) improvement and provide the beamforming pattern.

### Keyword Spotting (KWS)

Test the KWS algorithm by playing a set of predefined keywords and non-keyword audio. Measure the detection accuracy, false acceptance rate, and false rejection rate.

### Far-Field Performance

Test the microphone array's performance at different distances (e.g., 1m, 3m, 5m) from the sound source. Measure the SNR, speech recognition accuracy, and other relevant metrics to assess far-field capabilities.

### Multi-Talker Scenario

Evaluate the microphone array's performance in scenarios with multiple talkers. Measure the ability to separate and recognize individual voices and provide the separation and recognition accuracy.

### Environmental Robustness

Test the microphone array in various environmental conditions (e.g., different temperatures, humidity levels, and air pressures). Measure the performance stability and provide the results for each condition.


# Conclusion

This guide has provided a detailed overview of microphone sensitivity, frequency response, and advanced AI speech enhancement testing. Remember, there is no one-size-fits-all testing sequence. Customize your testing approach to address specific areas for improvement. Focus on the aspects you want to enhance and then measure them accordingly.


