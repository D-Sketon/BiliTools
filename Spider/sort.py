import json
import re

import requests

from Spider.getHeader import getHeader

order = ''
resultList = []


def getVideos(number, tag, tid, order1):
    resultList.clear()
    url = "https://api.bilibili.com/x/web-interface/search/type"
    for i in range(1, 100):
        data = {
            'context': "",
            'page': i,
            'keyword': tag,
            'order': order1,
            'search_type': 'video',
            'tids': int(tid)
        }
        r = requests.get(url, headers=getHeader(), params=data)
        parseResult(r.text, number)
        if len(resultList) >= number:
            break
    return resultList


def parseResult(jsonString, number):
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]["result"]:
        data = {
            'bvid': elem['bvid'],
            'title': title(elem['title']),
            'pic': elem['pic'],
            'play': elem['play'],
            'review': elem['review'],
            'video_review': elem['video_review'],
            'favorites': elem['favorites'],
            'pubdate': elem['pubdate']
        }
        resultList.append(data)
        if len(resultList) >= number:
            break


def doubleSort(list, order2):
    global order
    if order2 == "click":
        order = "play"
    elif order2 == "dm":
        order = "video_review"
    elif order2 == "stow":
        order = "favorites"
    elif order2 == "pubdate":
        order = "pubdate"
    list.sort(key=compare, reverse=True)

    return list


def compare(elem):
    global order
    return int(elem[order])


def title(title):
    return re.sub(r'<em class="keyword">(.+?)</em>', "", title)
