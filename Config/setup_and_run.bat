@echo off
echo Creating Virtual Enviroment...
python -m venv venv

echo Activating Virtual Enviroment...
call venv\Scripts\activate

echo Installing Dependencies...
pip install pyodbc python-dotenv

echo Running Python Script...
python test_imports.py

echo Running Database Test...
python databasecheck.py

pause