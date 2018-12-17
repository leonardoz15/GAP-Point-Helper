
#def createList():





import pygsheets
# from oauth2client.service_account import ServiceAccountCredentials
client = pygsheets.authorize(service_file='client_secret.json')

sheet = client.open("Point Update Tester")
wks = sheet.sheet1


def main():
    # Use creds to create a client to interact with Google Drive API

    print("Hello, starting out")
    c1 = wks.cell('A6')
    c2 = wks.cell('B6')
    c3 = wks.cell('C6')
    c4 = wks.cell('D6')
    values_list = []
    values_list.append(c1.value)
    values_list.append(c2.value)
    values_list.append(c3.value)
    values_list.append(c4.value)
    wks.insert_rows(row=3, number=1, values=values_list)
    #member_list = createList()
    #print(member_list[1], len(member_list))
    #member_list = updateList(member_list)

if __name__ == '__main__':
    main()
