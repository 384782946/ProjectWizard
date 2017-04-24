#coding:utf-8

import json

PT_WIN32 = 1
PT_LINUX = 2

class Configuration:
    '''用来存储每个页面生成的配置信息'''

    initialized = False
    project_name = ""       #工程名称
    project_location = ""   #工程所在位置
    component_type = ""     #组件类型
    template_source = ""    #源模板名称
    platform_type = 0      #平台类型（win32|linux）
    platform_version = ""     #平台版本(x86_32|x86_64)
    modules = []            # 所有引用的模块
    qt_libs = []  # 依赖qt模块
    libs = []               #依赖库
    interfaces = {}         #实现的接口

    def toJson(self):
        output = {}
        output['project_name'] = self.project_name
        output['project_location'] = self.project_location
        output['template_source'] = self.template_source
        output['component_type'] = self.component_type
        output['platform_type'] = self.platform_type
        output['platform_version'] = self.platform_version
        output['qt_libs'] = self.qt_libs
        output['modules'] = self.modules
        output['libs'] = self.libs
        output['interfaces'] = self.interfaces
        return json.dumps(output)

    def fromJson(self,content):
        inputs = json.loads(content)
        self.project_name = inputs['project_name']
        self.project_location = inputs['project_location']
        self.template_source = inputs['template_source']
        self.component_type = inputs['component_type']
        self.platform_type = inputs['platform_type']
        self.platform_version = inputs['platform_version']
        self.qt_libs = inputs['qt_libs']
        self.modules = inputs['modules']
        self.libs = inputs['libs']
        self.interfaces = inputs['interfaces']
        self.initialized = True