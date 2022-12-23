import json
import threading

from Spider.getData import *
from Spider.getTag import getTag


def parsePopularPrecious(jsonString):
    popularPreciouslist = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]["list"]:
        popularPreciouslist.append(elem["aid"])
    return popularPreciouslist


def parsePopular(jsonString):
    popularList = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]["list"]:
        popularList.append(elem["aid"])
    return popularList


def parseHistory(jsonString):
    popularList = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]:
        popularList.append(elem["aid"])
    return popularList


def parseTag(jsonString):
    tagList = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]:
        tagList.append(elem["tag_name"])
    return tagList


def parseBvAndTitle(jsonString):
    bvList = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]["list"]:
        list = []
        list.append(elem["title"])
        list.append(elem["bvid"])
        list.append(elem['pic'])
        bvList.append(list)
    return bvList


def parseHistoryBvAndTitle(jsonString):
    bvList = []
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    for elem in dictionary["data"]:
        list = []
        list.append(elem["title"])
        list.append(elem["bvid"])
        list.append(elem['pic'])
        bvList.append(list)
    return bvList

