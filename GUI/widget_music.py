import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QHeaderView
from qtpy import QtGui

from Parse.musicRecognize import musicRecognize, parseFile
from Spider.getData import *


class Widget_Music(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.fileList = []
        downloadPath = "Download"
        self.fileList = os.listdir(downloadPath)
        self.loadList = []
        self.model = QStandardItemModel(len(self.loadList), 3)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['封面', '标题', 'BV号'])  # 设置每列标题
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(930, 700)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 931, 701))
        self.widget.setObjectName("widget")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(20, 60, 890, 400))
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
        self.text_outputinfo = QtWidgets.QTextBrowser(self.widget)
        self.text_outputinfo.setEnabled(True)
        self.text_outputinfo.setGeometry(QtCore.QRect(20, 480, 890, 181))
        self.text_outputinfo.setObjectName("text_outputinfo")
        self.retranslateUi(self)

        '''通过tag查询视频'''
        self.tableView.doubleClicked.connect(self.open_url)
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

    '''加载动态表格'''

    def loadTable(self):
        self.model = QStandardItemModel(len(self.loadList), 3)  # 创建 行和列 固定的 模板
        self.model.setHorizontalHeaderLabels(['封面', '标题', 'BV号'])  # 设置每列标题
        i = 0
        session = requests.Session()
        for item in self.loadList:
            pic = QStandardItem()
            url = item['pic'] + "@170w_100h_1c.webp"
            r = session.get(url)
            pixmap = QPixmap()
            pixmap.loadFromData(r.content)
            icon = QIcon(pixmap)
            pic.setIcon(QIcon(icon))
            self.model.setItem(i, 0, pic)
            title = QStandardItem(item['title'])
            title.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            title.setFont(QFont('Microsoft YaHei UI', 12))
            self.model.setItem(i, 1, title)
            bvid = QStandardItem(item['file'])
            bvid.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.model.setItem(i, 2, bvid)
            QApplication.processEvents()
            i += 1
        self.tableView.setModel(self.model)
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(1, 500)
        self.tableView.horizontalHeader().setMinimumSectionSize(5)
        self.tableView.verticalHeader().setHidden(True)
        self.tableView.horizontalHeader().setHidden(True)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for j in range(len(self.loadList)):
            self.tableView.setRowHeight(j, 100)

    def showEvent(self, e):
        downloadPath = "Download"
        self.fileList = os.listdir(downloadPath)
        self.loadList = parseFile(self.fileList)
        self.loadTable()

    def open_url(self, index):
        self.loadList = parseFile(self.fileList)
        index = index.row()
        path = self.loadList[index]['file']
        set = musicRecognize(path)
        for item in set:
            cursor = self.text_outputinfo.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.insertText(item)
            self.text_outputinfo.setTextCursor(cursor)
        if not set:
            cursor = self.text_outputinfo.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.insertText("很遗憾，没有搜索到歌曲信息~\n")
            self.text_outputinfo.setTextCursor(cursor)
