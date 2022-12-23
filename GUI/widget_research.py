import sys
import urllib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QSize, Qt
from PyQt5.QtGui import QStandardItem, QIcon, QPixmap, QStandardItemModel, QFont
from PyQt5.QtWidgets import QApplication, QHeaderView, QMessageBox

from GUI.widget_download import ThreadForDownload
from Parse.parseData import *
from Spider.getRecommend import getRecommend
from Utils.bv2av import parsemid


class Widget_Research(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.loadList = []
        self.tablelist = []
        self.threadList = []
        self.model = QStandardItemModel(0, 3)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['封面', '标题', 'BV号'])  # 设置每列标题
        self.ip = False
        self.port = False
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(930, 700)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 931, 701))
        self.widget.setObjectName("widget")
        self.centralwidget = QtWidgets.QWidget(self.widget)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(340, 115, 100, 35))
        self.search.setObjectName("search")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(560, 115, 100, 35))
        self.download.setObjectName("download")
        self.label_Bv = QtWidgets.QLabel(self.centralwidget)
        self.label_Bv.setGeometry(QtCore.QRect(20, 70, 120, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Bv.setFont(font)
        self.label_Bv.setObjectName("label_Bv")
        self.label_Tag = QtWidgets.QLabel(self.centralwidget)
        self.label_Tag.setGeometry(QtCore.QRect(320, 70, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Tag.setFont(font)
        self.label_Tag.setObjectName("label_Tag")
        self.label_Num = QtWidgets.QLabel(self.centralwidget)
        self.label_Num.setGeometry(QtCore.QRect(20, 115, 170, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Num.setFont(font)
        self.label_Num.setObjectName("label_Num")
        self.tag1 = QtWidgets.QTextEdit(self.centralwidget)
        self.tag1.setGeometry(QtCore.QRect(150, 70, 150, 35))
        self.tag1.setObjectName("tag1")
        self.tag2 = QtWidgets.QTextEdit(self.centralwidget)
        self.tag2.setGeometry(QtCore.QRect(450, 70, 100, 35))
        self.tag2.setObjectName("tag2")
        self.tag3 = QtWidgets.QTextEdit(self.centralwidget)
        self.tag3.setGeometry(QtCore.QRect(560, 70, 100, 35))
        self.tag3.setObjectName("tag3")
        self.tag4 = QtWidgets.QTextEdit(self.centralwidget)
        self.tag4.setGeometry(QtCore.QRect(670, 70, 100, 35))
        self.tag4.setObjectName("tag4")
        self.tag5 = QtWidgets.QTextEdit(self.centralwidget)
        self.tag5.setGeometry(QtCore.QRect(200, 115, 100, 35))
        self.tag5.setObjectName("tag4")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 200, 890, 400))
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

        '''通过Bvid,tag爬取固定数量的视频'''
        self.search.clicked.connect(self.click)
        self.tableView.doubleClicked.connect(self.open_url)
        self.download.clicked.connect(self.videodownload)
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
        self.label_Bv.setText(_translate("MainWindow", "视频Bv号"))
        self.label_Tag.setText(_translate("MainWindow", "视频tag"))
        self.label_Num.setText(_translate("MainWindow", "爬取视频数量"))
        self.download.setText(_translate("MainWindow", "全部下载"))

    def click(self):
        bvid = self.tag1.toPlainText()
        if not parsemid(bvid):
            QMessageBox.critical(self, "错误", "BVID或AID输入错误！")
            return
        else:
            bvid = parsemid(bvid)
        number = self.tag5.toPlainText()
        allDataList = getRecommend(str(bvid), int(number))  # 获取bv号和title
        self.t = ThreadForSelect(allDataList, self.ip, self.port)
        self.t.signal.connect(self.getCallBack)
        self.t.start()

    def tagSearch(self):
        tagAndTitle = []
        tag2 = self.tag2.toPlainText()
        tag3 = self.tag3.toPlainText()
        tag4 = self.tag4.toPlainText()
        for items in self.loadList:
            tagList = items['tag']
            for tag in tagList:
                if tag == tag2 or tag == tag3 or tag == tag4:
                    temp = []
                    temp.append(items['bvid'])  # 获得视频Bvid号
                    temp.append(items['title'])  # 获得视频标题
                    temp.append(items['pic'])
                    tagAndTitle.append(temp)
                    break
        self.tablelist = tagAndTitle
        self.loadTable(tagAndTitle)

    def loadTable(self, list):
        self.model = QStandardItemModel(len(list), 3)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['封面', '标题', 'BV号'])  # 设置每列标题
        i = 0
        for item in list:
            pic = QStandardItem()
            url = item[2]
            data = urllib.request.urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            icon = QIcon(pixmap)
            pic.setIcon(QIcon(icon))
            self.model.setItem(i, 0, pic)
            title = QStandardItem(item[1])
            title.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            title.setFont(QFont('Microsoft YaHei UI', 12))
            self.model.setItem(i, 1, title)
            bvid = QStandardItem(item[0])
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
        self.t.isRunning = 0
        self.tagSearch()

    def open_url(self, index):
        index = index.row()
        bvid = self.loadList[index]['bvid']
        url = "https://www.bilibili.com/video/" + bvid
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def videodownload(self):
        for items in self.loadList:
            bvid = items['bvid']
            qn = 80
            t = ThreadForDownload(bvid, 1, qn)
            t.start()
            self.threadList.append(t)


class ThreadForSelect(QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self, dataList, ip, port):
        self.isRunning = 0
        self.dataList = dataList
        self.resultList = []
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
    cid = items['cid']
    pic = items['pic']
    title = items['title']
    tagList = parseTag(getTag(aid, ip, port))
    if not tagList:
        tagList = []
    data = {
        'tag': tagList,
        'cid': cid,
        'bvid': bvid,
        'pic': pic,
        'title': title
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


# Only for test
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    ui = Widget_Research()
    ui.show()  # 显示主窗口
    sys.exit(app.exec_())  # 在主线程中退出
