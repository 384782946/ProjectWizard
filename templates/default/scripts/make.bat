call clean.bat
call VS02008-vsvars32.bat
cd ..
qmake -o MakeFile {{ config.project_name }}.pro
nmake
