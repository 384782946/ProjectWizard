# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：框架模块选择
'''

import app
import os
import json
from PyQt4.QtGui import QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QCheckBox,QGridLayout,QFileDialog
from PyQt4.QtCore import SIGNAL,Qt

class FrameworkLibraryPage(QWizardPage):

    def __init__(self):
        super(FrameworkLibraryPage,self).__init__()
        self.completed = False
        self.setTitle('框架模块')
        self.setSubTitle('设置框架的模块引用')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        # row2 = QHBoxLayout()
        # lable2 = QLabel('框架根目录：')
        # self.et_framework_root = QLineEdit()
        # self.et_framework_root.setReadOnly(True)
        # btn_location = QPushButton('...')
        # btn_location.clicked.connect(self.on_select)
        # btn_location.setFixedWidth(50)
        # row2.addWidget(lable2)
        # row2.addWidget(self.et_framework_root)
        # row2.addWidget(btn_location)

        self.gLayout = QGridLayout()

        #rootLayout.addLayout(row2)
        rootLayout.addLayout(self.gLayout)
        self.setLayout(rootLayout)

    def initializePage(self):
        super(FrameworkLibraryPage, self).initializePage()
        exsits = []
        for moudel in app.g_configurations.modules:
            exsits.append(moudel['name'])

        self.checkboxs = []
        index = 0
        ret_json = app.render(app.g_configurations.config_content, config=app.g_configurations)
        app.g_configurations.config = json.loads(ret_json)
        for moudel in app.g_configurations.config['moudels']:
            checkBox = QCheckBox(moudel['name'])
            checkBox.setToolTip(moudel['description'])
            if moudel['buildin']:
                checkBox.setCheckState(Qt.Checked)
                checkBox.setEnabled(False)
            elif moudel['name'] in exsits:
                checkBox.setCheckState(Qt.Checked)
            else:
                checkBox.setCheckState(Qt.Unchecked)
            row = index / 3
            offset = index % 3
            self.gLayout.addWidget(checkBox, row, offset)
            self.checkboxs.append(checkBox)
            index += 1

    def validatePage(self):
        librarys = []
        for i in range(len(self.checkboxs)):
            if self.checkboxs[i].checkState() == 2:
                app.g_configurations.modules.append(app.g_configurations.config['moudels'][i])
                for lib in app.g_configurations.config['moudels'][i]['libs']:
                    librarys.append(lib)

        app.g_configurations.libs = librarys
        return True

    # def on_select(self):
    #     path = QFileDialog.getExistingDirectory()
    #     self.et_framework_root.setText(path)
    #     self.isComplete()

    def test_completed(self):
        return True

    def isComplete(self):
        ret = self.test_completed()
        if ret != self.completed:
            self.completed = ret
            self.emit(SIGNAL("completeChanged()"))
        return ret
