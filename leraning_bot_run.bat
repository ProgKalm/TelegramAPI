@echo off

call %~dp0venv\Scripts\activate.bat

cd %~dp0Learning\

set TOKEN=5682682178:AAELtBNb6YfuiX5PE763En0HvXJVgKOTQWQ

python main.py

pause