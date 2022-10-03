import hashlib
import json
import random
from string import Template
from time import time

import requests

randomKey = 'abcdefghijklmnopqrstuvwxyz0123456789'

class YoudaoOpenApi:
  def __init__(self) -> None:
    self.base_path = 'https://openapi.youdao.com/api'
    self.secret = 'ArCPpw1pWU1QVjaYJn2tTdBwl6pdmwiB'
    self.query = {
      'from': 'en',
      'to': 'zh-CHS',
      'appid': '30a1efb29ce98152',
      'timestamp': 0,
      'salt': ''
    }


  def _createH256_(self, text: str):
    sha256 = hashlib.sha256()
    sha256.update(text.encode(encoding="utf-8"))
    return sha256.hexdigest()

  def _signQuery_(self, query: str):
    ### concat sequence: 'appid', 'q', 'salt', 'secret'
    ### refer link: https://fanyi-api.baidu.com/doc/21

    salt = ''.join(random.sample(randomKey, 10))
    self.query['salt'] = salt
    self.query['timestamp'] = int(round(time()))
    original = self.query['appid'] + query + self.query['salt'] + str(self.query['timestamp']) + self.secret
    return self._createH256_(original)
  
  def _buildQueryStr_(self, search: str):
    ### query: [q, from, to, appid, salt, sign ]
    query = Template('q=$q&from=$from_l&to=$to_l&appKey=$appKey&salt=$salt&sign=$sign&signType=v3&curtime=$curtime')
    sign = self._signQuery_(search)
    return query.safe_substitute(
      q= search, 
      from_l= self.query['from'],
      to_l=self.query['to'], 
      appKey=self.query['appid'], 
      salt=self.query['salt'], 
      sign = sign,
      curtime= self.query['timestamp']
      )
  def createRequest(self, word: str):
    query = self._buildQueryStr_(word)
    print(query)
    res = requests.get(self.base_path + '?' + query)
    result = json.loads(res.text)
    print(result)
    # print(result['explains'])
    if result['isWord'] == True:
      return {
        'value': '; '.join(result['basic']['explains']),
      }
    else:
      return {
        'value': ''
      }
   

