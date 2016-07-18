# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：列举之前向导的用户设定
'''
import app
from PyQt4.QtGui import QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QListWidget,QDateEdit,QFileDialog
from PyQt4.QtCore import QStringList,Qt,QDate

class PanelPage(QWizardPage):

    def __init__(self):
        super(PanelPage,self).__init__()
        self.setTitle('生成信息')
        self.setSubTitle('显示工程配置的简要信息和即将生成的文件')

    def initializePage(self):
        super(PanelPage, self).initializePage()

        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        row0 = QHBoxLayout()
        lable0 = QLabel('  依赖库：')
        lable0.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.lw_files = QListWidget()
        items0 = QStringList()
        for moudel in app.g_configurations.libs:
            items0.append(moudel['name'])
        self.lw_files.addItems(items0)
        row0.addWidget(lable0)
        row0.addWidget(self.lw_files)

        row1 = QHBoxLayout()
        lable1 = QLabel('工程文件：')
        lable1.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.lw_files = QListWidget()
        items1 = QStringList()
        for file in app.g_configurations.config['files']:
            items1.append(file['target'])
        self.lw_files.addItems(items1)
        row1.addWidget(lable1)
        row1.addWidget(self.lw_files)

        rootLayout.addLayout(row0)
        rootLayout.addLayout(row1)
        self.setLayout(rootLayout)

    def validatePage(self):
        return True