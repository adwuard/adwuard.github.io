---
title: "A Guide to Audio Testing, Automation, and Standards"
excerpt: "Discover essential tips, tools, and industry standards for testing audio/speech systems and evaluating speech quality. Based on my experience with speech audio hardware products, this guide provides valuable insights into overcoming common challenges in audio testing and automation."
date: 2022-08-12
comments: true
tags:
    - Audio Testing
    - Speech Quality
    - DSP
    - Audio Standards
    - CI/CD
    - Speech Processing
    - Testing
    - Algorithm
    - AEC
---
When I was working on speech audio hardware products, I came across the challenge of testing audio and having metrics on the speech processing DSP. Here are some insights and tips based on my experience.

## Challenges in Audio Algorithm and Hardware Development

Working in speech algorithm and hardware development has both fascinating and challenging journey. It comes with its fair share of challenges. Ensuring that audio quality meets industry standards while being practical for real-world applications. Let me share some of the obstacles I've faced and how I've managed to overcome them.

### The Struggle with Consistency
Maintaining consistency across different environments has been one of the main challenges I've faced. Audio systems can behave differently in a controlled lab setting compared to a noisy office or a bustling street. To address this, I set up a variety of testing environments, ranging from anechoic chambers to more realistic settings like meeting rooms. This approach has helped me understand how my system performs in different scenarios and make necessary adjustments. Additionally, developing adaptive algorithms that can adjust to these varying conditions has been crucial in ensuring consistent performance across different environments. 

### The Quantify of Metrics
Maintaining a comprehensive set of metrics is crucial for evaluating audio systems, but it can be overwhelming at first. I found that focusing on the most relevant metrics for my goals made a significant difference. For instance, when prioritizing speech clarity, I concentrated on metrics like MOS and POLQA. By narrowing my focus, I made the process more manageable and effective. Clearly defining my goals and knowing what I wanted to improve was key. 

### Automation to the Rescue
Manual testing can be incredibly time-consuming and prone to errors. This is where automation has been a game-changer for me. By integrating CI/CD pipelines with automated audio tests, I've streamlined the testing process. Setting up CI to run tests automatically whenever there's a code change has ensured that any issues are caught early, saving me a lot of time and effort. 

### Constant Learning Process: The New AI Approach
At my line of work, we are continuously experimenting with innovative AI techniques for speech noise suppression and echo cancellation. Our focus is on achieving superior performance in dynamic environments, particularly in non-stationary noise cancellation. Additionally, we are exploring effective metrics for analyzing AI-powered DSP systems to ensure optimal performance.

### Working on New Hardware Projects
Starting new hardware projects provides hands-on experience and a deeper understanding of audio systems. Whether designing a new microphone array, developing a custom audio analyzer, or creating a portable testing rig, these projects help apply theoretical knowledge to practical scenarios. Documenting projects and sharing findings with the team or community also contributes to the collective knowledge in the field.

> Note: 
This article assumes that you have already properly designed your hardware, managed hardware noise, optimized hardware audio port enclosure design, and ensured mic port air-tight sealing. 
Hardware design is a topic of its own. Today, we will focus on acoustic testing, metrics, and automation.

--- 

## How Do I Test an Audio System?
Testing an audio system might seem overwhelming at first, but breaking it down into simple steps can make it much more manageable. Here’s a straightforward approach to get you started:

1. **Define Your Goals**: What exactly are you trying to test? Are you focusing on speech clarity, background noise suppression, overall audio quality, or codec performance over Ethernet? Each of these requires a different testing setup. Follow the recommendations below to see how to set up different testing loops for various scenarios.

2. **Choose the Right Tools**: Select appropriate tools for your audio testing needs. For hardware analysis, consider using oscilloscopes and audio analyzers. For software analysis, tools that measure frequency and speech quality metrics like MOS and POLQA are useful. You can also develop custom testing and analysis algorithms.

3. **Set Up Your Environment**: Create a controlled testing environment to minimize external noise and interference, ensuring accurate and reliable results. Different environments offer varying levels of detail:
    - **Anechoic Chamber**: Provides the highest level of detail by eliminating reflections and external noise, ideal for precise measurements. Costing the most and hardest to gain access to.  
      - <img src="/images/posts/2022-08-12-guide-to-audio-testing-and-standards/2.jpg" style="width:80%;">
    - **Listening Room**: Simulates real-world conditions while controlling some variables, suitable for subjective listening tests. A meeting room, medium/small office room with proper acoustic treatment does the trick.
    - **Small Enclosed Chamber**: A metal-enclosed case with foam-padded inserts. This setup provides a controlled space with some reflections, making it useful for general testing in small spaces.  
      - <img src="/images/posts/2022-08-12-guide-to-audio-testing-and-standards/1.jpg" style="width:80%;">

    - **Uncontrolled Environment**: Testing in an uncontrolled environment can introduce noise and variability, making it less reliable but useful for quick, informal tests.
    - **Software Testing**: Algorithms and scripts can automate up to 80% of the day-to-day testing process, efficiently evaluating speech quality metrics. This allows developers to quickly assess changes on a server. The remaining 20% should still be fundamental hardware testing conducted in a controlled environment.

4. **Run Your Tests**: Perform a series of tests, such as frequency response, distortion, and signal-to-noise ratio (SNR). Additionally, evaluate speech metrics like Mean Opinion Score (MOS) and Perceptual Objective Listening Quality Analysis (POLQA).

5. **Analyze the Results**: Compare your results against industry standards to see how your system performs. This will help you identify areas for improvement.

### For Example:
### Testing Microphone Raw Audio
When testing a new microphone, whether hardware enclosed or standalone, I used an audio analyzer to measure its frequency response, Total Harmonic Distortion (THD), noise, and Signal-to-Noise Ratio (SNR). This helped identify areas where the microphone excelled and where it needed improvement, both at the hardware design level and for the microphone raw signal level. This knowledge is crucial for building better Digital Signal Processors (DSPs) for the microphones in use.

### Testing Microphone Audio System
When testing an audio system, such as `Mic->Algorithm->Sink`, it is essential to evaluate latency and speech quality metrics for continuous improvement of audio algorithms. At Vibe, we build our audio input systems with microphone arrays and AI-powered noise suppression and echo cancellation. Therefore, it is crucial to test metrics like [Mean Opinion Score (MOS)](https://en.wikipedia.org/wiki/Mean_opinion_score) and [Perceptual Objective Listening Quality Analysis (POLQA)](https://www.polqa.info/). Additionally, newer metrics like Google's [ViSQOL](https://github.com/google/visqol) offer advanced approaches for testing AI systems. Ultimately, the choice of metrics depends on the specific aspects you want to test, as each metric performs differently, with some requiring reference audio and others not, making them best suited for different scenarios.

## What Are Common Industry Standards and Metrics to Evaluate Speech Quality?

Understanding industry standards and metrics is crucial for evaluating speech quality. Here are some key standards and metrics:

- **ITU-T P.800**: Methods for subjective determination of transmission quality.
- **ITU-T P.862 (PESQ)**: Perceptual evaluation of speech quality.
- **ITU-T P.863**: Perceptual objective listening quality prediction.
- **Mean Opinion Score (MOS)**: A numerical measure of the human-judged overall quality of voice and audio.
- **ViSQOL**: Virtual Speech Quality Objective Listener, an advanced metric developed by Google for evaluating speech quality using machine learning techniques.

### Example:
Using the ITU-T P.862 standard, I was able to objectively evaluate the speech quality of a new voice codec, which provided a clear benchmark for comparison against other codecs.

## How Do Big Companies Conduct Audio Testing and Certification?
Understanding how major companies conduct their audio testing and certification processes can also provide valuable insights and help you quickly get up to speed with industry standards. Here are some examples of certification standards from leading companies:
- [Teams Certification Standard](https://learn.microsoft.com/en-us/microsoftteams/devices/certification-overview)
- [Zoom Certification Standard](https://www.zoom.com/en/hardware-as-a-service/zoom-certified/)
  - [HEAD acoustics Implements the Zoom Audio Specification as a New ACQUA Standard](https://www.head-acoustics.com/news-events/press-releases/press-details/show/head-acoustics-implements-the-zoom-audio-specification-as-a-new-acqua-standard)
- [Skype Certification Standard](https://learn.microsoft.com/en-us/skypeforbusiness/certification/archived/overview)
- **Tencent Certification Standard**: Tencent provides certification standards for audio and video communication products to ensure compatibility and performance within their ecosystem.

## Audio Algorithm Testing with CI/CD Automation
As a software developer, I've always been a fan of the CI/CD approach. But can we design a test rig for CI/CD on hardware testing? The answer is yes! This approach greatly benefits the development team. Audio testing is challenging due to the complexity of setting up the environment and conducting the tests. Automating this process can lead to faster delivery and quicker identification of issues.

Designing a Continuous Integration (CI) system for audio algorithm testing and automation involves several steps:

1. **Set Up a CI Server**: Use tools like Jenkins, GitLab CI, or CircleCI to set up your CI server.
2. **Automate Your Tests**: Write scripts to automate your audio tests. This can include running unit tests, integration tests, and performance tests. You can either use pure software scripts to test the metrics by feeding audio through your pipeline or set up a real hardware environment to script automate hardware test routines.
3. **Integrate with Version Control**: Ensure your CI system is integrated with your version control system (e.g., Git) to automatically run tests on code changes.
4. **Monitor and Report**: Set up monitoring and reporting to track test results and identify issues quickly. Quantify the metrics and make them meaningful.

# Conclusion
Testing audio systems and understanding speech quality metrics are essential skills for anyone working in audio technology. By following industry standards and automating your testing processes, you can ensure your products meet high-quality standards. If you have any questions or need further tips, feel free to reach out!

In conclusion, while the journey in audio algorithm and hardware development is filled with challenges, it's also incredibly rewarding. By setting up diverse testing environments, understanding and utilizing various metrics, automating the testing process, and fostering collaboration, we can overcome these obstacles and achieve high-quality audio systems.

# Resource
## Mega List of Audio Standards I've Collected Over the Years
The standards listed below are credited to their respective organizations:

- **ETSI**: European Telecommunications Standards Institute
- **IEEE**: Institute of Electrical and Electronics Engineers
- **ITU-T**: International Telecommunication Union - Telecommunication Standardization Sector
- **TR**: Technical Report

These organizations provide valuable guidelines and standards to ensure quality and consistency in audio and speech transmission.

### ITU-T G Series
The ITU-T G series recommendations focus on transmission systems, media, digital systems, and networks. Here are some key recommendations from the G series:

- [**ITU-T G.114**](https://www.itu.int/rec/t-rec-G.114): One-way transmission time - Defines acceptable limits for one-way transmission time in voice communication.
- [**ITU-T G.115**](https://www.itu.int/rec/t-rec-G.115): Mean active speech level for announcement and speech synthesis systems - Specifies the mean active speech level for these systems.
- [**ITU-T G.122**](https://www.itu.int/rec/t-rec-G.122): Influence of national systems on stability, talker echo, and listener echo in international connections - Addresses the impact of national systems on echo and stability in international calls.
- [**ITU-T G.131**](https://www.itu.int/rec/t-rec-G.131): Talker echo and its control - Provides guidelines for controlling talker echo.
- [**ITU-T G.160**](https://www.itu.int/rec/t-rec-G.160): Voice enhancement devices - Covers devices that enhance voice quality.
- [**ITU-T G.167**](https://www.itu.int/rec/t-rec-G.167): Acoustic echo controllers - Specifies requirements for devices that control acoustic echo.
- [**ITU-T G.169**](https://www.itu.int/rec/t-rec-G.169): Automatic level control devices - Defines standards for devices that automatically control audio levels.
- [**ITU-T G.711**](https://www.itu.int/rec/t-rec-G.711): Pulse code modulation (PCM) of voice frequencies - Standard for PCM of voice frequencies.
- [**ITU-T G.712**](https://www.itu.int/rec/t-rec-G.712): Transmission performance characteristics of pulse code modulation channels - Specifies performance characteristics for PCM channels.

### ITU-T P Series
The ITU-T P series recommendations focus on the quality of voice and audio communications. Here are some key recommendations from the P series:

- [**ITU-T P.10/G.100**](https://www.itu.int/rec/t-rec-p.10): Vocabulary for performance, quality of service, and quality of experience - Defines terminology for performance and quality.
- [**ITU-T P.50**](https://www.itu.int/rec/t-rec-p.50): Artificial voices - Defines standards for artificial voices used in testing.
- [**ITU-T P.51**](https://www.itu.int/rec/t-rec-p.51): Artificial mouth - Specifies standards for artificial mouths used in testing.
- [**ITU-T P.56**](https://www.itu.int/rec/t-rec-p.56): Objective measurement of active speech level - Defines methods for measuring active speech levels.
- [**ITU-T P.59**](https://www.itu.int/rec/t-rec-p.59): Artificial conversational speech - Defines standards for artificial conversational speech.
- [**ITU-T P.64**](https://www.itu.int/rec/t-rec-p.64): Determination of sensitivity frequency characteristics of local telephone systems - Specifies methods for determining sensitivity frequency characteristics.
- [**ITU-T P.1100**](https://www.itu.int/rec/t-rec-p.1100): Narrowband hands-free communication in motor vehicles - Specifies standards for hands-free communication in vehicles.
- [**ITU-T P.501**](https://www.itu.int/rec/t-rec-p.501): Test signals for use in telephony and other speech-based applications - Specifies test signals for telephony.
- [**ITU-T P.502**](https://www.itu.int/rec/t-rec-p.502): Objective test methods for speech communication systems using complex test signals - Defines objective test methods.
- [**ITU-T P.570**](https://www.itu.int/rec/t-rec-p.570): Artificial noise fields under laboratory conditions - Specifies standards for artificial noise fields.
- [**ITU-T P.800**](https://www.itu.int/rec/t-rec-p.800): Methods for subjective determination of transmission quality - Defines subjective methods for determining transmission quality.
- [**ITU-T P.800.1**](https://www.itu.int/rec/t-rec-p.800.1): Mean opinion score (MOS) terminology - Defines terminology for MOS.
- [**ITU-T P.835**](https://www.itu.int/rec/t-rec-p.835): Subjective test methodology for evaluating speech communication systems - Specifies subjective test methodologies.
- [**ITU-T P.862**](https://www.itu.int/rec/t-rec-p.862): Perceptual evaluation of speech quality (PESQ) - Defines methods for perceptual evaluation of speech quality.
- [**ITU-T P.863**](https://www.itu.int/rec/t-rec-p.863): Perceptual objective listening quality prediction - Specifies methods for predicting listening quality.
- [**ITU-T P.563**](https://www.itu.int/rec/t-rec-p.553): Single-ended method for objective speech quality assessment in narrowband telephony applications - Defines single-ended methods for speech quality assessment.

### ETSI EG and TS Series
The ETSI (European Telecommunications Standards Institute) EG and TS series focus on standards for speech and multimedia transmission quality.

- [**ETSI EG 202 396-1**](https://www.etsi.org/deliver/etsi_eg/202300_202399/20239601/01.02.02_60/eg_20239601v010202p.pdf): Speech Processing, Transmission and Quality Aspects (STQ)
- [**ETSI TS 103 106**](https://www.etsi.org/deliver/etsi_ts/103100_103199/103106/01.05.01_60/ts_103106v010501p.pdf): Speech and multimedia Transmission Quality (STQ); Speech quality performance in the presence of background noise

### IEEE Series
- [**IEEE 269-2019**](https://standards.ieee.org/ieee/269/5674/) The IEEE 269 standard focuses on measuring the electroacoustic performance of communication devices.


