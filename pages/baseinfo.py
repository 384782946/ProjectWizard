# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：工程信息
'''

from PyQt4.QtGui import QWizard,QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QFileDialog,QComboBox
from PyQt4.QtCore import QString,QStringList,SIGNAL
import app
import os
import json

class BaseInfoPage(QWizardPage):

    def __init__(self):
        super(BaseInfoPage,self).__init__()

        self.setTitle('工程配置')
        self.setSubTitle('设置工程的参数')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        self.project_name = ""
        self.project_dir = ""
        self.completed = False

        row1 = QHBoxLayout()
        lable1 = QLabel('工程名称：')
        self.et_project_name = QLineEdit()
        self.et_project_name.textChanged.connect(self.on_text_changed)
        row1.addWidget(lable1)
        row1.addWidget(self.et_project_name)
        row1.addSpacing(200)

        # row2 = QHBoxLayout()
        # lable2 = QLabel('工程位置：')
        # self.et_project_location = QLineEdit()
        # self.et_project_location.textChanged.connect(self.on_text_changed)
        # self.et_project_location.setReadOnly(True)
        # btn_location = QPushButton('...')
        # btn_location.setFixedWidth(50)
        # btn_location.clicked.connect(self.getSavePath)
        # row2.addWidget(lable2)
        # row2.addWidget(self.et_project_location)
        # row2.addWidget(btn_location)

        row3 = QHBoxLayout()
        lable3 = QLabel('源模板  ：')
        self.cb_wizard_type = QComboBox()
        items = QStringList()
        for key in app.g_templates:
            items.append(key)
        self.cb_wizard_type.addItems(items)
        row3.addWidget(lable3)
        row3.addWidget(self.cb_wizard_type)
        row3.addStretch(0)

        row4 = QHBoxLayout()
        lable4 = QLabel('平台类型：')
        self.cb_platform_type = QComboBox()
        items_platform = QStringList()
        items_platform.append('Win')
        items_platform.append('Linux(32位)')
        items_platform.append('Linux(64位)')
        self.cb_platform_type.addItems(items_platform)
        row4.addWidget(lable4)
        row4.addWidget(self.cb_platform_type)
        row4.addStretch(0)

        row5 = QHBoxLayout()
        lable5 = QLabel('组件类型：')
        self.cb_component_type = QComboBox()
        items_component_type = QStringList()
        items_component_type.append('服务')
        items_component_type.append('窗口')
        self.cb_component_type.addItems(items_component_type)
        row5.addWidget(lable5)
        row5.addWidget(self.cb_component_type)
        row5.addStretch(0)

        rootLayout.addLayout(row1)
        #rootLayout.addLayout(row2)
        rootLayout.addLayout(row3)
        rootLayout.addLayout(row4)
        rootLayout.addLayout(row5)
        self.setLayout(rootLayout)

    def initializePage(self):
        super(BaseInfoPage, self).initializePage()
        if app.g_configurations.initialized:
            self.et_project_name.setText(app.g_configurations.project_name)
            if app.g_configurations.platform_type == "win32":
                self.cb_platform_type.setCurrentIndex(0)
            elif app.g_configurations.platform_type == "linux":
                if app.g_configurations.platform_level == "x86_32":
                    self.cb_platform_type.setCurrentIndex(1)
                else:
                    self.cb_platform_type.setCurrentIndex(2)

            index = self.cb_wizard_type.findText(app.g_configurations.template_source)
            self.cb_wizard_type.setCurrentIndex(index)

            if app.g_configurations.component_type == "server":
                self.cb_component_type.setCurrentIndex(0)
            else:
                self.cb_component_type.setCurrentIndex(1)

    # def getSavePath(self):
    #     path = QFileDialog.getExistingDirectory()
    #     self.et_project_location.setText(path)

    def test_completed(self):
        project_name = self.et_project_name.text().trimmed()
        #project_dir = self.et_project_location.text().trimmed()
        #return not project_name.isEmpty() and not project_dir.isEmpty()
        return not project_name.isEmpty()

    def on_text_changed(self,text):
        self.isComplete()

    def isComplete(self):
        ret = self.test_completed()
        if ret != self.completed:
            self.completed = ret
            self.emit(SIGNAL("completeChanged()"))
        return ret

    def validatePage(self):
        project_name = self.et_project_name.text().trimmed()
        #project_dir = self.et_project_location.text().trimmed()
        wizard_template = self.cb_wizard_type.currentText()
        platform_type = self.cb_platform_type.currentIndex()
        component_type = self.cb_component_type.currentIndex()

        app.g_configurations.project_name = app.QString2str(project_name)
        #app.g_configurations.project_location = app.QString2str(project_dir)
        app.g_configurations.template_source = app.QString2str(wizard_template)

        if platform_type == 1:
            app.g_configurations.platform_type = "linux"
            app.g_configurations.platform_level = "x86_32"
        elif platform_type == 2:
            app.g_configurations.platform_type = "linux"
            app.g_configurations.platform_level = "x86_64"
        else:
            app.g_configurations.platform_type = "win32"
            app.g_configurations.platform_level = "x86_32"

        if component_type == 0:
            app.g_configurations.component_type = "server"
        elif component_type == 1:
            app.g_configurations.component_type = "window"

        template_name = app.g_configurations.template_source
        template_dir = app.g_pwd + os.sep + 'templates' + os.sep + template_name
        with open(template_dir + os.sep + 'config.json', 'r') as f:
            app.g_configurations.config_content = f.read()
        return True