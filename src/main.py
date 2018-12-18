def format():
    #Capitilizes and sorts all names by last name, then updates the sheet
    c = 0
    for cell in names_listcell[2:length + 2]:
        label = cell.label
        linked_cell = wks.cell(label)
        name_toReplace = Name_list[c]
        linked_cell.value = name_toReplace
        c += 1
#end of format()

def addMember(last_list):
    #Alphabetically add a new member
    print("To add a new member, please specify the following: ")
    fname_new = input("First Name:    ").lower()
    lname_new = input("Last Name:     ").lower()
    email_new = input("Email (@allegheny.edu):    ") + '@allegheny.edu'
    bal_new = int(input("Starting point balance:    "))

    #find where new name should be indexed
    lname_new = lname_new.capitalize()
    last_list.append(lname_new)
    last_list.sort()
    index_add = last_list.index(lname_new)
    index_add += 2 # to account for styling

    #update spreadsheet with new member
    newmember_list = []
    fname_new = fname_new.capitalize()
    name_new = fname_new + " " + lname_new
    newmember_list.extend((name_new, email_new, bal_new, bal_new))
    wks.insert_rows(row=index_add, number=1, values=newmember_list)

#end of addMember()

##############################################################################
import pygsheets
# Use creds to create a client to interact with Google Drive API
client = pygsheets.authorize(service_file='client_secret.json')
print("Welcome to the GAP Point Helper!")
while True:
    try:
        name = input("What is the name of the google sheets file? ")
        sheet = client.open(name)
        break
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
    #Choose which operation to perform: (Only add member at the moment)
    #TODO: add methods for adding and removing points
    while True:
        first = input("Do you need to format? This may take a few minutes for longer lists. (yes / no) ").lower() #to cut down on exec time
        if first == "yes":
            format()
            addMember(last_list) #Hard-coded as the only method currently
        elif first == "no":
            addMember(last_list) #Hard-coded as the only method currently
        another = input("Would you like to add another? (yes / no) ").lower()
        if another == "no":
            break

    print("Thanks for using the GAP Point Helper")

if __name__ == '__main__':
    main()
