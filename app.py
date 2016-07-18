 # coding:utf-8

from jinja2 import Template
from configuration import Configuration

def render(source, **kwargs):
    template = Template(source.decode('utf-8'))
    return template.render(kwargs)

def QString2str(qstring):
    return str(qstring.toUtf8())

g_pwd = '' #当前程序目录
g_templates = [] #当前所有可用模板列表
g_projects = [] #所有工程

g_configurations = Configuration() #用来渲染的配置数据

g_qt_library = [
    {
        "name":"XML",
        "qt":"xml",
        "refer":False
    },
    {
        "name": "SVG",
        "qt":"svg",
        "refer":False
    },
    {
        "name": "Qml",
        "qt": "qml",
        "refer": False
    },
    {
        "name": "Quick",
        "qt": "quick",
        "refer": False
    },
    {
        "name": "Multimedia",
        "qt":"multimedia",
        "refer":False
    },
    {
        "name": "Qt3 support",
        "qt":"qt3support",
        "refer":False
    },
    {
        "name": "SQL",
        "qt":"sql",
        "refer":False
    },
    {
        "name": "ActiveQt container",
        "qt":"xml",
        "refer":False
    },
    {
        "name": "OpenGL",
        "qt":"opengl",
        "refer":False
    },
    {
        "name": "Network",
        "qt":"network",
        "refer":False
    },
    {
        "name": "Script",
        "qt":"script",
        "refer":False
    },
    {
        "name": "Script Tools",
        "qt": "scripttools",
        "refer": False
    },
    {
        "name": "WebKit",
        "qt":"webkit",
        "refer":False
    },
    {
        "name": "Xml patterns",
        "qt":"xmlpatterns",
        "refer":False
    },
    {
        "name": "Phonon",
        "qt":"phonon",
        "refer":False
    },
    {
        "name": "Test",
        "qt":"testlib",
        "refer":False
    },
    {
        "name": "Declarative",
        "qt":"declarative",
        "refer":False
    }
]
