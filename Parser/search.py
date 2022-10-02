#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


Req_Base = "https://dict.youdao.com/suggest?num=1&ver=3.0&doctype=json&cache=false&le=en&q="

res = requests.get(Req_Base + "synopsis")

print(res.text)