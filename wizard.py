# coding:utf-8

'''
作者：张潇健
日期：2016-6-13
概述：向导窗口
'''

from PyQt4.QtGui import QWizard,QWizardPage,QPixmap
from  PyQt4.QtCore import QDir,QFileInfo
from pages import baseinfo,qtlibrary,frameworklibrary,interface,panel
import os
import app
import json

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

class MyWizard(QWizard):
    '''
    向导类
    '''
    def __init__(self):
        super(MyWizard,self).__init__()
        self.setWindowTitle('框架工程向导')
        self.setWizardStyle(QWizard.MacStyle)
        self.setOption(QWizard.IndependentPages,True)
        #self.setPixmap(QWizard.BackgroundPixmap,QPixmap('bj.jpg'))
        self.addPage(baseinfo.BaseInfoPage())
        self.addPage(qtlibrary.QtLibraryPage())
        self.addPage(frameworklibrary.FrameworkLibraryPage())
        self.addPage(interface.InterfacePage())
        self.addPage(panel.PanelPage())
        self.button(QWizard.NextButton).setEnabled(False)
        self.setButtonText(QWizard.NextButton,'下一步')
        self.setButtonText(QWizard.BackButton, '上一步')
        self.setButtonText(QWizard.HelpButton, '帮助')
        self.setButtonText(QWizard.CancelButton, '取消')
        self.setButtonText(QWizard.FinishButton, '完成')

    def accept(self):
        # template_name = app.g_configurations.template_source
        # template_dir = app.g_pwd + os.sep + 'templates' + os.sep + template_name
        # for file in app.g_configurations.config['files']:
        #     sourcepath = template_dir + os.sep + file['source']
        #     targetdir = app.g_configurations.project_location + app.g_configurations.project_name
        #     targetpath =  targetdir + os.sep + file['target']
        #     fi = QFileInfo(targetpath)
        #     qdir = fi.absoluteDir()
        #     if not qdir.exists():
        #         qdir.mkpath(fi.absolutePath())
        #     with open(sourcepath,'r') as f:
        #         content = f.read()
        #         content = app.render(content, config = app.g_configurations)
        #     with open(targetpath,'w+') as f:
        #         f.write(content.encode('utf-8'))
        super(MyWizard, self).accept()

    def validateCurrentPage(self):
        print self.currentId()
        return super(MyWizard, self).validateCurrentPage()