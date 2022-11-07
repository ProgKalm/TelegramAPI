@echo off

call %~dp0venv\Scripts\activate.bat

cd %~dp0Learning\

set TOKEN=5683182363:AAGfN2-YHTiS0kQ20mboYCe0vH7dhnkMUKU

python bot.py

pause