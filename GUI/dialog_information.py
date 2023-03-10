# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_information.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QDialog
from qtpy import QtCore, QtWidgets, QtGui

from Spider.getBiliInfo import parseAllInfo, getBiliUserUid, getBiliUserInfo
from Spider.getHeader import readExistCookie


class Dialog_Information(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog_information")
        self.setFixedSize(500, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/bili.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.widget_up = QtWidgets.QWidget(self)
        self.widget_up.setGeometry(QtCore.QRect(0, 0, 501, 121))
        self.widget_up.setObjectName("widget_up")
        self.label_face = QtWidgets.QLabel(self.widget_up)
        self.label_face.setGeometry(QtCore.QRect(210, 20, 80, 80))
        self.label_face.setObjectName("label_face")
        self.widget_down = QtWidgets.QWidget(self)
        self.widget_down.setGeometry(QtCore.QRect(0, 120, 501, 311))
        self.widget_down.setObjectName("widget_down")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget_down)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 480, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_sex = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sex.setText("")
        self.label_sex.setObjectName("label_sex")
        self.gridLayout.addWidget(self.label_sex, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_level = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_level.setText("")
        self.label_level.setObjectName("label_level")
        self.gridLayout.addWidget(self.label_level, 5, 1, 1, 1)
        self.label_coins = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_coins.setText("")
        self.label_coins.setObjectName("label_coins")
        self.gridLayout.addWidget(self.label_coins, 4, 1, 1, 1)
        self.label_birthday = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_birthday.setText("")
        self.label_birthday.setObjectName("label_birthday")
        self.gridLayout.addWidget(self.label_birthday, 2, 1, 1, 1)
        self.label_sign = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sign.setText("")
        self.label_sign.setObjectName("label_sign")
        self.label_sign.setWordWrap(True)
        self.gridLayout.addWidget(self.label_sign, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(15, 15, 31, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.widget_down.setStyleSheet('''
        QWidget{
            background-color: #EAEAEA;
            font-family: "Microsoft YaHei";
            border-bottom-left-radius:15px;
            border-bottom-right-radius:15px;
        }   
                        ''')
        self.widget_up.setStyleSheet('''
        QWidget{
            background-color: #222b2e;
            font-family: "Microsoft YaHei";
            border-top-left-radius:15px;
            border-top-right-radius:15px;
        }   
                                ''')
        self.setWindowOpacity(0.95)  # ?????????????????????
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # ????????????????????????
        self.pushButton.setFixedSize(25, 25)
        self.pushButton.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')

    def retranslateUi(self, Dialog_information):
        _translate = QtCore.QCoreApplication.translate
        Dialog_information.setWindowTitle(_translate("Dialog_information", "????????????"))
        self.label_face.setText(_translate("Dialog_information", "?????????"))
        self.label_3.setText(_translate("Dialog_information", "??????"))
        self.label.setText(_translate("Dialog_information", "?????????"))
        self.label_4.setText(_translate("Dialog_information", "????????????"))
        self.label_2.setText(_translate("Dialog_information", "??????"))
        self.label_7.setText(_translate("Dialog_information", "?????????"))
        self.label_8.setText(_translate("Dialog_information", "??????"))

    def loadInformation(self):
        uid = getBiliUserUid(readExistCookie())
        if uid:
            information = parseAllInfo(getBiliUserInfo(uid))
            if information:
                self.label_sign.setText(information['sign'])
                self.label_birthday.setText(information['birthday'])
                self.label_name.setText(information['name'])
                self.label_coins.setText(str(information['coins']))
                self.label_sex.setText(information['sex'])
                self.label_level.setText(str(information['level']) + "???")
                r = requests.get(information['face'])
                photo = QPixmap()
                photo.loadFromData(r.content)
                pixmap = QPixmap(200, 200)
                pixmap.fill(Qt.transparent)
                painter = QPainter(pixmap)
                painter.begin(self)  # ?????????????????????begin(self)???end()?????????
                painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)  # ?????????????????????????????????????????????
                path = QPainterPath()
                path.addEllipse(0, 0, 200, 200)  # ????????????
                painter.setClipPath(path)
                painter.drawPixmap(0, 0, 200, 200, photo)
                painter.end()
                self.label_face.setPixmap(pixmap)
                self.label_face.setScaledContents(True)

    def showEvent(self, e):
        self.loadInformation()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # ?????????????????????????????????
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # ??????????????????
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
