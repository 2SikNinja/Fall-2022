from mysql.connector import connection
from mysql.connector.errors import Error


def displayAllCommands():

    print("\nPlease choose a transaction:")
    print("1  - Display a Schedule of trips")
    print("2  - Delete a Trip Offering")
    print("3  - Add a Trip Offering")
    print("4  - Change the Driver of a Trip Offering")
    print("5  - Change the Bus of a Trip Offering")
    print("6  - Display a Trip's Stops")
    print("7  - Insert Actual Trip Info")
    print("8  - Add a Driver")
    print("9  - Add a Bus")
    print("10 - Delete a Bus")
    print("11 - Exit the program")
    print("Your choice (Select a number): ") 


def displaySchedule(cursor):
        
    print("\n---- Display a schedule of trips ----")
    print("Start Location Name: ") 
    startLoc = input().strip() 
    print("Destination Name: ") 
    destLoc = input().strip() 
    print("Enter the Date using the format 'yyyy-MM-dd': ") 
    date = input().strip() 

    # Get the data from the database
    try:           
        cursor.execute("SELECT T1.StartLocationName AS Start_Location, T1.DestinationName AS Destination, " +
                                        "T0.Date, T0.ScheduledStartTime AS Scheduled_Start_Time, T0.ScheduledArrivalTime AS Scheduled_Arrival_Time, " +
                                        "T0.DriverName, T0.BusID " +
                                        "FROM TripOffering T0, Trip T1 " + 
                                        "WHERE T1.StartLocationName LIKE '" + startLoc + "' AND " + 
                                        "T1.DestinationName LIKE '" + destLoc + "' AND " + 
                                        "T0.Date = '" + date + "' AND " + 
                                        "T1.TripNumber = T0.TripNumber " + 
                                        "Order by ScheduledStartTime ")
        row = cursor.fetchone()
        if row:
            print("RESULT:")
            print("-------------------------------------------------------------------------------------------------------------------------------")
            for column in cursor.description:
                print(column[0] + "\t\t", end="")
            print("\n-------------------------------------------------------------------------------------------------------------------------------")
            while row is not None:
                print(str(row[0]) + "\t\t\t\t\t" + str(row[1]) + "\t\t\t" + str(row[2]) + "\t\t\t\t" + str(row[3]) + "\t\t\t\t\t\t" +
                      str(row[4]) + "\t\t\t\t\t\t" + str(row[5]) + "\t\t\t" + str(row[6]))
                row = cursor.fetchone()
            print("-------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("No data found for this trip.")
    
    except Error: 
        print("=> No schedule from " + startLoc + " to " + destLoc + " on " + date)
     

# delete a trip offering
def deleteTripOffering(cursor, conn): 

    print("\n---- Delete a Trip Offering ----")
    print("Enter the Trip Number: ") 
    tripNo = input().strip() 
    print("Enter the Date: ") 
    date = input().strip() 
    print("Enter the scheduled Start Time: ") 
    scheduledStartTime = input().strip() 

    try: 
        # if no matching, output an error 
        cursor.execute("DELETE FROM TripOffering " + 
                                "WHERE TripNumber = '" + tripNo + "' AND " + 
                                "Date = '" + date + "' AND " + 
                                "ScheduledStartTime = '" + scheduledStartTime + "'")
        conn.commit()
        print("=> The inputted Trip Offering was successfully deleted.") 
        
    except Error: 
        #if some error occurs check input
        print("=> Error! The inputted Trip Offering does not exist.")
     
    
# add a sets of trip offerings
def addTripOffering(cursor, conn): 

    print("\n---- Add a Trip Offering ----")
    while True: 
        print("Enter the Trip Number: ") 
        tripNo = input().strip() 
        print("Enter the Date using the format 'yyyy-MM-dd': ") 
        date = input().strip() 
        print("Enter the Scheduled Start Time: ") 
        scheduledStartTime = input().strip() 
        print("Enter the Scheduled Arrival Time: ") 
        scheduledArrivalTime = input().strip() 
        print("Enter the Driver Name: ") 
        driver = input().strip() 
        print("Enter the Bus ID: ") 
        bus = input().strip() 

        # insert data to the database
        try: 
            cursor.execute("INSERT INTO TripOffering VALUES ('" + tripNo + "', '" + date + "', '" + scheduledStartTime
                 + "', '" + scheduledArrivalTime + "', '" + driver + "', '" + bus + "')")
            conn.commit()
            print("=> The new Trip Offering was successfully added.")
        except Error:
            print("=> Error! Please check the inputted data.")
        

        # Ask if the user wants to add another trip offering
        print("\nDo you want to add another Trip Offering? (y/n): ")
        choice = input()
        if choice.lower().strip()[0] == 'n':
            break    


# change the driver of a given trip offering
def changeDriver(cursor, conn):

    print("\n---- Change the Driver's Name of a Trip Offering ----")
    print("Enter the new Driver's Name: ")
    newDriver = input().strip()
    print("Enter the Trip's Number: ")
    tripNo = input().strip()
    print("Enter the Date using the format 'yyyy-MM-dd': ")
    date = input().strip()
    print("Enter the Scheduled Start Time: ")
    scheduledStartTime = input().strip()

    try:
        cursor.execute("UPDATE TripOffering " +
                                "SET DriverName = '" + newDriver + "' " +
                                "WHERE TripNumber = '" + tripNo + "' AND " +
                                "Date = '" + date + "' AND " +
                                "ScheduledStartTime = '" + scheduledStartTime + "'")
        conn.commit()
        print("=> The inputted Trip Offering was successfully updated with the new Driver.")
        
    except Error:
        print("=> Error! Please check the inputted data.")


# change the bus of a given trip offering
def changeBus(cursor, conn):

    print("\n---- Change the bus ID of a Trip Offering ----")
    print("New Bus Number: ")
    newBus = input().strip()
    print("Start Trip Number: ")
    tripNo = input().strip()
    print("Enter the Date using the format 'yyyy-MM-dd': ")
    date = input().strip()
    print("Scheduled Start Time: ")
    scheduledStartTime = input().strip()

    try:
        cursor.execute("UPDATE TripOffering " +
                                "SET BusID = '" + newBus + "' " +
                                "WHERE TripNumber = '" + tripNo + "' AND " +
                                "Date = '" + date + "' AND " +
                                "ScheduledStartTime = '" + scheduledStartTime + "'")
        conn.commit()
        print("The inputted Trip Offering was successfully updated with the new Bus ID.")
        
    except Error:
        print("=> Error! Please check the inputted data.")
    

# display the stops of a given trips
def displayTripStops(cursor):

    print("\n---- Display the stops of a given trip ----")
    print("Enter the Trip Number: ")
    tripNo = input().strip()
    #getting database  data
    try:
        cursor.execute("SELECT * FROM TripStopInfo "+
                                "WHERE TripNumber = '" + tripNo + "' " +
                                "Order By SequenceNumber ")
        row = cursor.fetchone()
        if row:
            print("RESULT:")
            print("----------------------------------------------------")
            for column in cursor.description:
                print(column[0] + "\t", end="")
            print("\n----------------------------------------------------")
            while row is not None:
                print("\t" + str(row[0]) + "\t\t\t" + str(row[1]) + "\t\t\t" + str(row[2]) + "\t\t\t\t" + str(row[3]))
                row = cursor.fetchone()
            print("----------------------------------------------------")
        else:
            print("The inputted Trip Number = " + tripNo + " does not exist")
    except Error:
        print("The inputted Trip Number = " + tripNo + " does not exist")
    

# add a driver
def addDriver(cursor, conn):

    print("\n---- Add a driver ----")
    print("Enter the Driver's Name: ")
    driver = input().strip()
    print("Enter the Driver's Phone number: ")
    phoneNo = input().strip()

    try:
        cursor.execute("INSERT INTO Driver VALUES ('" + driver + "', '" + phoneNo + "')")
        conn.commit()
        print("=> Driver's name = " + driver + " was successfully added!")
    except Error:
        print("=> Error! Please check the inputted data.")
    

# add a bus 
def addBus(cursor, conn):

    print("\n---- Add a bus ----")
    print("Enter the Bus ID: ")
    busId = input().strip()
    print("Enter the Bus's Model: ")
    model = input().strip()
    print("Enter the Bus's Year: ")
    year = input().strip()
    
    try:
        cursor.execute("INSERT INTO Bus VALUES ('" + busId + "', '" + model + "', '" + year + "')")
        conn.commit()
        print("=> Bus ID = " + busId + " was successfully added!")
    except Error:
        print("=> Error! Please check the inputted data.")
    

# delete a bus
def deleteBus(cursor, conn):
    
    print("\n---- Delete a bus ----")
    print("Enter the Bus ID to be deleted: ")
    busId = input().strip()

    try:
        cursor.execute("DELETE FROM Bus WHERE BusID = '" + busId + "'")
        conn.commit()
        print("=> Bus ID = " + busId + " was successfully deleted!")
    
    except Error:
        print("=> Error! Bus ID = " + busId + " does not exists.")
    

# insert the actual data of a given trip
def insertTripData(cursor, conn):

    print("\n---- Record the actual data of a given trip offering ----")
    print("Enter the Trip Number: ")
    tripNo = input().strip()
    print("Enter the Date using the format 'yyyy-MM-dd': ")
    date = input().strip()
    print("Enter the Scheduled Start Time: ")
    scheduledStartTime = input().strip()
    print("Enter the Stop Number: ")
    stop = input().strip()
    print("Enter the Scheduled Arrival Time: ")
    scheduledArrivalTime = input().strip()
    print("Enter the Actual Start Time: ")
    actualStartTime = input().strip()
    print("Enter the Actual Arrival Time: ")
    actualArrival = input().strip()
    print("Enter the Number of Passengers in: ")
    passengersIn = input().strip()
    print("Enter the Number of Passengers out: ")
    passengersOut = input().strip()

    try:
        cursor.execute("INSERT INTO ActualTripStopInfo VALUES ('" + tripNo + "', '" + date + "', '" + scheduledStartTime + "', '" + stop + "', '" + scheduledArrivalTime
                    + "', '" + actualStartTime + "', '" + actualArrival + "', '" + passengersIn + "', '" + passengersOut + "')")
        conn.commit()
        print("=> The actual data of the given trip offering was successfully recorded.")
    except Error:
        print("=> Error! Please check the inputted data.")


# add a driver
def addDriver(cursor, conn):
    driver = input('Enter the Driver\'s name: ').strip()
    phoneNo = input('Enter the Driver\'s phone number: ').strip()
    try:
        cursor.execute("INSERT INTO Driver VALUES ('" + driver + "', '" + phoneNo + "')")
        conn.commit()
        print("=> Driver's name = " + driver + " was successfully added!")
    except Error:
        print('=> Error! Please check the inputted data.')


# add the username and password to authenticate later
def authenticate(cursor, conn):
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (Username text, Password text)''')
    cursor.execute("INSERT INTO users VALUES ('admin1', 'password1')")
    cursor.execute("INSERT INTO users VALUES ('admin2', 'password2')")
    cursor.execute("INSERT INTO users VALUES ('admin3', 'password3')")
    cursor.execute("INSERT INTO users VALUES ('admin4', 'password4')")
    conn.commit()

def main():

    print("------ Welcome to the Pomona's Transit Management System------")
    conn = connection.MySQLConnection(user='root', password='212992',
                                    host='localhost',
                                    database='testing', port=3306)
    cursor = conn.cursor(buffered=True)
    authenticate(cursor, conn)    

    # Login to the system
    loggingCount = 1
    while loggingCount <= 3:
        username = input("Please input the username: ")
        password = input("Please input the password: ")
        cursor.execute(f"SELECT username from users WHERE Username='{username}' AND Password='{password}';")
        if not cursor.fetchone():
            print("Username and/or Password is incorrect! Please try again.\n")
            if loggingCount == 3:
                print("You have entered the wrong login info too many times!")
                print("The system is exiting now...")
                exit(0)
            loggingCount += 1
        else:
            print("Logging in now...")
            break

    displayAllCommands()
    while True:
        choice = input().strip()
        if choice == "1":
            # display the schedule of trips
            displaySchedule(cursor)
            displayAllCommands() 
        elif choice == "2":
            #delete a trip offering
            deleteTripOffering(cursor, conn)
            displayAllCommands() 
        elif choice == "3":
            # add a sets of trip offerings
            addTripOffering(cursor, conn)
            displayAllCommands() 
        elif choice == "4":
            # change the driver of a given trip offering
            changeDriver(cursor, conn)
            displayAllCommands() 
        elif choice == "5":
            # change the bus of a given trip offering
            changeBus(cursor, conn)
            displayAllCommands() 
        elif choice == "6":
            # display the stops of a given trips
            displayTripStops(cursor)
            displayAllCommands() 
        elif choice == "7":
            # insert the actual data of a given trip
            insertTripData(cursor, conn)
            displayAllCommands() 
        elif choice == "8":
            # add a driver
            addDriver(cursor, conn)
            displayAllCommands() 
        elif choice == "9":
            # add a bus 
            addBus(cursor, conn)
            displayAllCommands() 
        elif choice == "10":
            # delete a bus
            deleteBus(cursor, conn)
            displayAllCommands() 
        elif choice == "11":
            # exit the program
            print("The system is exiting now...")                            
            #close all the connection
            cursor.close()
            conn.close()  
            exit(0) 
        else:
            #re-display all the transaction options
            print("Invalid choice. Please select a valid number.")
            displayAllCommands()     

main()
