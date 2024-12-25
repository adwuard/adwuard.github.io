---
title: "E-Paper Display for arXiv Papers"
excerpt: "Build a Raspberry Pi-powered e-paper display to showcase the latest arXiv papers.<br/><img src='/images/projects/arXivDisplay/2.jpg' width='320'>"
collection: projects
date: 2023-05-13
minute_read: 3
tags:
  - DIY Electronics
  - E-Paper
  - Raspberry Pi
  - Zero2
  - DIY Project
  - Data Scraping
---
# Overview
Building products with unique displays always adds a touch of magic. From circular displays to monochrome displays from Sharp, and now e-paper displays, each offers unique characteristics and charm when integrated into a project or product. In this project, I aim to explore the capabilities of e-paper displays. While there are numerous weather and time billboard projects, I wanted to create something different—something that requires a low refresh rate and serves an informational purpose.

### Thus, the idea for this project was born:   
> **An arXiv display that showcases the latest papers in the categories you subscribe to.**

<img src="/images/projects/arXivDisplay/2.jpg" width="550">
<img src="/images/projects/arXivDisplay/3.jpg" width="550">

---

# Key Components
- **Data Acquisition**: We need a method to scrape or fetch arXiv data on the latest papers. Fortunately, `@Mahdisadjadi` has developed an excellent scraper written in Python. You can find the repository here: [arxivscraper](https://github.com/Mahdisadjadi/arxivscraper).
- **Daily Update Timer**: Implement a timer to update the display daily with new papers. Use a long timer to fetch data and a short timer to update the display.
- **UI Rendering**: Use the Python Pillow library to render a 400x300 UI.
- **QR Code Generation**: Generate a QR code for each paper's PDF. This allows easy access to the paper by scanning the QR code if you're interested.
- **Optimized Font Rendering**: To improve the readability of text on the e-paper display, use a font that is specifically designed for low-resolution screens. The `Fira Code` font is a good choice as it is monospaced and optimized for clarity. You can download it from [Google Fonts](https://fonts.google.com/specimen/Fira+Code).

---

### Designing a 3D Printed Case
<img src="/images/projects/arXivDisplay/3D-Print.jpg" width="550">

# The Build
<img src="/images/projects/arXivDisplay/build-1.jpg" width="550">

# Scraping and Displaying Papers with QR Codes for Fast Access
<img src="/images/projects/arXivDisplay/arxiv-paper.jpg" width="550">

# Dithering Algorithm for Displaying Grayscale Images on a Monochrome Display
For displaying grayscale images on a monochrome display, dithering algorithms can be very useful. Tanner Helland provides an excellent overview of eleven different dithering algorithms, complete with source code. You can read more about these algorithms and find the source code on his [website](https://tannerhelland.com/2012/12/28/dithering-eleven-algorithms-source-code.html). This resource will help you choose the best dithering technique for your e-paper display project.

### Here's some of the dithered images I made with the e-paper display
<img src="/images/projects/arXivDisplay/ditter-1.jpg" width="350">
<img src="/images/projects/arXivDisplay/ditter-2.jpg" width="350">
<img src="/images/projects/arXivDisplay/ditter-3.jpg" width="350">

# Resources
- [EPaper Purchase Link](https://www.waveshare.com/4.2inch-e-Paper-Module.htm)
- [Wiki Page](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module)
- [arxivscraper GitHub Repository](https://github.com/Mahdisadjadi/arxivscraper)
- [RPI Setup Guide](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_Manual#Working_With_Raspberry_Pi)
- [Tanner Helland's Dithering Algorithms](https://tannerhelland.com/2012/12/28/dithering-eleven-algorithms-source-code.html)
