#ifndef {{ config.project_name.upper() }}DEF_H
#define {{ config.project_name.upper() }}DEF_H

#include <QtCore/qglobal.h>

#if defined {{ config.project_name.upper() }}_LIB
#  define {{ config.project_name.upper() }}_EXPORT Q_DECL_EXPORT
#else
#  define {{ config.project_name.upper() }}_EXPORT Q_DECL_IMPORT
#endif

#endif
