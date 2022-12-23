# https://www.zhihu.com/question/381784377/answer/1099438784
import re

table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def bvToav(x):
    """

    :param x: e.g. BV17x411w7KC
    :return: e.g. 170001
    """
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - add) ^ xor


def avTobv(x):
    """

    :param x: e.g. 170001
    :return: e.g. BV17x411w7KC
    """
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x // 58 ** i % 58]
    return ''.join(r)


def parsemid(mid):
    bvid_pattern = re.compile(r'BV[0-9A-Za-z]{10}')
    aid_pattern = re.compile(r'av[0-9]+')
    if bvid_pattern.fullmatch(mid) or aid_pattern.fullmatch(mid.lower()):
        if bvid_pattern.fullmatch(mid):
            return mid
        else:
            return avTobv(int(mid[2:]))
    else:
        return False
