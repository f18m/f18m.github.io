---
layout: single
permalink: /programming/
title:  "My Software Projects"
toc: true
date:   2025-11-12
author_profile: true
---

[My GitHub page](https://github.com/f18m?tab=repositories) is where all my recent activity is stored and indexed.
In this page I keep track of my various projects involving computer science and computer programming. They are roughly ordered by year and by category.

## More HomeAssistant projects (2025-2026)

* [Floor-heating controller](https://github.com/f18m/floor-heating-controller): an ESPHome package that allows me to control from Home Assistant all the hydraulic valves for floor heating.
* [viessmann-optolink2mqtt](https://github.com/f18m/viessmann-optolink2mqtt): a bridge between my Viessmann heatpump device and MQTT to enable smart control of the house heating.
* [HERAComm Invoice analyzer](https://github.com/f18m/heracomm-invoice-analyzer): an utility Python project to help me analyze invoices related to electric and gas utilities


## HomeAssistant projects (2024-2025)

* [HomeAssistant VOIP client](https://github.com/f18m/ha-addon-voip-client): An Home Assistant addon that runs a VOIP client, to initiate outgoing calls or receive incoming calls
* [HomeAssistant DHCP server](https://github.com/f18m/ha-addon-dnsmasq-dhcp-server): An Home Assistant addon that runs dnsmasq as a DHCP server; the perfect tool to take control of all your home automation devices and have a single pane of glass.
* [HomeAssistant RPi MQTT bridge](https://github.com/f18m/rpi2home-assistant): A software daemon to expose Raspberry PI inputs and outputs to HomeAssistant through MQTT.
* [PSMQTT](https://github.com/eschava/psmqtt/): a cross-platform utility for reporting system and processes metrics (CPU, memory, disks, network, S.M.A.R.T. disk data) to an MQTT broker.


## Utilities for commercial projects (2020-2024)

* [cMonitor](https://github.com/f18m/cmonitor): a Docker/LXC/Kubernetes, database-free, lightweight container performance monitoring solution.
* [MallocTag](https://github.com/f18m/malloc-tag): a lighweight, intrusive memory profiler that allows to categorize or "tag" memory allocation inside C/C++ projects
* [Boost Intrusive Pool](https://github.com/f18m/boost-intrusive-pool): A C++ memory pool that is Boost-friendly and performance oriented (zero-malloc).


## Software for my Hardware projects (2017-2019) 

*   [Light Media Center](https://github.com/f18m/light-media-center): a simple, light and fast collection of scripts, configuration files and web code to implement a basic media center capable to run on single board computers like Rasperry PI, BeagleBone, OLinuxino, etc.
*   [NetlistViewer](https://github.com/f18m/netlist-viewer): a tool capable of loading SPICE netlists and convert them in a schematic (i.e., graphical format)


## Tools and Libraries (2017-2019) 

At some point I started to work create and publish libraries and low-level tools designed
to solve some issue I encountered in my everyday job:

*   [Large PCAP analyzer](https://github.com/f18m/large-pcap-analyzer): a simple tool to handle large files containing captured traffic (e.g., TCP/IP)
*   [CPU-MEM-monitor](https://github.com/f18m/CPU-MEM-monitor): a simple script to log Linux CPU and memory usage over time and output an Excel-friendly report.
*   [rpm-make-rules-dependency-lister](https://github.com/f18m/rpm-make-rules-dependency-lister): a small tool to allow incremental RPM packaging, useful to speed up your deployment chain when you are packaging several RPMs
*   [rpm-spec-dependency-analyzer](https://github.com/f18m/rpm-spec-dependency-analyzer): a simple Python3 script to generate a DOT graph of the inter-dependencies among a set of SPEC files
*   [malloc-benchmarks](https://github.com/f18m/malloc-benchmarks): simple benchmarking scripts to run on any machine to compare different C/C++ malloc implementations.

A few more github-based projects I have contributed to are:

*   [ZMQ](https://github.com/zeromq/libzmq): the fastest middleware for modern message exchange!
*   [eclipse-bash-editor](https://github.com/de-jcup/eclipse-bash-editor): Bash editor plugin for eclipse


## Misc projects (2009-2015)

Other miscellaneous projects I created or where I collaborated:

*   [EmfPrinter](https://emfprinter.sf.net): a virtual printer driver for Windows 2000 and Windows XP, which allows you to generate EMF and WMF
*   [muParser](https://beltoforion.de/en/muparser/): fast math parser library
*   [UsbPicProg](https://usbpicprog.org/): a free and open source usb pic programmer
*   [OphMedRecords](https://ophmedrecords.sf.net/): a simple ophthalmic medical records archival software


## Games (2009-2014) 

I did create also a couple of simple games (I may open-source them in the future) using [Unity](https://unity.com/) (which back at the time was named _Unity3D_).
Back at the time I contributed a simple Hermite Spline Controller but that was lost after the Unity3D Wiki was shut down.

![Unity3D](/assets/images/unity3d.png) 


## MATLAB contributions (2009-2013) 

During my PhD I have been writing ton of MATLAB code regarding the wide fields of: a) signal processing (in particular for radio and inertial signals), b) modelling of localization system signals, c) statistical estimation (e.g., imeplementation of maximum-a-posteriori estimators for specific problems), d) pattern recognition.

![MATLAB](/assets/images/matlab.png)

Most of that code is specifically tied to my scientific research and I have uploaded it at [https://sourceforge.net/projects/frm-research/](https://sourceforge.net/projects/frm-research/). Some code is generic enough to be useful to others; for this reason I'm (slowly) posting on [the MATLAB FileExchange page](https://it.mathworks.com/matlabcentral/profile/authors/2008460?detail=all) some of my most general-purpose code.


## Firefox addons (2009-2012)

I'm not a fan of XUL programming but I'm a great fan of Firefox ;)  
Recently I needed to to extend its functionalities and thus I took some time to create my own Firefox addon. As almost all Firefox extensions, it's written in a mix of JavaScript and XUL. The code was initially hosted by Mozdev.org but later I moved it to [this page](https://sourceforge.net/projects/contextcalc/) on Sourceforge.

![Firefox](/assets/images/firefox.png)

In December 2009 the first public version, 0.3, was released. I've not been updating this extension for some time so it was eventually retired from the list of Firefox addons.

## Bakefile (2007-2009)

To create all build systems for my software packages I have been using for some time [Bakefile](https://github.com/vslavik/bakefile): a cross-platform, open source makefile- and IDE projects- generator. I created the bakefiles for various wxWidgets-related libraries.
I've also contributed various patches to Bakefile: you can see them [here](https://sourceforge.net/tracker/?atid=568031&group_id=83016&func=browse&by_submitter=frm).


## wxCode (2005-2009)

I have written various components for wxWidgets hosted by [wxCode](https://wxcode.sourceforge.net) and written in C++:
![wxCode](/assets/images/wxcodelogo2.png)

wxCode has been retired and its website shut down in 2018.
The code is still there though. So this is the list of the components I contributed to wxCode:

*   [Keybinder](https://sourceforge.net/p/wxcode/code/HEAD/tree/trunk/wxCode/components/keybinder)
*   [wxExtMiniFrame](https://sourceforge.net/p/wxcode/code/HEAD/tree/trunk/wxCode/components/extminiframe)
*   [wxScript](https://sourceforge.net/p/wxcode/code/HEAD/tree/trunk/wxCode/components/wxscript)
*   [wxXml2](https://sourceforge.net/p/wxcode/code/HEAD/tree/trunk/wxCode/components/wxxml2)
*   [WebUpdate](https://sourceforge.net/p/wxcode/code/HEAD/tree/trunk/wxCode/components/webupdate)


## wxWidgets programming (2003-2009) 
[wxWidgets](https://www.wxwidgets.org) is a powerful library and an [open source](https://www.opensource.org) C++ toolkit for cross-platform Graphical User Interfaces (GUI). I've submitted a good number of patches to wxWidgets project: you can browse them [here](https://trac.wxwidgets.org/query?status=accepted&status=closed&status=confirmed&status=infoneeded&status=infoneeded_new&status=new&status=portneeded&status=reopened&group=component&reporter=%24USER&order=priority). In 2007-2009 I have been one of the wxWidgets developers and I worked in many areas of the library (new widgets: wx\*PickerCtrl, wxCollapsiblePane; documentation of wxWidgets, bugfixing, etc). I've been involved in various open-source projects related to wxWidgets:

![wxWidgets](/assets/images/wxlogo.jpg)

*   [MathStudio](https://mathstudio.sf.net): an attempt to build an easy-to-use CAS
*   [wxCode](https://wxcode.sf.net): a repository of wxWidgets addons
*   [wxArt2d](https://wxart2d.sf.net): 2D drawing facilities
*   [wxLua](https://wxlua.sf.net): Lua bindings to wxWidgets
*   [wxGlPlot](https://mathdev.sf.net): a plotter for 2D/3D mathematical functions

  
## Google Summer of Code (2006-2007)

On summer 2006 and 2007, I also partecipated to the [Google Summer of Code](https://code.google.com/soc/) with wxWidgets projects: the [wxWidgets package manager](https://wiki.wxwidgets.org/ComponentManager) and the XTI metadata completion.

![GSoc](/assets/images/soc2007.gif)

It was a very nice experience, also because of the great help I received by my mentor, Julian Smart. Thanks to both Google, Julian Smart and wxWidgets team!

## Coreutils (2006) 

Back in 2006 I did contribute the `--group-directories-first` option to the `ls` GNU coreutil. [Here's](https://lists.gnu.org/archive/html/bug-coreutils/2006-01/msg00000.html) the link to the coreutils ML.


## PlanetSourceCode (2003-2004)

At the beginning of my programming experiences I posted some of my works at [www.planetsourcecode.com](https://web.archive.org/web/20191215041540/http://www.planetsourcecode.com/).

These very old projects have been lost when PlanetSourceCode has been shut down.
But I still have a copy of my old _CountDown_ utility zipped [here](/assets/prog/countdown.zip).

