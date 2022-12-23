from Spider.doFavFolder import *


def parseFavFolderList(jsonString):
    list = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]["list"]:
        data = {
            'title': elem["title"],
            'id': str(elem["id"])
        }
        list.append(data)
    return list


def parseFavFolder(jsonString):
    list = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    if not dictionary['data']['medias']:
        return False
    for elem in dictionary['data']['medias']:
        data = {
            'title': elem["title"],
            'bvid': elem['bvid'],
            'pic': elem['cover'],

            'ctime': elem['ctime'],
            'play': elem['cnt_info']['play'],
            'collect': elem['cnt_info']['collect'],
            'danmaku': elem['cnt_info']['danmaku']
        }
        list.append(data)
    return list

