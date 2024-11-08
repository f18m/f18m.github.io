---
layout: single
permalink: /electronics/
title:  "My Hardware Projects"
toc: true
date:   2024-11-05
author_profile: true
---

One of my favourite hobbies is Do-It-Yourself (DIY) electronics.

[![Electromagnetic spectrum for the hobbyist](/assets/ele/electromagnetic_spectrum_small.png "Electromagnetic spectrum for the hobbyist")](/assets/ele/electromagnetic_spectrum.png)

I like to design and assemble my own projects, even if that takes lots of time! (Most people only build projects designed and coinceived by others - there are plenty of them on the web - but I prefer to design from scratch all my circuits!).  
  
In this page I list some of my main electronic projects, listed from the most recent to the oldest one.

## Software Tools for HW projects

My favourite software packages for electronics were:

* _Spectrum Microcap_ as SPICE simulator; unfortunately the company behind this simulator was shut down. I need to find a modern alternative!
* _CadSoft EAGLE_ as schematic CAD; unfortunately this software product has been acquired by Autodesk which is discontinuing this tool... it's a pity.

Nowadays electronics involves lots of technologies and thus lots of different software; during my thesis and my projects I've thus used also: Cadence OrCAD, National Instruments MultiSim, Microchip MPLAB IDE, Altera Quartus II, Texas Instruments Code Composer Studio, Kicad.

## BeagleTorrent (2013-2016) 

This is actually more a software project than an electronic project. Simply put: I wanted to transform a low-cost single-board computer, the well-known [BeagleBone](https://www.beagleboard.org/), into a low-cost, low-power, multimedia server with the following features:

*   controlled by an easy-to-use web interface
*   torrent server downloading on an USB external drive (BeagleBone and other single-board-computers employ an SD card for the OS storage)
*   exposing the contents of the USB external drive as a Windows network share (via SAMBA)
*   streaming multimedia contents over the network, directly to my Samsung TV (via ReadyMedia)

I realized this project at first using a [BeagleBone](https://www.beagleboard.org/) and [Raspberry PI](https://www.raspberrypi.org/). However in both cases I had a lot of troubles with external drives attached via USB. For this reason I switched to [OLinuxino A20 LIME2](https://www.olimex.com/Products/OLinuXino/A20/A20-OLinuXIno-LIME2/) that provides a SATA interface, to avoid crappy SATA-to-USB Chinese converters.

The system now works well and streams all sort of media contents directly to my network-attached TV.

[![BeagleTorrent photo](/assets/ele/beagle_torrent_small.png "My current BeagleTorrent setup")](/assets/ele/beagle_torrent.png)   [![BeagleTorrent web interface](/assets/ele/web_interface.png "My web interface to BeagleTorrent")](/assets/ele/web_interface.png)  

You can now find the code that generates the simple web portal for this project in my Github [Light Media Center](https://github.com/f18m/light-media-center) project.

## Heart rate monitor (2008)

This project was developed for a course in _Medical electronics_ I took during my Master Degree. It's a simple all-analog circuit which takes the input from cheap electrodes and which displays the heart rate on some 7-segments LEDs through the ICL7107.

You can view the full schematic of this project clicking on the following thumbnails:

[![1st schematic of heart rate monitor](/assets/ele/heart_rate_monitor_sch.png)](/assets/ele/heart_rate_monitor_sch.png)   [![2nd schematic of heart rate monitor](/assets/ele/heart_rate_monitor_sch2.png)](/assets/ele/heart_rate_monitor_sch2.png)

You can read more details about the circuit and its design in its relative [essay](/assets/ele/cardiofrequenzimetro.pdf) (in italian).

## Wideband Acquisition Board (2008) 

This project consisted in the development of an USB-based acquisition board capable of:

*   sampling at 100 MHz
*   two channels: a low-frequency DC-coupled (0-1 MHz) channel and an high frequency DC-coupled one (0-30MHz)
*   employing USB 2.0 High Speed communication bandwidth toward the computer
*   amplification (with gain up to 30 for the low-frequency channel and up to 15 for the high-frequency channel)

The project currently has been designed but I lack the time to finish it! 

## Wheely (2008)

This project consisted in the development of a small 4-wheel robot, powered by a Microchip PIC24F driving two stepper motors and handling the radio communications via an (unfriendly) MRF49XA 433 MHz transceiver. Together with a friend, we developed: the drivers of the stepper motors, a LiPO battery recharger, the radio circuit (together with a PCB printed antenna), an USB Microchip-based radio transceiver and its software, to radio control the robot.  

Unfortunately, we found the mechanical problems to be the biggest hurdle to this project: the robot was capable of running straight only for short distances. For this reason we implemented a simple optical system to track the deviations from the straight course and correct them (for this, a simple PID controller was implemented on the PIC), but this never worked very well.


## Coilgun (2007)

This project was developed to find an employment to some big high-voltage capacitors... 
I had no much luck with this project... my coilgun was never able to actually "fire" metals.

## Lab Power Supply (2006)

This project was developed to equip my lab with a low-cost power supply capable of supplying stabilized voltages ranging from 5V to 25V (the output voltage can be selected rotating a multi-turn knob) and currents up to 1-2A (depending on the selected output voltage), with overcurrent protection. 

My original design consisted basically in: 220V rectifier bridge + BUCK switching converter + LINEAR stabilizer... and of course a lot of capacitors to filter out unwanted ripple. In addition, I designed: overcurrent protection, fast discharge system (this helps when the user decreases the output voltage using the main knob), digital output voltage display (via 7 segment LEDs), integrated amperometer. 

Unfortunately, I had no time to finish and test this project. Moreover, nowadays you can find very cheap lab power supplies which basically provide the same features.  
Here are the schematics in case someone is interested (annotations are in Italian though):

[![Microcap simulation](/assets/ele/lab_power_supply_sch_small.png)](/assets/ele/lab_power_supply_sch.png)  

## UsbPicProg (2006)

I've been working with the main author, Frans Schreuder, to a low-cost, versatile [USB PIC programmer](https://usbpicprog.org). In particular, I wrote some parts of the GUI of the programmer.

[![programmer](/assets/ele/usbpicprog_small.png)](/assets/ele/usbpicprog.png)
