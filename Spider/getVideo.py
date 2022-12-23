import json

import requests

from Spider.getHeader import *


def getVideoByBvid(bvid):
    url = 'https://api.bilibili.com/x/web-interface/view'
    data = {
        'bvid': bvid
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getVideoByAid(aid):
    url = 'https://api.bilibili.com/x/web-interface/view'
    data = {
        'aid': aid
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getVideoName(jsonString):
    content = json.loads(jsonString)
    name = content['data']['title']
    return name

