# Project ORACLE Developer Commands

## Start ORACLE

```powershell
cd "C:\Users\Vanig\OneDrive\Documents\Project_ORACLE"
.\.venv\Scripts\Activate.ps1
python -m streamlit run app.py
```

## Stop ORACLE

Press:

```text
Ctrl + C
```

## Run Tests

```powershell
python -m pytest
```

## Save Changes to GitHub

```powershell
git status
git add .
git commit -m "Describe your change"
git push
```

## Install a Package

```powershell
python -m pip install package-name
pip freeze > requirements.txt
```