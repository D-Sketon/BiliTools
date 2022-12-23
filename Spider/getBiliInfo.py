import json

import requests

from Spider.getHeader import *


def getBiliCsrf(cookie):
    """获得cookie中的bili_jct(csrf token)

    :param cookie: cookie值
    :return: csrf值
    """
    pattern = re.compile(r'(?<=bili_jct=)[0-9a-z]+')
    match = pattern.search(cookie)
    start = match.start()
    end = match.end()
    return cookie[start:end]


def getBiliUserUid(cookie):
    """获得cookie中的DedeUserID(UID)

    :param cookie: cookie值
    :return: UID值
    """
    if not cookie:
        return cookie
    pattern = re.compile(r'(?<=DedeUserID=)[0-9]+')
    match = pattern.search(cookie)
    start = match.start()
    end = match.end()
    return cookie[start:end]


def getBiliUserInfo(uid):
    url = 'https://api.bilibili.com/x/space/acc/info'
    data = {
        'mid': uid,
        'jsonp': 'jsonp'
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def parseUsername(jsonString):
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    return dictionary['data']['name']


def parseFacePhoto(jsonString):
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    return dictionary['data']['face']


def parseAllInfo(jsonString):
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    data = {
        'name': dictionary['data']['name'],
        'birthday': dictionary['data']['birthday'],
        'sex': dictionary['data']['sex'],
        'coins': dictionary['data']['coins'],
        'level': dictionary['data']['level'],
        'sign': dictionary['data']['sign'],
        'face': dictionary['data']['face']
    }
    return data
