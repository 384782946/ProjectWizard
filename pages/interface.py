# coding:utf-8

'''
作者：张潇健
日期：2016-6-14
概述：接口选择
'''

import app
import os
import json
from PyQt4.QtGui import QWizardPage,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton,QCheckBox,QListWidget,QListWidgetItem
from PyQt4.QtCore import SIGNAL,Qt

class InterfacePage(QWizardPage):

    def __init__(self):
        super(InterfacePage,self).__init__()
        self.completed = False
        self.setTitle('接口设置')
        self.setSubTitle('设置需要实现的接口')
        rootLayout = QVBoxLayout()
        rootLayout.setContentsMargins(20, 30, 20, 30)

        self.lw_interface = QListWidget()
        rootLayout.addWidget(self.lw_interface)
        self.setLayout(rootLayout)

    def initializePage(self):
        super(InterfacePage, self).initializePage()
        exsits = []
        for key in app.g_configurations.interfaces:
            if app.g_configurations.interfaces[key]:
                exsits.append(key)

        for interface in app.g_configurations.config['interfaces']:
            litem = QListWidgetItem(interface['name'])
            litem.setToolTip(interface['description'])
            litem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            if app.g_configurations.initialized:
                if interface['name'] in exsits:
                    litem.setCheckState(Qt.Checked)
                else:
                    litem.setCheckState(Qt.Unchecked)
            else:
                isdefault = False
                if app.g_configurations.component_type == "window":
                    if interface['default'] & 2:
                        isdefault = True
                else:
                    if interface['default'] & 1:
                        isdefault = True
                if isdefault:
                    litem.setCheckState(Qt.Checked)
                else:
                    litem.setCheckState(Qt.Unchecked)
            self.lw_interface.addItem(litem)

    def validatePage(self):
        interfaces = {}
        for i in range(self.lw_interface.count()):
            litem = self.lw_interface.item(i)
            key = app.QString2str(litem.text())
            if litem.checkState() == 2:
                interfaces[key] = True;
            else:
                interfaces[key] = False;

        app.g_configurations.interfaces = interfaces
        return True