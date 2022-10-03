import hashlib
import json
import random
from string import Template

import requests

randomKey = 'abcdefghijklmnopqrstuvwxyz0123456789'

class BaiduOpenApi:
  def __init__(self) -> None:
    self.base_path = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    self.secret = 'NyE1UxMmPMziiiZkAJHJ'
    self.query = {
      'from': 'en',
      'to': 'zh',
      'appid': '20221003001367945',
    }
    self.salt = ''


  def _createMd5_(self, text: str):
    md5 = hashlib.md5()
    md5.update(text.encode(encoding="utf-8"))
    return md5.hexdigest()

  def _signQuery_(self, query: str):
    ### concat sequence: 'appid', 'q', 'salt', 'secret'
    ### refer link: https://fanyi-api.baidu.com/doc/21

    salt = ''.join(random.sample(randomKey, 10))
    print('salt: ', salt)
    self.salt = salt
    print('before salt: ', self.salt)
    original = self.query['appid'] + query + self.salt + self.secret
    return self._createMd5_(original)
  
  def _buildQueryStr_(self, search: str):
    ### query: [q, from, to, appid, salt, sign ]
    query = Template('q=$q&from=$from_l&to=$to_l&appid=$appid&salt=$salt&sign=$sign&dict=0')
    sign = self._signQuery_(search)
    return query.safe_substitute(q= search, from_l= self.query['from'], to_l=self.query['to'], appid=self.query['appid'], salt=self.salt, sign = sign)
  def createRequest(self, word: str):
    query = self._buildQueryStr_(word)
    print(query)
    res = requests.get(self.base_path + '?' + query)
    print(json.loads(res.text))

