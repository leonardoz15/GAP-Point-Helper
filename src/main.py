#####GAP POINT HELPER#####
#Author: Zachary Leonardo
##############################################################################
import pygsheets
# Use creds to create a client to interact with Google Drive API
# please add your own client_secret.json
client = pygsheets.authorize(service_file='secret/client_secret.json')
print("Welcome to the GAP Point Helper!")
file_name = input("What is the name of the google sheets file? ")
try:
    sheet = client.open(file_name)
except pygsheets.exceptions.SpreadsheetNotFound:
    #Code to extract client email to share with
    import json
    jdata = json.loads(open('client_secret.json').read())
    cl = jdata["client_email"]
    print("Please share with the email : " + cl)

#Global variables:
wks = sheet.sheet1
name_list = [] #lower case list
Name_list = [] #capitalized list
last_list = [] #list of last names for alphabetizing
length = 0
names_listcell = wks.get_col(1, returnas = 'cell')
for cell in names_listcell[2:]:
    if cell.value:
        length += 1 #real length of first column set to length
    else:
        pass
for cell in names_listcell[2:length + 2]:
    name_list.append(cell.value.lower())
for name in name_list:
    name_pieces = name.split(" ")
    first_name = name_pieces[0] #first name
    first_name = first_name.capitalize()
    last_name = name_pieces[1] #last name
    last_name = last_name.capitalize()
    last_list.append(last_name)
    Name_list.append(first_name + " " + last_name)

def main():
    #Main method
    import addMember
    import format
    #Choose which operation to perform: (Only add member at the moment)
    #TODO: add methods for adding and removing points
    while True:
        first = input("Do you need to format? This may take a few minutes for longer lists. (yes / no) ").lower() #to cut down on exec time
        if first == "yes":
            print("Formatting " + file_name)
            format.formatSheet()
            addMember.addMember(last_list) #Hard-coded as the only method currently
        elif first == "no":
            addMember.addMember(last_list) #Hard-coded as the only method currently
        another = input("Would you like to add another? (yes / no) ").lower()
        if another == "no":
            break

    print("Thanks for using the GAP Point Helper")

if __name__ == '__main__':
    main()
