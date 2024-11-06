---
layout: single
permalink: /about/
title:  "About Me"
toc: true
date:   2024-11-05
author_profile: true
---

Welcome to my homepage. My name is **Francesco Montorsi**.

## Short Bio

Very short bio: I was born in 1986 near Modena, Italy. I took the Bachelor Degree and the Master Degree in _Electronic Engineering_ at the [University of Modena and Reggio Emilia](http://www.ing.unimo.it). I took the PhD in the same university in the area of [telecommunications](http://en.wikipedia.org/wiki/Telecommunication) (more info about my PhD research activity is in the [publications](/publications/) page). I'm currently employed in a telecommunication company which provides high-performance high through-put live analysis of data on mobile network operators.

My favourite hobbies are [computer programming](/programming/) (thus you'll find here mostly stuff about it) and [DIY electronics](/electronics/).  
I keep up to date also a page with my (scientific) [publications](/publications/) and the related material (software and data used in the papers, etc).

My curriculum vitae is available [here](/assets/misc/Francesco_Montorsi_CV.pdf) as well as my theses:

*   [bachelor thesis](http://sourceforge.net/projects/frm-research/files/Publications/tesi_triennale.pdf) (in italian) entitled "Development of Fine Frequency Synchronization System for OFDM Communication Systems";
*   [master thesis](http://sourceforge.net/projects/frm-research/files/Publications/tesi_specialistica.pdf) (in italian) entitled "Development and Implementation of a Wideband Digital Modem";
*   PhD thesis: not public yet (will be released to public in 2016)

I also have a public profile on LinkedIn: [http://www.linkedin.com/in/francescomontorsi](http://www.linkedin.com/in/francescomontorsi).

These pages are updated when I have time (i.e. rarely)...

Contact info If you want to contact me, please send me an email at: [francesco.montorsi@NOSPAM AT gmail.com](mailto:francesco.montorsi@NOSPAM_AT_gmail.com) (remove @NOSPAM).

## SSH public key 

The following is my [public SSH key](/assets/misc/francesco.pub), which can be used to authenticate my emails/documents:  

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDiEkclo+Ai+ADF7ov9Mt2udKLwxon7h+3n2IWIGosHZtdP32A8Ey3m/4XQwbTMMqqGnhnJ4/woJUlwOBGURdjzh31P8q52aG1E59eyEU+mil05KpkUPXxAr/jj18sumBi9LXZx4gLLsq3XJL7q06J9W7K24bm42M6PkymTgf8CsnStJhx9JeedFOLMfejQ719ZpiwR2UXDSRTbRlRt5flv6zY05vsxvUvFCCc4MG5pGWKu2/FMsgM3h7ufq06DTBAkcG+48Z7BnTxCWIShur2vlEiH6Cugsin7wiBgvph8V7uZzUbzz8ziafmOifrT3gukK15ulzzMnfGLfgGMl21V imported-openssh-key  
```

To install the key on a Unix-like machine with OpenSSH:

*   log into the remote host entering the password
*   download the public key: 

```
cd ~/.ssh && wget http://frm.users.sourceforge.net//assets/misc/francesco.pub
```
*   install the public key: 

```
cat >> ~/.ssh/authorized\_keys2 < ~/.ssh/francesco.pub
```