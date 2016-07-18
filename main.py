#coding:utf-8
import sys
import os
import app
import mainwindow

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QTextCodec

def main():
    qapp = QApplication(sys.argv)
    tc = QTextCodec.codecForName('utf-8')
    QTextCodec.setCodecForCStrings(tc)
    QTextCodec.setCodecForLocale(tc)
    QTextCodec.setCodecForTr(tc)
    app.g_pwd = os.getcwd()
    print app.g_pwd

    #遍历目录
    tmpdirs = os.listdir(app.g_pwd + os.sep + 'templates')
    for tmpdir in tmpdirs:
        currentdir = app.g_pwd + os.sep + 'templates' + os.sep + tmpdir
        if os.path.isdir(currentdir) and os.path.exists(currentdir + os.sep + 'config.json'):
            app.g_templates.append(tmpdir)

    m = mainwindow.mainwindow()
    m.show()
    qapp.exec_()

if __name__ == "__main__":
    main()



