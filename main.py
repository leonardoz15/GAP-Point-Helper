#Author: Zachary Leonardo
#Date: 11/6/2018

class GAPmember:
    """The GAPmember class initilaizes a member object with name, email, gross, and net balances"""
    def __init__(self, full_name, email, gross, net):
        self.name = full_name
        self.email = email
        self.gross_bal = gross
        self.net_bal = net
    #end of __init__() method

#end of GAPmember class

def updateList(full_list):
    """The updateList() method alphabetizes and updates the spreadsheet"""
    for self.name in full_list:
        name_pieces = self.name.split(" ")
        self.first_name = name_pieces[0] # first name
        self.first_name.capitilize()
        self.last_name = name_pieces[1]  # second name
        self.last_name.capitilize()
        self.name = self.first_name + " " + self.last_name
        print(self.last_name)

    full_list.sort(key = lambda x: x.self.last_name)
    return full_list
#end of updateList() function

def createList():
    """The createList function builds a list of member objects from the google sheet"""
    cell_list = sheet.get_row(1, returnas='cells')
    rows = len(cell_list) - 2  #To account for top two rows
    member_list = []
    q = 3
    for i in range(rows):
        full_name = sheet[q][1]
        email = sheet[q][2]
        gross_bal = sheet[q][3]
        net_bal = sheet[q][4]
        member = GAPmember(full_name, email, gross_bal, net_bal)
        member_list.append(member)
        q + 1
    return member_list
#End of createList() function


#####################################################################################

import pygsheets
# from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with Google Drive API
client = pygsheets.authorize(service_file='client_secret.json')

sheet = client.open("Point Update Tester").sheet1

print("Hello, starting out")

member_list = createList()
member_list = updateList(member_list)
    # def newMember():
    #     """The newMember() method is used to alphabetically input a new member object into the spreadsheet"""
    # #End of newMember()
    #
    # def removeMember():
    #     """The removeMembe() method is used to remove a member from the spreadsheet and delete the row""
    #
    #
    # def addPoints():
    #
    # def removePoints():
    #
    # def lookup():
