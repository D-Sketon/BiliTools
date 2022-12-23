#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os

from Parse.acrcloud.recognizer import ACRCloudRecognizeType
from Parse.acrcloud.recognizer import ACRCloudRecognizer
# 开始识别刚刚下载的一个flv并从test中删除
from Spider.getVideo import getVideoByBvid


def musicRecognize(file):
    file = os.path.join('Download', file)
    return getBgm(file)


def getBgm(testfile):
    config = {
        'host': 'identify-cn-north-1.acrcloud.cn',
        'access_key': '请输入你的access_key',
        'access_secret': '请输入你的access_secret',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,
        # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug': False,
        'timeout': 10  # seconds
    }

    re = ACRCloudRecognizer(config)

    jsonList = []
    musicSet = set()
    for i in range(int(ACRCloudRecognizer.get_duration_ms_by_file(testfile) / 30000)):
        resdict = json.loads(re.recognize_by_file(testfile, i * 30, 30))
        jsonList.append(resdict)

    for item in jsonList:
        if item['status']['code'] == 0:
            musicSet.add(str("歌曲名：" + item['metadata']['music'][0]['title'] + ' ' + "作者名：" +
                             item['metadata']['music'][0]['artists'][0]['name'] + "\n"))
    return musicSet


def parseFile(fileList):
    resultList = []
    for file in fileList:
        if file.startswith("BV"):
            bvid = file[0:12]
            data = parseBvAndTitle(getVideoByBvid(bvid))
            data['file'] = file
            resultList.append(data)
            pass
        else:
            data = {
                'pic': '',
                'title': '',
                'file': file
            }
            resultList.append(data)
    return resultList


def parseBvAndTitle(jsonString):
    dictionary = json.loads(jsonString)
    if dictionary["code"] != 0:
        return False
    data = {
        "file": "",
        'title': dictionary['data']['title'],
        'pic': dictionary['data']['pic']
    }
    return data
