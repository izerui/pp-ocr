rmdir /s /q build dist
:: https://pyinstaller.org/en/stable/usage.html
.\venv\Scripts\pyinstaller -n ocr --uac-admin --additional-hooks-dir=./hooks --windowed main.py