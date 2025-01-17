---
layout: single
title:  "Looking for a fast and cheap presence sensor?"
date:   2025-01-17
categories: homeassistant
---

I'm now testing in my house the [Tuya ZY-M100](https://it.aliexpress.com/item/1005004705672138.html?sku_id=12000030169395611&gatewayAdapt=glo2ita) radar presence sensor.
You can find that online from several different vendors from platforms like Aliexpress.

So far I found this sensor to be in a really good spot:

* it's really cheap (11€ roughly); but you will need to add some kind of mounting bracket, like 
  [this one](https://it.aliexpress.com/item/1005007545582299.html?spm=a2g0o.order_list.order_list_main.5.ff193696XJo79e&gatewayAdapt=glo2ita) which adds few more euros

* it's quite fast in the OFF->ON transition which is important if you want to e.g. use this presence
  sensor to activate lights on staircases or corridors or similar crossing points.

* the Zigbee version works completely off-the-cloud, locally. If you use HomeAssistant and the ZHA integration
  for Zigbee devices you will need [this quirk](https://github.com/zigpy/zha-device-handlers/issues/3472)

I also have as presence sensors:
* Aqara FP2
* Everything Presence Lite
and I can say that this Tuya sensor is faster in the OFF->ON transition in comparison to both the Aqara
and the Everything Presence sensors (which are more complex devices supporting zones).

Hope this will be useful to you, if you're looking for a simple (no zone) presence sensor!
