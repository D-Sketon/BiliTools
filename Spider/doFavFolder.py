from Spider.getBiliInfo import *
from Spider.getHeader import *


def addFavFolder(title, intro, privacy):
    """添加收藏夹

    :param title:收藏夹标题
    :param intro:收藏夹简介
    :param privacy:是否公开收藏夹，0表示公开，1表示私密
    :return:返回response json
    """
    csrf = getBiliCsrf(readExistCookie())
    url = 'https://api.bilibili.com/x/v3/fav/folder/add'
    data = {
        'title': title,
        'intro': intro,
        'privacy': privacy,
        'cover': '',
        'csrf': csrf
    }
    r = requests.post(url, headers=getHeader(), params=data)
    return r.text


def delFavFolder(media_ids):
    """删除收藏夹

    :param media_ids:收藏夹id
    :return:返回response json
    """
    csrf = getBiliCsrf(readExistCookie())
    url = 'https://api.bilibili.com/x/v3/fav/folder/del'
    data = {
        'media_ids': media_ids,
        'platform': 'web',
        'jsonp': 'jsonp',
        'csrf': csrf
    }
    r = requests.post(url, headers=getHeader(), params=data)
    return r.text


def getFavFolder(media_id, page_num, page_per_num):
    """获得收藏夹视频

    :param media_id:收藏夹id
    :param page_num:页数
    :param page_per_num:每页条数
    :return:返回response json
    """
    url = 'https://api.bilibili.com/x/v3/fav/resource/list'
    data = {
        'media_id': media_id,
        'pn': page_num,
        'ps': page_per_num,
        'keyword': '',
        'order': 'mtime',
        'type': 0,
        'tid': 0,
        'platform': 'web',
        'jsonp': 'jsonp'
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def getFavFolderList(up_mid):
    """

    :param up_mid:用户UID
    :return:返回response json
    """
    url = 'https://api.bilibili.com/x/v3/fav/folder/created/list-all'
    data = {
        'up_mid': up_mid,
        'jsonp': 'jsonp'
    }
    r = requests.get(url, headers=getHeader(), params=data)
    return r.text


def copyFavResource(src_media_id, tar_media_id, mid, resources):
    """复制收藏夹内视频到另一个收藏夹中

    :param src_media_id:源收藏夹id
    :param tar_media_id:目标收藏夹id
    :param mid:用户UID
    :param resources:视频av号，使用str类型
    :return:返回response json
    """
    csrf = getBiliCsrf(readExistCookie())
    url = 'https://api.bilibili.com/x/v3/fav/resource/copy'
    data = {
        'src_media_id': src_media_id,
        'tar_media_id': tar_media_id,
        'mid': mid,
        'resources': resources,
        'platform': 'web',
        'jsonp': 'jsonp',
        'csrf': csrf
    }
    r = requests.post(url, headers=getHeader(), params=data)
    return r.text


def moveFavResource(src_media_id, tar_media_id, resources):
    """移动收藏夹内视频到另一个收藏夹中

    :param src_media_id:源收藏夹id
    :param tar_media_id:目标收藏夹id
    :param resources:视频av号，使用str类型
    :return:返回response json
    """
    csrf = getBiliCsrf(readExistCookie())
    url = 'https://api.bilibili.com/x/v3/fav/resource/move'
    data = {
        'src_media_id': src_media_id,
        'tar_media_id': tar_media_id,
        'resources': resources,
        'platform': 'web',
        'jsonp': 'jsonp',
        'csrf': csrf
    }
    r = requests.post(url, headers=getHeader(), params=data)
    return r.text


def batch_delFavFolder(resources, media_id):
    """删除收藏夹内指定视频

    :param resources: 视频AV号
    :param media_id: 收藏夹id
    :return:
    """
    csrf = getBiliCsrf(readExistCookie())
    url = 'https://api.bilibili.com/x/v3/fav/resource/batch-del'
    data = {
        'resources': resources,
        'media_id': media_id,
        'platform': 'web',
        'jsonp': 'jsonp',
        'csrf': csrf
    }
    r = requests.post(url, headers=getHeader(), params=data)
    return r.text

