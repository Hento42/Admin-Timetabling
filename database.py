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


#01editor.execute("""INSERT INTO StaffDetails VALUES
#01               (1, 'Arthur', 'Dent', 5, 'email@totallyrealemail.com', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00'),
#01               (2, 'Bowerick', 'Wowbagger', 10, 'anotheremail@totallyrealemail.com', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00'),
#01               (3, 'Zaphod', 'Beeblebrox', 1, 'president@theuniverse.com', '11:30:00', '14:00:00', '09:30:00', '10:00:00', '12:00:00', '15:00:00', '08:00:00', '09:00:00', '15:00:00', '16:00:00'),
#01               (4, 'Ford', 'Prefect', 7, 'fp@hhgttg.com', '00:00:00', '00:00:00', '09:00:00', '15:30:00', '08:30:00', '13:00:00', '10:30:00', '16:00:00', '08:00:00', '18:00:00'),
#01               (5, 'Prostetnic Vogon', 'Jeltz', 3, 'jeltz@vogfleet.com', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00'),
#01               (6, 'Mr.', 'Zarniwoop', 6, 'zw@hhgttg.com', '10:00:00', '15:30:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '09:00:00', '17:00:00')""")


#2editor.execute("CREATE TABLE Jobs ("
#2               "JobCode INTEGER PRIMARY KEY,"
#2               "Job TEXT,"
#2               "WeekHoursNeeded INTEGER,"
#2               "DaysNeeded TEXT,"
#2               "Priority INTEGER)")


#02editor.execute("""INSERT INTO Jobs VALUES
#02               (1, 'President of the Universe', 8, 'MoTuWeTh', 0),
#02               (2, 'Drinking Tea', 14, 'MoTuWeThFr', 4),
#02               (3, 'Article Writing', 30, 'MoWeThFr', 2),
#02               (4, 'Alphabetical insults', 35, 'MoTuWeThFr', 0),
#02               (5, 'Poetry', 12, 'TuWeThFr', 3),
#02               (6, 'Bypass Construction', 10, 'MoTuWeThFr', 5),
#02               (7, 'Intergalactic Cruising', 6, 'Fri', 1)""")


#3editor.execute("CREATE TABLE Week ("
#3               "ID INTEGER PRIMARY KEY,"
#3               "DAY TEXT,"
#3               "JobCode INTEGER,"
#3               "StaffCode INTEGER,"
#3               "StartTime time,"
#3               "EndTime time)")


#4editor.execute("CREATE TABLE AnnualLeave ("
#4               "StaffCode INTEGER,"
#4               "StartDate date,"
#4               "StartTime time,"
#4               "EndDate date,"
#4               "EndTime time,"
#4               "PRIMARY KEY (StaffCode, StartDate))")


#5editor.execute("CREATE TABLE Attendance ("
#5               "StaffCode INTEGER PRIMARY KEY,"
#5               "Monday TEXT,"
#5               "Tuesday TEXT,"
#5               "Wednesday TEXT,"
#5               "Thursday TEXT,"
#5               "Friday TEXT)")


#6editor.execute("CREATE TABLE HoursRecord ("
#6               "StaffCode INTEGER PRIMARY KEY,"
#6               "Reception INTEGER,"
#6               "Dispensary INTEGER,"
#6               "Admin INTEGER,"
#6               "Hurley INTEGER,"
#6               "Scanning INTEGER,"
#6               "Scripts INTEGER,"
#6               "NewRegistrations INTEGER,"
#6               "Other INTEGER)")


#7editor.execute("CREATE TABLE Levels ("
#7               "LEVEL INTEGER PRIMARY KEY,"
#7               "Reception BOOLEAN,"
#7               "Dispensary BOOLEAN,"
#7               "Admin BOOLEAN,"
#7               "Scripts BOOLEAN,"
#7               "Hurley BOOLEAN,"
#7               "Scanning BOOLEAN)")


# Experimenting with the tables I have made to work out how they can be read and collaborate
names = editor.execute("""SELECT FirstName, Surname, Email
               FROM StaffDetails
               WHERE Level >= 5
               ORDER BY Level DESC""")
theNames = names.fetchall()
#print(names.fetchone()) # Once fetched for the first time, the variable is cleared
for record in theNames:
    print(record)


editor.execute("""INSERT INTO Week VALUES
               (1, 'Monday', 5, 5, '08:00:00', '11:00:00'),
               (2, 'Tuesday', 3, 4, '11:00:00', '14:00:00'),
               (3, 'Monday', 1, 3, '11:30:00', '14:00:00'),
               (4, 'Monday', 6, 5, '11:30:00', '16:00:00'),
               (5, 'Monday', 7, 6, '10:00:00', '13:00:00'),
               (6, 'Monday', 3, 6, '13:00:00', '15:30:00'),
               (7, 'Monday', 4, 2, '08:00:00', '15:00:00'),
               (8, 'Tuesday', 4, 2, '08:00:00', '15:00:00'),
               (9, 'Tuesday', 2, 1, '11:00:00', '14:30:00')""")





con.commit()