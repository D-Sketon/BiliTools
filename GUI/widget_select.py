import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QSize, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QHeaderView, QMessageBox

from GUI.widget_download import ThreadForDownload
from Parse.parseData import *
from Spider.getData import *


class Widget_Select(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.popularList = []
        self.popularpreciousList = []
        self.popularSeriesList = []
        self.rankingList = []
        self.loadList = []
        self.historyList = []
        self.threadList = []
        self.windownum = 0
        self.ip = False
        self.port = False
        self.model = QStandardItemModel(0, 3)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['封面', '标题', 'BV号'])  # 设置每列标题
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(930, 700)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 931, 701))
        self.widget.setObjectName("widget")
        self.search = QtWidgets.QPushButton(self.widget)
        self.search.setGeometry(QtCore.QRect(490, 70, 100, 35))
        self.search.setObjectName("search")
        self.download = QtWidgets.QPushButton(self.widget)
        self.download.setGeometry(QtCore.QRect(650, 70, 100, 35))
        self.download.setObjectName("download")
        self.label_tag = QtWidgets.QLabel(self.widget)
        self.label_tag.setGeometry(QtCore.QRect(20, 70, 120, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_tag.setFont(font)
        self.label_tag.setObjectName("label_tag")
        self.tag1 = QtWidgets.QTextEdit(self.widget)
        self.tag1.setGeometry(QtCore.QRect(150, 70, 100, 35))
        self.tag1.setObjectName("tag1")
        self.tag2 = QtWidgets.QTextEdit(self.widget)
        self.tag2.setGeometry(QtCore.QRect(260, 70, 100, 35))
        self.tag2.setObjectName("tag2")
        self.tag3 = QtWidgets.QTextEdit(self.widget)
        self.tag3.setGeometry(QtCore.QRect(370, 70, 100, 35))
        self.tag3.setObjectName("tag3")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(20, 170, 890, 440))
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(1, 550)
        self.tableView.horizontalHeader().setMinimumSectionSize(5)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.verticalHeader().setHidden(True)
        self.tableView.horizontalHeader().setHidden(True)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.tableView.setIconSize(QSize(170, 100))
        self.retranslateUi(self)

        '''通过tag查询视频'''
        self.search.clicked.connect(self.tagSearch)
        self.tableView.doubleClicked.connect(self.open_url)
        self.download.clicked.connect(self.video_download)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.widget.setStyleSheet('''
        QWidget{
            background-color: #FFFFFF;
            font-family: "Microsoft YaHei";
            border-top-right-radius:15px;
        }   
        QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QTimeEdit, QDateEdit, QDateTimeEdit {
            border-width: 2px;
            border-radius: 8px;
            border-style: solid;
            border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
            background-color: #f4f4f4;
            color: #3d3d3d;
        }
        QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QTimeEdit:focus, QDateEdit:focus, QDateTimeEdit:focus {
            border-width: 2px;
            border-radius: 8px;
            border-style: solid;
            border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
            border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
            border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #85b7e3, stop:1 #9ec1db);
            border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
            background-color: #f4f4f4;
            color: #3d3d3d;
        }
        QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QTimeEdit:disabled, QDateEdit:disabled, QDateTimeEdit:disabled {
            color: #b9b9b9;
        }
        QRadioButton::indicator {
            height: 14px;
            width: 14px;
            border-style:solid;
            border-radius:7px;
            border-width: 1px;
        }
        QRadioButton::indicator:checked {
            border-color: #48a5fd;
            background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #48a5fd, stop:1 #48a5fd);
        }
        QRadioButton::indicator:!checked {
            border-color: #a9b7c6;
            background-color: #fbfdfa;
        }
        QPushButton, QToolButton, QCommandLinkButton{
            padding: 0 5px 0 5px;
            border-style: solid;
            border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
            border-width: 2px;
            border-radius: 8px;
            color: #616161;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #fbfdfd, stop:0.5 #ffffff, stop:1 #fbfdfd);
        }
        QPushButton::default, QToolButton::default, QCommandLinkButton::default{
            border: 2px solid transparent;
            color: #FFFFFF;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
        }
        QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{
            color: #3d3d3d;
        }
        QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{
            color: #aeaeae;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
        }
        QPushButton:disabled, QToolButton:disabled, QCommandLinkButton:disabled{
            color: #616161;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #dce7eb, stop:0.5 #e0e8eb, stop:1 #dee7ec);
        }
        QScrollBar:horizontal {
        	max-height: 10px;
        	border: 1px transparent grey;
        	margin: 0px 20px 0px 20px;
        	background: transparent;
        }
        QScrollBar:vertical {
        	max-width: 10px;
        	border: 1px transparent grey;
        	margin: 20px 0px 20px 0px;
        	background: transparent;
        }
        QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
        	background: #52595d;
        	border-style: transparent;
        	border-radius: 4px;
        	min-height: 25px;
        }
        QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {
        	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
        }
        QScrollBar::add-line, QScrollBar::sub-line {
            border: 2px transparent grey;
            border-radius: 4px;
            subcontrol-origin: margin;
            background: #b9b9b9;
        }
        QScrollBar::add-line:horizontal {
            width: 20px;
            subcontrol-position: right;
        }
        QScrollBar::add-line:vertical {
            height: 20px;
            subcontrol-position: bottom;
        }
        QScrollBar::sub-line:horizontal {
            width: 20px;
            subcontrol-position: left;
        }
        QScrollBar::sub-line:vertical {
            height: 20px;
            subcontrol-position: top;
        }
        QScrollBar::add-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed, QScrollBar::sub-line:vertical:pressed {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
        }
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        QScrollBar::up-arrow:vertical {
            image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);
        }
        QScrollBar::down-arrow:vertical {
            image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);
        }
        QScrollBar::left-arrow:horizontal {
            image: url(/usr/share/icons/Adwaita/16x16/actions/go-previous-symbolic.symbolic.png);
        }
        QScrollBar::right-arrow:horizontal {
            image: url(/usr/share/icons/Adwaita/16x16/actions/go-next-symbolic.symbolic.png);
        }

        ''')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.search.setText(_translate("MainWindow", "查询"))
        self.download.setText(_translate("MainWindow", "全部下载"))
        self.label_tag.setText(_translate("MainWindow", "根据tag筛选"))

    '''爬取综合热门'''

    def loadPopular(self):
        self.windownum = 1
        if len(self.popularList) == 0:
            text = getPopular(1, 20)
            aidList = parsePopular(text)
            bvAndTitleList = parseBvAndTitle(text)
            if not aidList or not bvAndTitleList:
                QMessageBox.critical(self, "错误", "抓取失败！")
                return
            dataList = []
            for i in range(len(aidList)):
                data = {
                    'aid': aidList[i],
                    'title': bvAndTitleList[i][0],
                    'bvid': bvAndTitleList[i][1],
                    'pic': bvAndTitleList[i][2]
                }
                dataList.append(data)
            self.loadTable(bvAndTitleList)
            self.t = ThreadForSelect(dataList, 1, self.ip, self.port)
            self.t.signal.connect(self.getCallBack)
            self.t.start()
        else:
            bvAndTitleList = []
            for items in self.popularList:
                list = []
                list.append(items['title'])
                list.append(items['bvid'])
                list.append(items['pic'])
                bvAndTitleList.append(list)
            self.loadList = self.popularList
            self.loadTable(bvAndTitleList)

    '''爬取入站必刷'''

    def loadPopularprecious(self):
        self.windownum = 2
        if len(self.popularpreciousList) == 0:
            text = getPopularPrecious(1, 12)
            aidList = parsePopularPrecious(text)
            bvAndTitleList = parseBvAndTitle(text)
            if not aidList or not bvAndTitleList:
                QMessageBox.critical(self, "错误", "抓取失败！")
                return
            dataList = []
            for i in range(len(aidList)):
                data = {
                    'aid': aidList[i],
                    'title': bvAndTitleList[i][0],
                    'bvid': bvAndTitleList[i][1],
                    'pic': bvAndTitleList[i][2]
                }
                dataList.append(data)
            self.loadTable(bvAndTitleList)
            self.t = ThreadForSelect(dataList, 2, self.ip, self.port)
            self.t.signal.connect(self.getCallBack)
            self.t.start()
        else:
            bvAndTitleList = []
            for items in self.popularpreciousList:
                list = []
                list.append(items['title'])
                list.append(items['bvid'])
                list.append(items['pic'])
                bvAndTitleList.append(list)
            self.loadList = self.popularpreciousList
            self.loadTable(bvAndTitleList)

    '''爬取每周必看'''

    def loadPopularSeries(self, week):
        self.windownum = 3
        text = getPopularSeries(int(week))
        aidList = parsePopular(text)
        bvAndTitleList = parseBvAndTitle(text)
        if not aidList or not bvAndTitleList:
            QMessageBox.critical(self, "错误", "抓取失败！")
            return
        dataList = []
        for i in range(len(aidList)):
            data = {
                'aid': aidList[i],
                'title': bvAndTitleList[i][0],
                'bvid': bvAndTitleList[i][1],
                'pic': bvAndTitleList[i][2]
            }
            dataList.append(data)
        self.loadTable(bvAndTitleList)
        self.t = ThreadForSelect(dataList, 3, self.ip, self.port)
        self.t.signal.connect(self.getCallBack)
        self.t.start()

    '''爬取排行榜'''

    def loadRanking(self, rid, type):
        self.windownum = 4
        text = getRanking(rid, type)
        aidList = parsePopular(text)
        bvAndTitleList = parseBvAndTitle(text)
        if not aidList or not bvAndTitleList:
            QMessageBox.critical(self, "错误", "抓取失败！")
            return
        dataList = []
        for i in range(len(aidList)):
            data = {
                'aid': aidList[i],
                'title': bvAndTitleList[i][0],
                'bvid': bvAndTitleList[i][1],
                'pic': bvAndTitleList[i][2]
            }
            dataList.append(data)
        self.loadTable(bvAndTitleList)
        self.t = ThreadForSelect(dataList, 4, self.ip, self.port)
        self.t.signal.connect(self.getCallBack)
        self.t.start()

    def loadHistory(self):
        self.windownum = 0
        if len(self.historyList) == 0:
            text = getHistory(1, 50)
            aidList = parseHistory(text)
            bvAndTitleList = parseHistoryBvAndTitle(text)
            if not aidList or not bvAndTitleList:
                QMessageBox.critical(self, "错误", "抓取失败！")
                return
            dataList = []
            for i in range(len(aidList)):
                data = {
                    'aid': aidList[i],
                    'title': bvAndTitleList[i][0],
                    'bvid': bvAndTitleList[i][1],
                    'pic': bvAndTitleList[i][2]
                }
                dataList.append(data)
            self.loadTable(bvAndTitleList)
            self.t = ThreadForSelect(dataList, 5, self.ip, self.port)
            self.t.signal.connect(self.getCallBack)
            self.t.start()
        else:
            bvAndTitleList = []
            for items in self.historyList:
                list = []
                list.append(items['title'])
                list.append(items['bvid'])
                list.append(items['pic'])
                bvAndTitleList.append(list)
            self.loadList = self.historyList
            self.loadTable(bvAndTitleList)

    def tagSearch(self):
        while self.t.isRunning == 1:
            pass
        tagAndTitle = []
        loadlist = []
        tag1 = self.tag1.toPlainText()
        tag2 = self.tag2.toPlainText()
        tag3 = self.tag3.toPlainText()
        if tag1 == "" and tag2 == "" and tag3 == "":
            QMessageBox.critical(self, "错误", "请至少填写一个tag！")
            return
        list = []
        if self.windownum == 0:
            list = self.historyList
        elif self.windownum == 1:
            list = self.popularList
        elif self.windownum == 2:
            list = self.popularpreciousList
        elif self.windownum == 3:
            list = self.popularSeriesList
        elif self.windownum == 4:
            list = self.rankingList
        for items in list:
            tagList = items['tag']
            for tag in tagList:
                if tag == tag1 or tag == tag2 or tag == tag3:
                    temp = []
                    temp.append(items['title'])  # 获得视频标题
                    temp.append(items['bvid'])  # 获得视频Bvid号
                    temp.append(items['pic'])  # 获得视频封面
                    tagAndTitle.append(temp)
                    data = {
                        'title': items['title'],
                        'bvid': items['bvid'],
                        'pic': items['pic']
                    }
                    loadlist.append(data)
                    break
        self.loadList = loadlist
        self.loadTable(tagAndTitle)

    '''加载动态表格'''

    def loadTable(self, list):
        self.model = QStandardItemModel(len(list), 3)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['封面', '标题', 'BV号'])  # 设置每列标题
        i = 0
        session = requests.Session()
        for item in list:
            pic = QStandardItem()
            url = item[2] + "@170w_100h_1c.webp"
            r = session.get(url)
            pixmap = QPixmap()
            pixmap.loadFromData(r.content)
            icon = QIcon(pixmap)
            pic.setIcon(QIcon(icon))
            self.model.setItem(i, 0, pic)
            title = QStandardItem(item[0])
            title.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            title.setFont(QFont('Microsoft YaHei UI', 12))
            self.model.setItem(i, 1, title)
            bvid = QStandardItem(item[1])
            bvid.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.model.setItem(i, 2, bvid)
            QApplication.processEvents()
            i += 1
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(1, 550)
        self.tableView.horizontalHeader().setMinimumSectionSize(5)
        self.tableView.verticalHeader().setHidden(True)
        self.tableView.horizontalHeader().setHidden(True)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for j in range(len(list)):
            self.tableView.setRowHeight(j, 100)

    def getCallBack(self, msg):
        self.loadList = msg
        if self.t.funNumber == 1:
            self.popularList = msg
        elif self.t.funNumber == 2:
            self.popularpreciousList = msg
        elif self.t.funNumber == 3:
            self.popularSeriesList = msg
        elif self.t.funNumber == 4:
            self.rankingList = msg
        elif self.t.funNumber == 5:
            self.historyList = msg
        self.t.isRunning = 0

    def open_url(self, index):
        index = index.row()
        bvid = self.loadList[index]['bvid']
        url = "https://www.bilibili.com/video/" + bvid
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def video_download(self):
        for items in self.loadList:
            bvid = items['bvid']
            qn = 80
            t = ThreadForDownload(bvid, 1, qn)
            t.start()
            self.threadList.append(t)


class ThreadForSelect(QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self, dataList, funNumber, ip, port):
        self.isRunning = 0
        self.dataList = dataList
        self.resultList = []
        self.funNumber = funNumber
        self.ip = ip
        self.port = port
        super(ThreadForSelect, self).__init__()

    def run(self):
        self.isRunning = 1
        t_list = []
        for items in self.dataList:
            t = MyThread(parseAndGetTag, (items, self.ip, self.port))
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()
        for t in t_list:
            self.resultList.append(t.get_result())
        self.signal.emit(self.resultList)


def parseAndGetTag(items, ip, port):
    aid = items['aid']
    bvid = items['bvid']
    title = items['title']
    pic = items['pic']
    tagList = parseTag(getTag(aid, ip, port))
    if not tagList:
        tagList = []
    data = {
        'tag': tagList,
        'bvid': bvid,
        'title': title,
        'pic': pic
    }
    return data


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)  # 等待线程执行完毕
        try:
            return self.result
        except Exception:
            return None

