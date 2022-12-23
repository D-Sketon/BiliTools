import requests

from Spider.getHeader import *


def getTag(aid, ip, port):
    """获得视频的TAG

    :param aid:视频av号
    :return:返回response json
    """
    if ip and port:
        flag = True
    else:
        flag = False

    url_backup = 'https://api.bilibili.com/x/web-interface/view/detail/tag'
    url = 'https://api.bilibili.com/x/tag/archive/tags'
    data = {
        'aid': aid,
        'jsonp': 'jsonp'
    }
    session = requests.Session()
    if flag:
        proxies = {
            "http": "http://" + ip + ":" + port,
            "https": "http://" + ip + ":" + port
        }
        r = session.get(url, headers=getHeader(), params=data, proxies=proxies)
    else:
        r = session.get(url, headers=getHeader(), params=data)

    if r.text.startswith("{\"code\":0"):
        return r.text
    else:
        if flag:
            proxies = {
                "http": "http://" + ip + ":" + port,
                "https": "http://" + ip + ":" + port
            }
            r = session.get(url_backup, headers=getHeader(), params=data, proxies=proxies)
        else:
            r = session.get(url_backup, headers=getHeader(), params=data)
        return r.text
