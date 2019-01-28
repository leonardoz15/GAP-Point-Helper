import pygsheets
from __main__ import wks

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
