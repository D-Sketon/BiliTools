import json
import re

import requests

recommendList = []


def getRecommend(bvid, size):
    """获得推荐与其相关的size个视频

    :param bvid:视频bv号
    :return:返回bvid list
    """
    recommendList.clear()
    url = "https://www.bilibili.com/video/" + bvid
    r = requests.get(url)
    parseRecommend(r.text, size)
    return recommendList


def parseRecommend(html, size):
    jsonData = json.loads(parseHtmlForRelated(html))
    related = jsonData['related']
    for items in related:
        pic_before = items['pic']
        pic_after = pic_before.replace(r"\u002F", "\\")
        data = {
            "aid": items['aid'],
            "cid": items['cid'],
            "bvid": items['bvid'],
            "pic": pic_after,
            "title": items['title']
        }
        recommendList.append(data)
    for items in recommendList:
        item = items['bvid']
        url = "https://www.bilibili.com/video/" + item
        r = requests.get(url)
        html = r.text
        jsonData = json.loads(parseHtmlForRelated(html))
        related = jsonData['related']
        for items in related:
            pic_before = items['pic']
            pic_after = pic_before.replace(r"\u002F", "\\")
            data = {
                "aid": items['aid'],
                "cid": items['cid'],
                "bvid": items['bvid'],
                "pic": pic_after,
                "title": items['title']
            }
            if len(recommendList) > size:
                return
            recommendList.append(data)


def parseHtmlForRelated(html):
    pattern = re.compile(r'(?<=<script>window.__INITIAL_STATE__=)[\s\S]+')
    match = pattern.search(html)
    start = match.start()
    end = match.end()
    html_pro1 = html[start:end]
    pattern = re.compile(r'[\s\S]+(?=;\(function\(\)\{var s;\(s=document.currentScript)')
    match = pattern.search(html_pro1)
    start = match.start()
    end = match.end()
    return html_pro1[start:end]
