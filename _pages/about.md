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

Very short bio: I was born in the eighties in northern Italy. I took the Bachelor Degree and the Master Degree in _Electronic Engineering_ at the [University of Modena and Reggio Emilia](https://www.ingmo.unimore.it/en). 
I then took a PhD in the telecom space (more info about my PhD research activity is in the [publications](/publications/) page). 
After such academical journey I went into the industry and I've been working on a number of different software companies; more details about my work experiences are available on [my LinkedIn profile](https://www.linkedin.com/in/francescomontorsi).

My favourite hobbies are [computer programming](/programming/) (thus you'll find here mostly stuff about it) and [DIY electronics](/electronics/).  
I keep up to date also a page with my (scientific) [publications](/publications/) and the related material (software and data used in the papers, etc).

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
cd ~/.ssh && wget https://f18m.github.io/assets/misc/francesco.pub
```
*   install the public key: 

```
cat >> ~/.ssh/authorized\_keys2 < ~/.ssh/francesco.pub
```