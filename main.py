#import pygsheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Point Update Tester").sheet1

names_list = []

names_list = sheet.col_values(1)
print(names_list)
