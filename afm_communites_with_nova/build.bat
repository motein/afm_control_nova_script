@echo off
pyinstaller -F -w -i robot.ico -n robot gui_unit/application.py
xcopy .\gui_unit\config.ini .\dist\ /s /e /y