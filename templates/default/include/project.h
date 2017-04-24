#ifndef {{ config.project_name.upper() }}_H
#define {{ config.project_name.upper() }}_H

#include "{{ config.project_name }}Def.h"
{% if config.component_type == "window" %}
#include <QWidget>
#include "ui_{{ config.project_name }}.h"
#include "ComponentBase/ComponentWin.h"
using namespace Allone;

extern "C" {{ config.project_name.upper() }}_EXPORT CComponent* CreateComp(const std::string& CompName);

class {{ config.project_name.upper() }}_EXPORT {{ config.project_name }}:public ComponentWin,public QWidget
{
{% else %}
#include "ComponentBase/Component.h"
using namespace Allone;

extern "C" {{ config.project_name.upper() }}_EXPORT CComponent* CreateComp(const std::string& CompName);

class {{ config.project_name.upper() }}_EXPORT {{ config.project_name }}:public CComponent
{
{% endif %}
    //Q_OBJECT
public:

    /*
	 *\fn		CShowVResultWin(const std::string& sCompID)
	 *\brief	Constructor.
	 *\author	Yinjh
	 *\date		2016-2-18
	 *\param	sCompID	Identifier of the comp.
	 */
    {{ config.project_name }}(const std::string& sCompID);

    /*
	 *\fn		~CShowVResultWin()
	 *\brief	Finaliser.
	 *\author	Yinjh
	 *\date		2016-2-18
	 */
    ~{{ config.project_name }}();
{% if config.interfaces["changeShowMode"] %}
    /*
	 *\fn		void changeShowMode(const std::string& name)
	 *\brief	Change show mode.
	 *\author	Yinjh
	 *\date		2016-2-18
	 *\param	name	The name.
	 */
	void changeShowMode(const std::string& name);
{% endif %} {% if config.interfaces["initialize"] %}
/*
	 *\fn		virtual void initialize(const CompConfigInfo& compCfgInfo)
	 *\brief	Initializes this object.
	 *\author	Yinjh
	 *\date		2016-2-29
	 *\param	compCfgInfo	Information describing the comp configuration.
	 */
	virtual void initialize(const CompConfigInfo& compCfgInfo);
{% endif %} {% if config.interfaces["onListenerCompStatusUpdate"] %}
	/*
	 *\fn		virtual void onListenerCompStatusUpdate(const std::string sWho, COMPSTATUS_TYPE eEvent) = 0
	 *\brief	Executes the listener comp status update action. 被监听的功能组件状态改变.
	 *\author	Yinjh
	 *\date		2016-2-29
	 *\param	sWho	The who.
	 *\param	eEvent	The event. 被监听的功能组件状态.
	 */
	virtual void onListenerCompStatusUpdate(const std::string sWho, COMPSTATUS_TYPE eEvent);
{% endif %} {% if config.interfaces["showComp"] %}
	/*
	*\fn		virtual bool showComp()
	*\brief		Shows the comp. 显示功能组件
	*\author	Yinjh
	*\date		2016-3-1
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool showComp();
{% endif %} {% if config.interfaces["hideComp"] %}
	/*
	*\fn		virtual bool hideComp()
	*\brief		Hides the comp. 隐藏功能组件
	*\author	Yinjh
	*\date		2016-3-1
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool hideComp();
{% endif %} {% if config.interfaces["suspendComp"] %}
	/*
	*\fn		virtual bool suspendComp()
	*\brief		Suspend comp. 挂起功能组件
	*\author	Yinjh
	*\date		2016-3-1
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool suspendComp();
{% endif %} {% if config.interfaces["resumeComp"] %}
	/*
	*\fn		virtual bool resumeComp()
	*\brief		Resume comp. 恢复功能组件
	*\author	Yinjh
	*\date		2016-3-1
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool resumeComp();
{% endif %} {% if config.interfaces["terminateComp"] %}
	/*
	*\fn		virtual bool terminateComp()、
	*\brief		Terminate comp. 卸载功能组件
	*\author	Yinjh
	*\date		2016-3-1
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool terminateComp();
{% endif %} {% if config.interfaces["run"] %}
	/*
	*\fn		virtual bool run()
	*\brief		Runs this object.
	*\author	Yinjh
	*\date		2016-3-1
	*\return	true if it succeeds, false if it fails.
	*/
	virtual bool run();
{% endif %} {% if config.interfaces["saveCompMemento"] %}
	/*
	*\fn		virtual void saveCompMemento()
	*\brief		Saves the comp memento. 保存组件备忘录数据
	*\author	Yinjh
	*\date		2016-3-1
	*/
	virtual void saveCompMemento();
{% endif %} {% if config.interfaces["resumeCompMemento"] %}
	/*
	*\fn		virtual void resumeCompMemento()
	*\brief		Resume comp memento. 从备忘录中恢复数据
	*\author	Yinjh
	*\date		2016-3-1
	*/
	virtual void resumeCompMemento();
{% endif %} {% if config.interfaces["workModelChange"] %}
/*
	 *\fn		virtual void workModelChange(EWorkSituation iWorkMode) = 0
	 *\brief	Work model change.
	 *\author	Yinjh
	 *\date		2016-4-13
	 *\param	iWorkMode	The work mode.
	 */
	virtual void workModelChange(EWorkSituation iWorkMode);
{% endif %}
protected:
{% if config.interfaces["initData"] %}
	/*
	 *\fn		void initData(const CInitParam& params)
	 *\brief	Initialises the data.
	 *\author	Yinjh
	 *\date		2016-3-2
	 *\param	params	Options for controlling the operaation.
	 */
	void initData(const CInitParam& params);
{% endif %}
};

#endif
