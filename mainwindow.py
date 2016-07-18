# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：程序主窗口
'''

import os
import copy
import json
import app
import wizard

from PyQt4 import QtCore,QtGui,Qt
from configuration import Configuration
from PyQt4.QtCore import QString,QStringList,QFileInfo,QDir
from PyQt4.QtGui import QVBoxLayout,QHBoxLayout,QListWidget,QWidget,QTreeWidget,QPushButton,QLabel, \
    QTreeWidgetItem,QAbstractItemView,QLineEdit,QFileDialog,QGroupBox,QMessageBox

class mainwindow(QtGui.QMainWindow):
    '''主窗体'''

    def __init__(self):
        super(mainwindow,self).__init__()
        self.setWindowTitle('组件设计工具')
        self.showMaximized()
        self.menuBar().show()
        self.createMenus()

        cwHLayout = QHBoxLayout()
        lLayout = QVBoxLayout()
        rLayout = QVBoxLayout()
        self.lw = QListWidget()
        self.lw.setSelectionMode(QAbstractItemView.SingleSelection )

        lLayout.addWidget(self.lw)
        self.lw.itemSelectionChanged.connect(self.on_select)

        lGroup = QGroupBox('项目列表')
        lGroup.setLayout(lLayout)
        cwHLayout.addWidget(lGroup,3)
        cwHLayout.addLayout(rLayout,7)

        tLayout = QVBoxLayout()
        bLayout = QVBoxLayout()

        tGroup = QGroupBox('配置信息')
        self.bGroup = QGroupBox('生成代码')
        tGroup.setLayout(tLayout)
        self.bGroup.setLayout(bLayout)
        self.bGroup.setEnabled(False)

        rLayout.addWidget(tGroup)
        rLayout.addWidget(self.bGroup)

        self.tw_config = QTreeWidget()
        headerLabels = QStringList()
        headerLabels.append('项目')
        headerLabels.append('值')
        self.tw_config.setHeaderLabels(headerLabels)
        thLayout = QHBoxLayout()
        thLayout.addStretch(0)
        modify_btn = QPushButton('修改')
        modify_btn.clicked.connect(self.on_modify)
        thLayout.addWidget(modify_btn)

        tLayout.addWidget(self.tw_config)
        tLayout.addLayout(thLayout)

        bhLayout = QHBoxLayout()
        bhLayout.addStretch(0)
        gen_btn = QPushButton('生成')
        gen_btn.clicked.connect(self.on_gen)
        bhLayout.addWidget(gen_btn)

        row1 = QHBoxLayout()
        lable1 = QLabel('工程名称：')
        self.et_project_name = QLineEdit()
        row1.addSpacing(10)
        row1.addWidget(lable1)
        row1.addWidget(self.et_project_name)
        row1.addStretch(0)

        row2 = QHBoxLayout()
        lable2 = QLabel('工程位置：')
        self.et_project_location = QLineEdit()
        self.et_project_location.setReadOnly(True)
        btn_location = QPushButton('...')
        btn_location.setFixedWidth(50)
        btn_location.clicked.connect(self.getProjectLocation)
        row2.addSpacing(10)
        row2.addWidget(lable2)
        row2.addWidget(self.et_project_location)
        row2.addWidget(btn_location)
        row2.addStretch(0)

        bLayout.addLayout(row1)
        bLayout.addLayout(row2)
        bLayout.addLayout(bhLayout)

        cw = QWidget()
        cw.setLayout(cwHLayout)
        self.setCentralWidget(cw)
        self._initByConfig()
        self.setMinimumSize(400,200)

    def _initByConfig(self):
        '''初始化'''
        pass

    def createMenus(self):
        '''创建菜单'''
        menueBar = self.menuBar()
        menuSys = menueBar.addMenu('系统')
        actNew = menuSys.addAction('新建工程')
        actOpen = menuSys.addAction('打开工程')
        actNew.triggered.connect(self.on_new)
        actOpen.triggered.connect(self.on_open)
        menueBar.addMenu(menuSys)

    def on_new(self):
        '''新建向导'''
        app.g_configurations = Configuration()  # 用来渲染的配置数据
        dlg = wizard.MyWizard()
        if dlg.exec_():
            app.g_configurations.initialized = True
            app.g_projects.append(app.g_configurations)
            self.lw.addItem(app.g_configurations.project_name)

    def getProjectLocation(self):
        '''获取项目路径'''
        path = QFileDialog.getExistingDirectory()
        self.et_project_location.setText(path)

    def on_open(self):
        '''打开现有配置'''
        fileName = QFileDialog.getOpenFileName()
        with open(app.QString2str(fileName), 'r') as f:
            content = f.read()
        config = json.loads(content)
        app.g_projects.append(config)
        self.lw.addItem(config['project_name'])

    def on_select(self):
        '''选取配置'''
        index = self.lw.currentRow()
        if index < app.g_projects:
            self.bGroup.setEnabled(True)
            self.currentConfig = app.g_projects[index]
            self.showConfigInfo(self.currentConfig)

    def showConfigInfo(self,cf):
        '''显示配置信息'''
        self.tw_config.clear()
        self.et_project_name.setText(cf.project_name)
        self.et_project_location.setText(cf.project_location)
        sr = QStringList()
        sr.append('信息')
        root1 = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('Qt库')
        root2 = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('模块')
        root3 = QTreeWidgetItem(sr)
        sr = QStringList()
        sr.append('接口')
        root4 = QTreeWidgetItem(sr)

        self.tw_config.addTopLevelItem(root1)
        self.tw_config.addTopLevelItem(root2)
        self.tw_config.addTopLevelItem(root3)
        self.tw_config.addTopLevelItem(root4)

        sr1c00 = QStringList()
        sr1c00.append("项目名称")
        sr1c00.append(cf.project_name)
        r1c00 = QTreeWidgetItem(sr1c00)
        root1.addChild(r1c00)

        sr1c0 = QStringList()
        sr1c0.append("项目位置")
        sr1c0.append(cf.project_location)
        r1c0 = QTreeWidgetItem(sr1c0)
        root1.addChild(r1c0)

        sr1c1 = QStringList()
        sr1c1.append("组件类型")
        sr1c1.append(cf.component_type)
        r1c1 = QTreeWidgetItem(sr1c1)
        root1.addChild(r1c1)

        sr1c2 = QStringList()
        sr1c2.append("源模板")
        sr1c2.append(cf.template_source)
        r1c2 = QTreeWidgetItem(sr1c2)
        root1.addChild(r1c2)

        sr1c3 = QStringList()
        sr1c3.append("平台类型")
        sr1c3.append(cf.platform_type)
        r1c3 = QTreeWidgetItem(sr1c3)
        root1.addChild(r1c3)

        sr1c4 = QStringList()
        sr1c4.append("平台级别")
        sr1c4.append(cf.platform_level)
        r1c4 = QTreeWidgetItem(sr1c4)
        root1.addChild(r1c4)

        for qt in cf.qt_libs:
            sr2 = QStringList()
            sr2.append(qt['name'])
            sr2.append(qt['qt'])
            r2 = QTreeWidgetItem(sr2)
            root2.addChild(r2)

        for module in cf.modules:
            sr3 = QStringList()
            sr3.append(module['name'])
            sr3.append(module['description'])
            r3 = QTreeWidgetItem(sr3)
            root3.addChild(r3)

        for key in cf.interfaces.keys():
            sr4 = QStringList()
            sr4.append(key)
            if cf.interfaces[key]:
                sr4.append('实现')
            else:
                sr4.append('未实现')
            r4 = QTreeWidgetItem(sr4)
            root4.addChild(r4)
        self.tw_config.expandAll()

    def on_modify(self):
        '''修改配置'''
        if self.currentConfig:
            app.g_configurations = copy.copy(self.currentConfig)
            dlg = wizard.MyWizard()
            if dlg.exec_():
                index = self.lw.currentRow()
                if index < app.g_projects:
                    self.currentConfig = app.g_configurations
                    app.g_projects[index] = self.currentConfig
                    self.showConfigInfo(self.currentConfig)

    def on_gen(self):
        '''生成工程'''
        if not self.currentConfig:
            return

        #获取工程名及有效路径
        project_name = self.et_project_name.text()
        project_location = self.et_project_location.text()
        qdir = QDir(project_location)
        if not qdir.exists():
            if not qdir.mkpath(project_location):
                QMessageBox.warning(self, '警告', '路径无效！')
                return
        project_location = qdir.absolutePath()
        if not project_location.endsWith('/') and not project_location.endsWith('\\'):
            project_location += os.sep
        if project_name.isEmpty() or project_location.isEmpty():
            QMessageBox.warning(self, '警告', '项目名称或路径不能为空！')
            return

        self.currentConfig.project_name = app.QString2str(project_name)
        self.currentConfig.project_location = app.QString2str(project_location)
        template_name = self.currentConfig.template_source
        template_dir = app.g_pwd + os.sep + 'templates' + os.sep + template_name
        with open(template_dir + os.sep + 'config.json', 'r') as f:
            self.currentConfig.config_content = f.read()
        ret_json = app.render(self.currentConfig.config_content, config=self.currentConfig)
        self.currentConfig.config = json.loads(ret_json)
        for file in self.currentConfig.config['files']:
            sourcepath = template_dir + os.sep + file['source']
            targetdir = self.currentConfig.project_location + self.currentConfig.project_name
            targetpath = targetdir + os.sep + file['target']
            fi = QFileInfo(targetpath)
            qdir = fi.absoluteDir()
            if not qdir.exists():
                qdir.mkpath(fi.absolutePath())
            with open(sourcepath, 'r') as f:
                content = f.read()
                content = app.render(content, config=self.currentConfig) #渲染文件
            with open(targetpath, 'w+') as f:
                f.write(content.encode('utf-8'))
        QMessageBox.information(self,'提示','生成成功！')