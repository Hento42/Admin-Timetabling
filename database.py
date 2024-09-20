import sqlite3
con = sqlite3.connect("databases.db") # Connecting to the database

editor = con.cursor()   # Linking to the database

#01editor.execute("CREATE TABLE StaffDetails ("
#01                "StaffCode INTEGER PRIMARY KEY,"
#01                "FirstName TEXT,"
#01                "Surname TEXT,"
#01                "Level INTEGER," 
#01                "Email TEXT,"
#01                "MonStart time,"
#01                "MonFinish time,"
#01                "TueStart time,"
#01                "TueFinish time," 
#01                "WedStart time,"
#01                "WedFinish time,"
#01                "ThurStart time,"
#01                "ThurFinish time,"
#01                "FriStart time,"
#01                "FriFinish time)")


#02editor.execute("""INSERT INTO StaffDetails VALUES
#02               (1, 'Arthur', 'Dent', 5, 'email@totallyrealemail.com', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00'),
#02               (2, 'Bowerick', 'Wowbagger', 10, 'anotheremail@totallyrealemail.com', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00'),
#02               (3, 'Zaphod', 'Beeblebrox', 1, 'president@theuniverse.com', '11:30:00', '14:00:00', '09:30:00', '10:00:00', '12:00:00', '15:00:00', '08:00:00', '09:00:00', '15:00:00', '16:00:00'),
#02               (4, 'Ford', 'Prefect', 7, 'fp@hhgttg.com', '00:00:00', '00:00:00', '09:00:00', '15:30:00', '08:30:00', '13:00:00', '10:30:00', '16:00:00', '08:00:00', '18:00:00'),
#02               (5, 'Prostetnic Vogon', 'Jeltz', 3, 'jeltz@vogfleet.com', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00'),
#02               (6, 'Mr.', 'Zarniwoop', 6, 'zw@hhgttg.com', '10:00:00', '15:30:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '09:00:00', '17:00:00')""")


#03editor.execute("CREATE TABLE Jobs ("
#03               "JobCode INTEGER PRIMARY KEY,"
#03               "Job TEXT,"
#03               "WeekHoursNeeded INTEGER,"
#03               "DaysNeeded TEXT,"
#03               "Priority INTEGER)")


#04editor.execute("""INSERT INTO Jobs VALUES
#04               (1, 'President of the Universe', 8, 'MoTuWeTh', 0),
#04               (2, 'Drinking Tea', 14, 'MoTuWeThFr', 4),
#04               (3, 'Article Writing', 30, 'MoWeThFr', 2),
#04               (4, 'Alphabetical insults', 35, 'MoTuWeThFr', 0),
#04               (5, 'Poetry', 12, 'TuWeThFr', 3),
#04               (6, 'Bypass Construction', 10, 'MoTuWeThFr', 5),
#04               (7, 'Intergalactic Cruising', 6, 'Fri', 1)""")


#05editor.execute("CREATE TABLE Week ("
#05               "ID INTEGER PRIMARY KEY,"
#05               "DAY TEXT,"
#05               "JobCode INTEGER,"
#05               "StaffCode INTEGER,"
#05               "StartTime time,"
#05               "EndTime time)")


#07editor.execute("CREATE TABLE AnnualLeave ("
#07               "StaffCode INTEGER,"
#07               "StartDate date,"
#07               "StartTime time,"
#07               "EndDate date,"
#07               "EndTime time,"
#07               "PRIMARY KEY (StaffCode, StartDate))")


#09editor.execute("CREATE TABLE Attendance ("
#09               "StaffCode INTEGER PRIMARY KEY,"
#09               "Monday TEXT,"
#09               "Tuesday TEXT,"
#09               "Wednesday TEXT,"
#09               "Thursday TEXT,"
#09               "Friday TEXT)")


#11editor.execute("CREATE TABLE HoursRecord ("
#11               "StaffCode INTEGER PRIMARY KEY,"
#11               "Reception INTEGER,"
#11               "Dispensary INTEGER,"
#11               "Admin INTEGER,"
#11               "Hurley INTEGER,"
#11               "Scanning INTEGER,"
#11               "Scripts INTEGER,"
#11               "NewRegistrations INTEGER,"
#11               "Other INTEGER)")


#13editor.execute("CREATE TABLE Levels ("
#13               "LEVEL INTEGER PRIMARY KEY,"
#13               "Reception BOOLEAN,"
#13               "Dispensary BOOLEAN,"
#13               "Admin BOOLEAN,"
#13               "Scripts BOOLEAN,"
#13               "Hurley BOOLEAN,"
#13               "Scanning BOOLEAN)")


editor.execute

con.commit()