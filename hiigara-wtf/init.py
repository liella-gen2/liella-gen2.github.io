#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import random, time
import requests as req
class Constants(object):
    URL_PATTERN = "https://wtf.hiigara.net/api/run/LdQqGz/%s/%s?event=ManualRun"
    NUM_NAMES = 3
    LST_NAMES = [ ("name%02d" % _) for _ in range(NUM_NAMES) ]
    SET_NAMES = list(set(LST_NAMES))
    REQ_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
if __name__ == "__main__":
    print(Constants.SET_NAMES)
    resset = set()
    for k in range(Constants.NUM_NAMES):
        for l in range(Constants.NUM_NAMES):
            resset |= {req.get(url=(Constants.URL_PATTERN % ("%s_0" % Constants.SET_NAMES[k], "%s_1" % Constants.SET_NAMES[l])), headers=Constants.REQ_HEADERS).json()["text"].replace("%s_0" % Constants.SET_NAMES[k], "nameof0").replace("%s_1" % Constants.SET_NAMES[k], "nameof1")}
            time.sleep(random.randint(0, 4) + random.random())
#just4fun...