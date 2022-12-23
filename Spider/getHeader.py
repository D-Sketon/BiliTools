import re

from Utils.crypto import decrypt


def getHeader():
    headers = {
        'Authority': 'api.bilibili.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
        'Cookie': readExistCookie(),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    return headers


def readExistCookie():
    try:
        with open('Cookie', 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content) > 0:
                content_decrypt = decrypt(content)
                pattern = re.compile(r'(?<=bili_jct=)[0-9a-z]+')
                match = pattern.search(content_decrypt)
                if match:
                    return content_decrypt
                else:
                    file = open("Cookie", 'w').close()
                    return False
            else:
                return False
    except:
        return False
