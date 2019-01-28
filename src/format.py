import pygsheets
from __main__ import names_listcell, wks, Name_list, length

def formatSheet():
    #Sorts all names by last name, then updates the sheet
    c = 0
    for cell in names_listcell[2:length + 2]:
        label = cell.label
        linked_cell =wks.cell(label)
        name_toReplace = Name_list[c]
        linked_cell.value = name_toReplace
        c += 1
#end of format()
