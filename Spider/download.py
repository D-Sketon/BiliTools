from Spider.getVideo import *


# https://www.bilibili.com/read/cv6415114/
def download(bvid, p_num=1, qn=64):
    """

    :param aid:视频av号
    :param p_num:分P数
    :param qn:视频质量
    4K      120
    1080p60 116
    720p60  74
    1080p+  112
    1080p   80
    720p    64
    480p    32
    360p    16
    :return:
    """
    # 目前最大分P数：7199
    if p_num < 1:
        return False
    url = 'https://api.bilibili.com/x/player/playurl'
    cid = getcid(bvid, p_num)
    if not cid:
        return False
    if qn != 120:
        data = {
            'bvid': bvid,
            'cid': cid,
            'qn': qn
        }
    else:
        data = {
            'bvid': bvid,
            'cid': cid,
            'qn': qn,
            'fourk': 1
        }
    r = requests.get(url, headers=getHeader(), params=data)
    url = parseUrl(r.text)
    return url


def getcid(bvid, p_num):
    result = parsecid(getVideoByBvid(bvid))
    if not result:
        return False
    else:
        if p_num > len(result):
            return False
        else:
            return result[p_num - 1]


def parsecid(text):
    content = json.loads(text)
    if content['code'] != 0:
        return False
    pages = content['data']['pages']
    cidlist = []
    for obj in pages:
        cidlist.append(obj['cid'])
    return cidlist


def parseUrl(text):
    content = json.loads(text)
    if content['code'] != 0:
        return False
    else:
        return content['data']['durl'][0]['url']


def qndetect(bvid, p_num=1):
    if p_num < 1:
        return False
    url = 'https://api.bilibili.com/x/player/playurl'
    cid = getcid(bvid, p_num)
    data = {
        'bvid': bvid,
        'cid': cid,
        'qn': 120,
        'fourk': 1
    }
    r = requests.get(url, headers=getHeader(), params=data)
    content = json.loads(r.text)
    if content['code'] == 0:
        support_formats = content['data']['support_formats']
        support_list = []
        for item in support_formats:
            support_list.append(item['quality'])
        return support_list
    else:
        return False