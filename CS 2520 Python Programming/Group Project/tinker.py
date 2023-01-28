import tkinter as tk
from tkinter import *
columns = 0
rows = 0

firstWindow = Tk()

def click():
     print("hi")

def firstPanel(username, password):
     usernameEntryBox = Entry(firstWindow, width = 30, bg="gray", borderwidth=5)
     passwordEntryBox = Entry(firstWindow, width = 30, bg="gray", borderwidth=5)
     usernameLabel = Label(firstWindow, text = "Please input the username: ")
     passwordLabel = Label(firstWindow, text = "Please input the password: ")
     doneEntering = Button(firstWindow, text = "Enter", command = secondPanel)

     usernameLabel.grid(row = 0, column = 0)
     usernameEntryBox.grid(row = 0, column = 1)
     
     passwordLabel.grid(row = 1, column = 0)
     passwordEntryBox.grid(row = 1, column = 1)
     
     doneEntering.grid(row = 2, column = 1)
     username = usernameEntryBox.get()
     password = passwordEntryBox.get()
     
     return username, password
     
     
     
def secondPanel():
     firstWindow.destroy()
     secondWindow = Tk()
     
     # optionsLabel = Label(secondWindow, text = "Options")
     # option1 = Button(secondWindow, text = "Display a Schedule of trips", command = displaySchedule)
     # option2 = Button(secondWindow, text = "Delete a Trip Offering", command = deleteTripOffering)
     # option3 = Button(secondWindow, text = "Add a Trip Offering", command = addTripOffering)
     # option4 = Button(secondWindow, text = "Change the Driver of a Trip Offering", command = changeDriver)
     # option5 = Button(secondWindow, text = "Change the Bus of a Trip Offering", command = changeBus)
     # option6 = Button(secondWindow, text = "Display a Trip's Stops", command = displayTripStops)
     # option7 = Button(secondWindow, text = "Insert Actual Trip Info", command = insertTripData)
     # option8 = Button(secondWindow, text = "Add a Driver", command = addDriver)
     # option9 = Button(secondWindow, text = "Add a Bus", command = addBus)
     # option10 = Button(secondWindow, text = "Delete a Bus", command = deleteBus)
     # option11 = Button(secondWindow, text = "Exit the program", command = secondWindow.destroy)
     optionsLabel = Label(secondWindow, text = "Options")
     option1 = Button(secondWindow, text = "Display a Schedule of trips", command = secondPanel)
     option2 = Button(secondWindow, text = "Delete a Trip Offering", command = secondPanel)
     option3 = Button(secondWindow, text = "Add a Trip Offering", command = secondPanel)
     option4 = Button(secondWindow, text = "Change the Driver of a Trip Offering", command = secondPanel)
     option5 = Button(secondWindow, text = "Change the Bus of a Trip Offering", command = secondPanel)
     option6 = Button(secondWindow, text = "Display a Trip's Stops", command = secondPanel)
     option7 = Button(secondWindow, text = "Insert Actual Trip Info", command = secondPanel)
     option8 = Button(secondWindow, text = "Add a Driver", command = secondPanel)
     option9 = Button(secondWindow, text = "Add a Bus", command = secondPanel)
     option10 = Button(secondWindow, text = "Delete a Bus", command = secondPanel)
     option11 = Button(secondWindow, text = "Exit the program", command = secondWindow.destroy)



     optionsLabel.grid(row = 0, column = 0)
     option1.grid(row = 1, column = 0)
     option2.grid(row = 2, column = 0)
     option3.grid(row = 3, column = 0)
     option4.grid(row = 4, column = 0)
     option5.grid(row = 5, column = 0)
     option6.grid(row = 6, column = 0)
     option7.grid(row = 7, column = 0)
     option8.grid(row = 8, column = 0)
     option9.grid(row = 9, column = 0)
     option10.grid(row = 10, column = 0)
     option11.grid(row = 11, column = 0)


def main():
     username = ""
     password = ""
     firstPanel(username, password)
     firstWindow.mainloop()
     
main()

