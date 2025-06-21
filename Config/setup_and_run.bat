@echo off
echo Creating Virtual Environment...
python -m venv venv

echo Activating Virtual Environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing required packages...
pip install -r requirements.txt

echo Running Python Script...
python test_imports.py

echo Running Data Analytic Script...
python Manual_regres.py

pause
