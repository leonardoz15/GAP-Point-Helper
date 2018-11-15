# GAP Point Helper
I created this short Python program to assist me in managing the point reward system for Gator Activities Programming. This program helps automate data entry into a publically viewable google spreadsheet.

Installation:
-------------
Requirements: Python 2.7+ or 3+
This program also requires [pygsheets](https://github.com/nithinmurali/pygsheets) to operate

```
pip install pygsheets
```
or
```
pip install https://github.com/nithinmurali/pygsheets/archive/master.zip
```

Basic Usage:
-----------
1. First you need to obtain [OAuth2 credentials from Google Developers Console](https://gspread.readthedocs.io/en/latest/oauth2.html)

2. Place the generated .json file in the repository directory renamed as client_secret.json

3. If done correctly, you can use any spreadsheet in your google drive by naming it in this line:
```python
sheet = client.open("Point Update Tester")
```
Examples:
---------
To come :)
