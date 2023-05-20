from tkinter import *
from tkinter import messagebox
from Mosque import *
from dataBase import *

top = Tk()
top.title('Mosques Managment System')
top.geometry('770x450')

#LABELS **every variables name ends with L**
labelSize = 15
idL = Label(top,text='ID',font=('Helvatical bold',labelSize)) #1
idL.grid(row=0, column=0)

typeL = Label(top,text='Type',font=('Helvatical bold',labelSize)) #2
typeL.grid(row=1, column=0)

cordinatesL = Label(top,text='Cordinates',font=('Helvatical bold',labelSize)) #3
cordinatesL.grid(row=2, column=0)

nameL = Label(top,text='  Name',font=('Helvatical bold',labelSize)) #4
nameL.grid(row=0, column=2)

addressL = Label(top,text='  Address',font=('Helvatical bold',labelSize)) #5
addressL.grid(row=1, column=2)

imamNameL = Label(top,text='  Imam Name',font=('Helvatical bold',labelSize)) #6
imamNameL.grid(row=2, column=2)

#TEXTFIELDS **every variables name ends with T**
textBoxWidth = 20
textBoxHight = 1
idT = Text(top, width=textBoxWidth,height=textBoxHight,font=('Helvatical bold',labelSize)) #1
idT.grid(row=0,column=1)

mosq_types = ["congregational", "collective"]
value_inside = StringVar(top)
value_inside.set("congregational")
typesOP = OptionMenu(top, value_inside, *mosq_types) #2 option menu
typesOP.grid(row=1,column=1)
typesOP.config(width=30)

cordinatesT = Text(top, width=textBoxWidth,height=textBoxHight,font=('Helvatical bold',labelSize)) #3
cordinatesT.grid(row=2,column=1)

nameT = Text(top, width=textBoxWidth,height=textBoxHight,font=('Helvatical bold',labelSize)) #4
nameT.grid(row=0,column=3)

addressT = Text(top, width=textBoxWidth,height=textBoxHight,font=('Helvatical bold',labelSize)) #5
addressT.grid(row=1,column=3)

imamNameT = Text(top, width=textBoxWidth,height=textBoxHight,font=('Helvatical bold',labelSize)) #6
imamNameT.grid(row=2,column=3)

#BUTTONS **every variables ends with B**
BFontSize = 15
BHight = 2
BWidth = 15
displayAllB = Button(top,text="Display All",height=BHight,width=BWidth,font=('Helvatical bold',BFontSize),command= lambda: displayAllB()) #1
displayAllB.grid(row=3,column=1)

addEntryB = Button(top,text="Add Entry",height=BHight,width=BWidth,font=('Helvatical bold',BFontSize),command= lambda: insertB()) #2
addEntryB.grid(row=4,column=1)

searchByNameB = Button(top,text="Search By Name",height=BHight,width=BWidth,font=('Helvatical bold',BFontSize),command= lambda: searchNameB()) #3
searchByNameB.grid(row=3,column=2)

deleteEntryB = Button(top,text="Delete Entry",height=BHight,width=BWidth,font=('Helvatical bold',BFontSize),command= lambda: deleteEntryB()) #4
deleteEntryB.grid(row=4,column=2)

updateEntryB = Button(top,text="Update Entry",height=BHight,width=BWidth,font=('Helvatical bold',BFontSize),command= lambda: updateImamNameB()) #5
updateEntryB.grid(row=4,column=3)

clearBoard = Button(top,text="Clear The Board",height=BHight,width=BWidth,font=('Helvatical bold',BFontSize),command= lambda: listBox1.delete(0,END)) #6
clearBoard.grid(row=3,column=3)

#LIST BOX
listBox1 = Listbox(top,font=('Helvatical bold',12),height=10,width=81)
listBox1.place(x=18,y=230)
# Creating  Y  Scrollbar for list box **EXTRA**
scrollbarY = Scrollbar(top)
scrollbarY.place(x=750,y=230,width=20,height=190)
listBox1.config(yscrollcommand = scrollbarY.set)
scrollbarY.config(command = listBox1.yview)
# Creating  X  Scrollbar for list box **EXTRA**
scrollbarX = Scrollbar(top,orient=HORIZONTAL)
scrollbarX.place(x=18,y=425,width=730,height=20)
listBox1.config(xscrollcommand = scrollbarX.set)
scrollbarX.config(command = listBox1.xview)

#functions
def properDisplay(i):
    dic = {k:v for (k,v) in zip(['ID','name','type','address','coordinates','imamName'],i)}
    s=""
    for x in dic:
        s+=f"{x}:{dic[x]}   "
    return s

#functions for the buttons
def displayAllB():
    for i in mosqobj.displayAll():
        listBox1.insert(0,properDisplay(i))
    if len(mosqobj.displayAll()) == 0:
        listBox1.insert(0,"There is nothing to display :)")

def searchNameB(): #search by name
    name = mosqobj.searchName(nameT.get(1.0,"end-1c"))
    if name:
        for i in name:
             listBox1.insert(0,properDisplay(i))
    else:
        messagebox.showerror("Wrong input", "Name is NOT correct!")
        return 0

def updateImamNameB(): # UPDATE imam name. **EXTRA**
    name = nameT.get(1.0,"end-1c")
    newName = imamNameT.get(1.0,"end-1c")
    if not name.strip() or not mosqobj.searchName(name):
        messagebox.showerror("Wrong input", "Name is NOT correct!")
        return 0
    if not newName.strip():
        messagebox.showerror("Wrong input", "Please enter a valid Imam Name!")
    else:
        mosqobj.updateEntry(name,newName)
        listBox1.insert(0,f"Imam name of {name} mosque has been changed to {newName} ")

def deleteEntryB(): #delete a record
    if not idT.get(1.0,"end-1c").strip():
        messagebox.showerror("Empty input", "Please enter an ID!")
    else:
        try:
            if mosqobj.delEntry(idT.get(1.0,"end-1c")) == 0:
                messagebox.showinfo("NOT FOUND", "We don't have this in our records!")
            else:
                listBox1.insert(0,f"The mosque ID:{idT.get(1.0,'end-1c')} has been deleted.")
        except sqlite3.OperationalError:
            messagebox.showerror("Wrong input", "Please make sure ID is a number and correct!")

def insertB(): #enter new data
    if not nameT.get(1.0,"end-1c").strip() or not addressT.get(1.0,"end-1c").strip() or not imamNameT.get(1.0,"end-1c").strip() or not cordinatesT.get(1.0,"end-1c").strip():
        messagebox.showerror("Wrong input", "Please fill all blanks!")
    elif not idT.get(1.0,"end-1c").isnumeric():
        messagebox.showerror("Wrong ID", "Only numbers allowed in ID's!")
    elif mosqobj.searchName(nameT.get(1.0,"end-1c")) != 0:
        messagebox.showerror("Wrong name", "We already have this name.\nHint: Name has to be unique!")
    else:
        try:
            mosqobj.insertData(idT.get(1.0,"end-1c"),nameT.get(1.0,"end-1c"),value_inside.get(),addressT.get(1.0,"end-1c"),cordinatesT.get(1.0,"end-1c"),imamNameT.get(1.0,"end-1c"))
            listBox1.insert(0,f"The mosue of ID:{idT.get(1.0,'end-1c')} has been added succesfully")
        except sqlite3.IntegrityError:
            listBox1.insert(0,f"We have already a mosque with that ID\n Check all input if this is't the case")
mosqobj = dataBase()
mainloop()