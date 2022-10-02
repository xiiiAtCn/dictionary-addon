#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from string import Template

import requests

Req_Base = "https://dict.youdao.com/suggest?num=1&ver=3.0&doctype=json&cache=false&le=en&q="



wordDic = dict()
wordArr = []

savedPath = os.path.abspath(os.path.join(os.getcwd(), '../../../../WTF/Account/219135313#1/SavedVariables/dic.lua'))
dictionaryPath = os.path.abspath(os.path.join(os.getcwd(), '../Dictionary.lua'))

with open(savedPath) as dictionary:
  lines = dictionary.readlines()
  for line in lines:
    match = re.search(r'\["([a-z]*)"\] = (.*),', line, re.I)
    if match != None:
      wordDic.update({ match.group(1): match.group(2)})
      wordArr.append(match.group(1))
print(wordArr)
for word in wordArr:
  if wordDic[word] == '""':
    print(word)
    res = requests.get(Req_Base + word)
    result = json.loads(res.text)
    print(result)
    code = result['result']['code']
    if code != 200:
      print('cannot find word <', word, "> in youdao dictionary")
      wordDic.update({ word: "no answer" })
    else:
      message = result['data']['entries'][0]
      print(word)
      if message['entry'] == word:
        print(message['explain'])
        wordDic.update({word: message['explain']})
      else:
        wordDic.update({word: 'similar word: ' + message['entry'] + ', ' +  message['explain']})

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
