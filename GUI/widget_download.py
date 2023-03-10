# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_download.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import subprocess
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

from Spider.download import *
from Utils.bv2av import parsemid


class Widget_Download(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(930, 700)
        self.widget_up = QtWidgets.QWidget(self)
        self.widget_up.setGeometry(QtCore.QRect(0, 0, 931, 231))
        self.widget_up.setObjectName("widget_up")
        self.label_videotitle = QtWidgets.QLabel(self.widget_up)
        self.label_videotitle.setGeometry(QtCore.QRect(40, 40, 901, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_videotitle.setFont(font)
        self.label_videotitle.setText("")
        self.label_videotitle.setObjectName("label_videotitle")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_up)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 160, 111, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_p_num = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_p_num.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_p_num.setObjectName("horizontalLayout_p_num")
        self.label_p_num = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_p_num.setObjectName("label_p_num")
        self.horizontalLayout_p_num.addWidget(self.label_p_num)
        self.lineEdit_p_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_p_num.setObjectName("lineEdit_p_num")
        self.horizontalLayout_p_num.addWidget(self.lineEdit_p_num)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_up)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 160, 751, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_qn = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_qn.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_qn.setSpacing(7)
        self.horizontalLayout_qn.setObjectName("horizontalLayout_qn")
        self.radioButton_360p = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_360p.setObjectName("radioButton_360p")
        self.horizontalLayout_qn.addWidget(self.radioButton_360p)
        self.radioButton_480p = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_480p.setObjectName("radioButton_480p")
        self.horizontalLayout_qn.addWidget(self.radioButton_480p)
        self.radioButton_720p = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_720p.setObjectName("radioButton_720p")
        self.horizontalLayout_qn.addWidget(self.radioButton_720p)
        self.radioButton_1080p = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_1080p.setObjectName("radioButton_1080p")
        self.horizontalLayout_qn.addWidget(self.radioButton_1080p)
        self.radioButton_1080pp = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_1080pp.setObjectName("radioButton_1080pp")
        self.horizontalLayout_qn.addWidget(self.radioButton_1080pp)
        self.radioButton_720p60f = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_720p60f.setObjectName("radioButton_720p60f")
        self.horizontalLayout_qn.addWidget(self.radioButton_720p60f)
        self.radioButton_1080p60f = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_1080p60f.setObjectName("radioButton_1080p60f")
        self.horizontalLayout_qn.addWidget(self.radioButton_1080p60f)
        self.radioButton_4k = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4k.setObjectName("radioButton_4k")
        self.horizontalLayout_qn.addWidget(self.radioButton_4k)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget_up)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 90, 751, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_input = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_input.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_input.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_input.setSpacing(100)
        self.horizontalLayout_input.setObjectName("horizontalLayout_input")
        self.lineEdit_inputmid = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_inputmid.sizePolicy().hasHeightForWidth())
        self.lineEdit_inputmid.setSizePolicy(sizePolicy)
        self.lineEdit_inputmid.setText("")
        self.lineEdit_inputmid.setObjectName("lineEdit_inputmid")
        self.horizontalLayout_input.addWidget(self.lineEdit_inputmid)
        self.pushButton_download = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout_input.addWidget(self.pushButton_download)
        self.widget_down = QtWidgets.QWidget(self)
        self.widget_down.setGeometry(QtCore.QRect(0, 230, 931, 471))
        self.widget_down.setObjectName("widget_down")
        self.text_outputinfo = QtWidgets.QTextBrowser(self.widget_down)
        self.text_outputinfo.setEnabled(True)
        self.text_outputinfo.setGeometry(QtCore.QRect(40, 30, 851, 401))
        self.text_outputinfo.setObjectName("text_outputinfo")

        self.retranslateUi(self)
        self.pushButton_download.clicked.connect(self.button_download)
        self.lineEdit_inputmid.returnPressed.connect(self.button_qndetect)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.widget_up.setStyleSheet('''
        QWidget{
            background-color: #A9BCC5;
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
                                                ''')
        self.widget_down.setStyleSheet('''
        QWidget{
            background-color: #FFFFFF;
            font-family: "Consolas";
            border-bottom-right-radius:15px;
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_p_num.setText(_translate("Form", "???P:"))
        self.lineEdit_p_num.setPlaceholderText(_translate("Form", "??????1P"))
        self.radioButton_360p.setText(_translate("Form", "360P"))
        self.radioButton_480p.setText(_translate("Form", "480P"))
        self.radioButton_720p.setText(_translate("Form", "720P"))
        self.radioButton_1080p.setText(_translate("Form", "1080P"))
        self.radioButton_1080pp.setText(_translate("Form", "1080P+"))
        self.radioButton_720p60f.setText(_translate("Form", "720P60"))
        self.radioButton_1080p60f.setText(_translate("Form", "1080P60"))
        self.radioButton_4k.setText(_translate("Form", "4K"))
        self.lineEdit_inputmid.setPlaceholderText(_translate("Form", "??????BV??????AV???"))
        self.pushButton_download.setText(_translate("Form", "??????"))

    def button_download(self):
        mid = self.lineEdit_inputmid.text()
        if not parsemid(mid):
            QMessageBox.critical(self, "??????", "BVID???AID???????????????")
            return
        else:
            mid = parsemid(mid)
        q_num = 1
        if len(self.lineEdit_p_num.text()) > 0:
            q_num = int(self.lineEdit_p_num.text())
        qn = 64
        if self.radioButton_360p.isChecked():
            qn = 16
        elif self.radioButton_480p.isChecked():
            qn = 32
        elif self.radioButton_720p.isChecked():
            qn = 64
        elif self.radioButton_1080p.isChecked():
            qn = 80
        elif self.radioButton_1080pp.isChecked():
            qn = 112
        elif self.radioButton_720p60f.isChecked():
            qn = 74
        elif self.radioButton_1080p60f.isChecked():
            qn = 116
        elif self.radioButton_4k.isChecked():
            qn = 120
        self.label_videotitle.setText(getVideoName(getVideoByBvid(mid)))
        self.t = ThreadForDownload(mid, q_num, qn)
        self.t.textWritten.connect(self.outputWritten)
        self.t.boxSignal.connect(self.box)
        self.t.start()

    def button_qndetect(self):
        mid = self.lineEdit_inputmid.text()
        if not parsemid(mid):
            QMessageBox.critical(self, "??????", "BVID???AID???????????????")
            return
        else:
            mid = parsemid(mid)
        q_num = 1
        if len(self.lineEdit_p_num.text()) > 0:
            q_num = int(self.lineEdit_p_num.text())
        support_list = qndetect(mid, q_num)
        if not support_list:
            QMessageBox.critical(self, "??????", "??????????????????")
            return
        self.radioButton_360p.setEnabled(True) if support_list.count(16) > 0 else self.radioButton_360p.setEnabled(
            False)
        self.radioButton_480p.setEnabled(True) if support_list.count(32) > 0 else self.radioButton_480p.setEnabled(
            False)
        self.radioButton_720p.setEnabled(True) if support_list.count(64) > 0 else self.radioButton_720p.setEnabled(
            False)
        self.radioButton_1080p.setEnabled(True) if support_list.count(80) > 0 else self.radioButton_1080p.setEnabled(
            False)
        self.radioButton_1080pp.setEnabled(True) if support_list.count(112) > 0 else self.radioButton_1080pp.setEnabled(
            False)
        self.radioButton_720p60f.setEnabled(True) if support_list.count(
            74) > 0 else self.radioButton_720p60f.setEnabled(
            False)
        self.radioButton_1080p60f.setEnabled(True) if support_list.count(
            116) > 0 else self.radioButton_1080p60f.setEnabled(
            False)
        self.radioButton_4k.setEnabled(True) if support_list.count(120) > 0 else self.radioButton_4k.setEnabled(
            False)
        self.label_videotitle.setText(getVideoName(getVideoByBvid(mid)))

    def outputWritten(self, text):
        cursor = self.text_outputinfo.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.text_outputinfo.setTextCursor(cursor)
        self.text_outputinfo.ensureCursorVisible()

    def box(self):
        QMessageBox.critical(self, "??????", "??????????????????")


class ThreadForDownload(QThread):
    textWritten = QtCore.pyqtSignal(str)
    boxSignal = QtCore.pyqtSignal()

    def __init__(self, bvid, p_num, qn):
        self.bvid = bvid
        self.p_num = p_num
        self.qn = qn
        super(ThreadForDownload, self).__init__()

    def run(self):
        url = download(self.bvid, self.p_num, self.qn)
        if not url:
            self.boxSignal.emit()
            return
        exe_path = r'aria2-1.36.0-win-64bit-build1\aria2c.exe'
        referer = "--referer=https://www.bilibili.com/video/" + self.bvid + "?p=" + str(self.p_num)
        out = self.bvid + "_p" + str(self.p_num) + ".flv"
        dir = "Download"
        popen = subprocess.Popen([exe_path,
                                  '-s16',
                                  '-x10',
                                  url,
                                  referer,
                                  "--out", out, "--dir", dir], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        while popen.poll() is None:
            r = popen.stdout.readline().decode('GBK')
            if len(r) > 0:
                self.textWritten.emit(str(r))
        quality = ""
        if self.qn == 16:
            quality = "360P"
        elif self.qn == 32:
            quality = "480P"
        elif self.qn == 64:
            quality = "720P"
        elif self.qn == 80:
            quality = "1080P"
        elif self.qn == 112:
            quality = "1080P+"
        elif self.qn == 74:
            quality = "720P60"
        elif self.qn == 116:
            quality = "1080P60"
        elif self.qn == 120:
            quality = "4K"

        data = {
            'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'title': getVideoName(getVideoByBvid(self.bvid)),
            'p_num': str(self.p_num),
            'qn': quality,
            'bvid': self.bvid,
            'status': '??????' if popen.returncode == 0 else "??????"
        }
        with open('DownloadRec', 'r') as f:
            content = json.load(f)
            content['data'].append(data)
            jsonString = json.dumps(content)
        with open('DownloadRec', 'w') as f:
            f.write(jsonString)
