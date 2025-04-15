---
layout: single
title:  "Geotagging old photos with Free Software"
date:   2025-04-09
categories: photos
---

I recently spent some time writing my own script based on exiftool to help me with mass-geotagging of 
old photos, taken 10-15 years ago when geotagging was not that common
(or trivially, the GPS sensor was not yet available in all smartphones!).

After creating and validating the script, I found a much easier and ready solution was already there: [DigiKam](https://www.digikam.org/).
A brief step-by-step procedure to mass geo-tag photos with DigiKam:

1. Import all your photos (a.k.a. "albums" for DigiKam) in the application. This will take a while if you have many files.
2. Navigate your album by folder names (that's where I can find information on the location where photos were taken);
3. Select all photos (`CTRL+A`);
4. Bring up the "Geolocation Editor" (`CTRL+SHIFT+G`);
5. Select all photo thumbnails;
6. Use the "Search" panel to find the location on the map where you think all photos were (roughly) taken;
7. Right-Click on the location result and select "Move selected images to this position";

And voilà.
However this only works fine if all the photos you want to geotag live in the same folder.
If they are nested within multiple folders, you may want to look at [my mass-geotagging exiftool script](https://gist.github.com/f18m/5b54dd6f2838920762dc987671ac935e).

