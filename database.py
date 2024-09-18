import sqlite3
con = sqlite3.connect("databases.db") # Connecting to the database

editor = con.cursor()   # Linking to the database

#1editor.execute("CREATE TABLE StaffDetails ("
#1                "StaffCode INTEGER PRIMARY KEY,"
#1                "FirstName TEXT,"
#1                "Surname TEXT,"
#1                "Level INTEGER," 
#1                "Email TEXT,"
#1                "MonStart time,"
#1                "MonFinish time,"
#1                "TueStart time,"
#1                "TueFinish time," 
#1                "WedStart time,"
#1                "WedFinish time,"
#1                "ThurStart time,"
#1                "ThurFinish time,"
#1                "FriStart time,"
#1                "FriFinish time)")


#2editor.execute("""INSERT INTO StaffDetails VALUES
#2               (1, 'Arthur', 'Dent', 5, 'email@totallyrealemail.com', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00'),
#2               (2, 'Bowerick', 'Wowbagger', 10, 'anotheremail@totallyrealemail.com', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00'),
#2               (3, 'Zaphod', 'Beeblebrox', 1, 'president@theuniverse.com', '11:30:00', '14:00:00', '09:30:00', '10:00:00', '12:00:00', '15:00:00', '08:00:00', '09:00:00', '15:00:00', '16:00:00')""")


#3editor.execute("CREATE TABLE Jobs ("
#3               "JobCode INTEGER PRIMARY KEY,"
#3               "Job TEXT,"
#3               "WeekHoursNeeded INTEGER,"
#3               "DaysNeeded TEXT,"
#3               "Priority INTEGER)")


#4editor.execute("""INSERT INTO Jobs VALUES
#4               (1, 'President of the Universe', 8, 'MoTuWeTh', 0),
#4               (2, 'Drinking Tea', 14, 'MoTuWeThFr', 4),
#4               (3, 'Article Writing', 30, 'MoWeThFr', 2)""")


#5editor.execute("CREATE TABLE Week ("
#5               "ID INTEGER PRIMARY KEY,"
#5               "DAY TEXT,"
#5               "JobCode INTEGER,"
#5               "StaffCode INTEGER,"
#5               "StartTime time,"
#5               "EndTime time)")


#7editor.execute("CREATE TABLE AnnualLeave ("
#7               "StaffCode INTEGER,"
#7               "StartDate date,"
#7               "StartTime time,"
#7               "EndDate date,"
#7               "EndTime time,"
#7               "PRIMARY KEY (StaffCode, StartDate))")


editor.execute("CREATE TABLE Attendance ("
               "StaffCode INTEGER PRIMARY KEY,"
               "Monday TEXT,"
               "Tuesday TEXT,"
               "Wednesday TEXT,"
               "Thursday TEXT,"
               "Friday TEXT)")

editor.execute

con.commit()