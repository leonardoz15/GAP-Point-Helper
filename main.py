#import pygsheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Point Update Tester").sheet1

#####################################################################################

class GAPmember:
    """The GAPmember class initilaizes a member object with name, email, gross, and net balances"""
    def __init__(self, full_name, email, gross, net):
        self.full_name = name
        self.email = email
        self.gross = gross_bal
        self.net = net_bal

    def newMember():
        """The newMember() method is used to alphabetically input a new member object into the spreadsheet"""
    #End of newMember()

    def removeMember():
        """The removeMembe() method is used to remove a member from the spreadsheet and delete the row""


    def addPoints():

    def removePoints():

    def lookup():
