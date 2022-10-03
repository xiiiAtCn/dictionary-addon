#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from string import Template

import requests

# from translator.BaiduOpenApi import BaiduOpenApi
from translator.YoudaoOpenApi import YoudaoOpenApi

Req_Base = "https://dict.youdao.com/suggest?num=1&ver=3.0&doctype=json&cache=false&le=en&q="



wordDic = dict()
wordArr = []

savedPath = os.path.abspath(os.path.join(os.getcwd(), '../../../../WTF/Account/219135313#1/SavedVariables/Dictionary.lua'))
dictionaryPath = os.path.abspath(os.path.join(os.getcwd(), '../Dictionary.lua'))

with open(savedPath) as dictionary:
  lines = dictionary.readlines()
  for line in lines:
    print(line)
    match = re.search(r'\["([a-z]*)"\] = "(.*)",$', line, re.I)
    print(match)
    if match != None:
      wordDic.update({ match.group(1): match.group(2)})
      wordArr.append(match.group(1))
for word in wordArr:
  if wordDic[word] == '':
    print(word)
    openApi = YoudaoOpenApi()
    res = openApi.createRequest(word)
    wordDic.update({word: res['value']})

with open(dictionaryPath, 'w') as dictionary:
  first = Template('  ["$key"] = "$value",\n')
  second = Template('  ["$key"] = $value, \n')
  dictionary.write('DefaultDictionary = {\n')
  for key, value in wordDic.items():
    if value != 'no answer':
      if value.startswith('"'):
        dictionary.write(second.safe_substitute(key = key, value = value))
      else:
        dictionary.write(first.safe_substitute(key = key, value = value))
    else:
      dictionary.write(first.safe_substitute(key = key, value = ''))

  dictionary.write('}')
# res = requests.get(Req_Base + "synopsis")

# print(res.text)
