from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from qtpy import QtGui

from Spider.getBiliInfo import *
from Utils.crypto import *


# https://blog.csdn.net/qq_39996837/article/details/105353998

def readCookie():
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
                    return False
    except:
        return False


class WebEngineView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super(WebEngineView, self).__init__(*args, **kwargs)
        # 绑定cookie被添加的信号槽
        self.page().profile().cookieStore().cookieAdded.connect(self.__onCookieAdd)
        self.cookies = {}

    def __onCookieAdd(self, cookie):
        name = cookie.name().data().decode('utf-8')
        value = cookie.value().data().decode('utf-8')
        self.cookies[name] = value

    # 获取cookie
    def getCookie(self):
        cookieStr = ''
        i = 0
        for key, value in self.cookies.items():
            if i == len(self.cookies.items()) - 1:
                cookieStr += (key + '=' + value)
            else:
                cookieStr += (key + '=' + value + '; ')
            i += 1
        return cookieStr

    windowList = []

    # def createWindow(self, QWebEnginePage_WebWindowType):
    #     new_webview = WebEngineView()
    #     new_window = GetCookie()
    #     new_window.setCentralWidget(new_webview)
    #     new_window.show()
    #     self.windowList.append(new_window)
    #     return new_webview


class GetCookie(QDialog):
    _signal = pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.webview = WebEngineView()
        self.webview.load(QUrl("https://passport.bilibili.com/login"))
        self.setupUi(self)

    def getCookieFromWeb(self):
        cookie = self.webview.getCookie()
        return cookie

    def getBiliCookie(self):
        try:
            with open('Cookie', 'r', encoding='utf-8') as f:
                content = f.read()
                if len(content) == 0:
                    cookie = self.getCookieFromWeb()
                    pattern = re.compile(r'(?<=bili_jct=)[0-9a-z]+')
                    match = pattern.search(cookie)
                    if match:
                        with open('Cookie', 'w', encoding='utf-8') as n_f:
                            n_f.write(encrypt(cookie))
        except:
            cookie = self.getCookieFromWeb()
            pattern = re.compile(r'(?<=bili_jct=)[0-9a-z]+')
            match = pattern.search(cookie)
            if match:
                with open('Cookie', 'w', encoding='utf-8') as n_f:
                    n_f.write(encrypt(cookie))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1200, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/bili.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登录"))

    def closeEvent(self, event):
        self.getBiliCookie()
        cookie = readCookie()
        faceurl = ""
        if cookie:
            jsonstring = getBiliUserInfo(getBiliUserUid(cookie))
            username = parseUsername(jsonstring)
            faceurl = parseFacePhoto(jsonstring)
        else:
            username = "<u>未登录</u>"
        self._signal.emit(username, faceurl)
