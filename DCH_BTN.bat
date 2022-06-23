@echo off

call %~dp0Bot_Parcer\venv\Scripts\activate

cd %~dp0Bot_Parcer

set BOT_TOKEN=5500567502:AAHaRtLPqyFj8g7g5HO-ByvvSE0n7KaTzGg

python main.py

pause