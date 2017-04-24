#include "{{ config.project_name }}.h"

CComponent* CreateComp( const std::string& CompName)
{
	CComponent* comp = 0;
	if (CompName == "{{ config.project_name }}")
	{
		comp = new {{ config.project_name }}(CompName);
	}

	return comp;
}
{% if config.component_type == "window" %}
{{ config.project_name }}::{{ config.project_name }}(const std::string& sCompID)
    :CComponentWin(sCompID)
{
    m_ui.setupUi(this);
}
{% elif config.component_type == "server" %}
{{ config.project_name }}::{{ config.project_name }}(const std::string& sCompID)
    :CComponent(sCompID)
{

}
{% endif %}
{{ config.project_name }}::~{{ config.project_name }}()
{
}
{% if config.interfaces["changeShowMode"] %}
void {{ config.project_name }}::changeShowMode(const std::string& name)
{
}
{% endif %} {% if config.interfaces["initialize"] %}
void {{ config.project_name }}::initialize(const CompConfigInfo& compCfgInfo)
{
}
{% endif %} {% if config.interfaces["onListenerCompStatusUpdate"] %}
void {{ config.project_name }}::onListenerCompStatusUpdate(const std::string sWho, COMPSTATUS_TYPE eEvent)
{
}
{% endif %} {% if config.interfaces["showComp"] %}
bool {{ config.project_name }}::showComp()
{
    return true;
}
{% endif %} {% if config.interfaces["hideComp"] %}
bool {{ config.project_name }}::hideComp()
{
    return true;
}
{% endif %} {% if config.interfaces["suspendComp"] %}
bool {{ config.project_name }}::suspendComp()
{
    return true;
}
{% endif %} {% if config.interfaces["resumeComp"] %}
bool {{ config.project_name }}::resumeComp()
{
    return true;
}
{% endif %} {% if config.interfaces["terminateComp"] %}
bool {{ config.project_name }}::terminateComp()
{
    return true;
}
{% endif %} {% if config.interfaces["run"] %}
bool {{ config.project_name }}::run()
{
    return true;
}
{% endif %} {% if config.interfaces["saveCompMemento"] %}
void {{ config.project_name }}::saveCompMemento()
{
}
{% endif %} {% if config.interfaces["resumeCompMemento"] %}
void {{ config.project_name }}::resumeCompMemento()
{
}
{% endif %} {% if config.interfaces["initData"] %}
void {{ config.project_name }}::initData(const CInitParam& params)
{
}
{% endif %} {% if config.interfaces["workModelChange"] %}
void {{ config.project_name }}::workModelChange(EWorkSituation iWorkMode)
{
}
{% endif %}