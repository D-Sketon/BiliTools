import os
import sys

from PyQt5.QtWidgets import QApplication

from GUI.mainWindow import Ui_MainWindow

if __name__ == '__main__':
    if not os.path.exists('Cookie'):
        file = open('Cookie', 'w')
        file.close()
    if not os.path.exists('Proxy'):
        file = open('Proxy', 'w')
        file.write("{}")
        file.close()
    if not os.path.exists('DownloadRec'):
        file = open('DownloadRec', 'w')
        file.write("{\"data\": []}")
        file.close()
    if not os.path.exists('Cover'):
        os.mkdir('Cover')
    if not os.path.exists('Download'):
        os.mkdir('Download')
    app = QApplication(sys.argv)  # 创建应用程序对象
    ui = Ui_MainWindow()
    ui.show()  # 显示主窗口
    sys.exit(app.exec_())  # 在主线程中退出
