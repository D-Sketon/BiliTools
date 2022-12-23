import requests

from Spider.getHeader import *


def getHistory(page_num, page_per_num):
    """获得历史记录

    :param page_num:页数
    :param page_per_num:每页条数
    :return:response json
    """
    url = 'https://api.bilibili.com/x/v2/history'
    data = {
        'pn': page_num,
        'ps': page_per_num,
        'jsonp': 'jsonp',
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getPopular(page_num, page_per_num):
    """获得综合热门

    :param page_num:页数
    :param page_per_num:每页条数
    :return:response json
    """
    url = 'https://api.bilibili.com/x/web-interface/popular'
    data = {
        'pn': page_num,
        'ps': page_per_num,
        'jsonp': 'jsonp',
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getPopularPrecious(page_num, page_per_num):
    """获得入站必刷

    :param page_num:页数
    :param page_per_num:每页条数
    :return:response json
    """
    url = 'https://api.bilibili.com/x/web-interface/popular/precious'
    data = {
        'pn': page_num,
        'ps': page_per_num,
        'jsonp': 'jsonp',
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getPopularSeries(week):
    """获得每周必看

    :param week:周数
    :return:response json
    """
    url = 'https://api.bilibili.com/x/web-interface/popular/series/one'
    data = {
        'number': week
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getRanking(rid, type):
    """获得排行榜

    :param rid:
    0   全站
    168 国创相关
    1   动画
    3   音乐
    129 舞蹈
    4   游戏
    36  知识
    188 科技
    234 运动
    223 汽车
    160 生活
    211 美食
    217 动物圈
    119 鬼畜
    155 时尚
    5   娱乐
    181 影视
    :param type:
    all     全部
    origin  原创
    rookie  新人
    :return:
    """
    url = 'https://api.bilibili.com/x/web-interface/ranking/v2'
    data = {
        'rid': rid,
        'type': type
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text
