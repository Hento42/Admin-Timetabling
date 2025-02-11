import sqlite3
con = sqlite3.connect("databases.db")  # Connecting to the database

editor = con.cursor()   # Linking to the database

editor.execute("CREATE TABLE StaffDetails ("
                "StaffCode INTEGER PRIMARY KEY,"
                "FirstName TEXT,"
                "Surname TEXT,"
                "Level INTEGER," 
                "Email TEXT,"
                "MonStart time,"
                "MonFinish time,"
                "TueStart time,"
                "TueFinish time," 
                "WedStart time,"
                "WedFinish time,"
                "ThurStart time,"
                "ThurFinish time,"
                "FriStart time,"
                "FriFinish time)")


editor.execute("""INSERT INTO StaffDetails VALUES
               (1, 'Arthur', 'Dent', 5, 'email@totallyrealemail.com', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:00:00'),
               (2, 'Bowerick', 'Wowbagger', 10, 'anotheremail@totallyrealemail.com', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00', '08:00:00', '15:00:00'),
               (3, 'Zaphod', 'Beeblebrox', 1, 'president@theuniverse.com', '11:30:00', '14:00:00', '09:30:00', '10:00:00', '12:00:00', '15:00:00', '08:00:00', '09:00:00', '15:00:00', '16:00:00'),
               (4, 'Ford', 'Prefect', 7, 'fp@hhgttg.com', '00:00:00', '00:00:00', '09:00:00', '15:30:00', '08:30:00', '13:00:00', '10:30:00', '16:00:00', '08:00:00', '18:00:00'),
               (5, 'Prostetnic Vogon', 'Jeltz', 3, 'jeltz@vogfleet.com', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00', '08:00:00', '16:00:00'),
               (6, 'Mr.', 'Zarniwoop', 6, 'zw@hhgttg.com', '10:00:00', '15:30:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00', '09:00:00', '17:00:00')""")


editor.execute("CREATE TABLE Jobs ("
               "JobCode INTEGER PRIMARY KEY,"
               "Job TEXT,"
               "WeekHoursNeeded INTEGER,"
               "DaysNeeded TEXT,"
               "Priority INTEGER)")


editor.execute("""INSERT INTO Jobs VALUES
               (1, 'President of the Universe', 8, 'MoTuWeTh', 0),
               (2, 'Drinking Tea', 14, 'MoTuWeThFr', 4),
               (3, 'Article Writing', 30, 'MoWeThFr', 2),
               (4, 'Alphabetical insults', 35, 'MoTuWeThFr', 0),
               (5, 'Poetry', 12, 'TuWeThFr', 3),
               (6, 'Bypass Construction', 10, 'MoTuWeThFr', 5),
               (7, 'Intergalactic Cruising', 6, 'Fri', 1)""")


editor.execute("CREATE TABLE Week ("
               "ID INTEGER PRIMARY KEY,"
               "Day TEXT,"
               "JobCode INTEGER,"
               "StaffCode INTEGER,"
               "StartTime time,"
               "EndTime time)")


editor.execute("CREATE TABLE AnnualLeave ("
               "StaffCode INTEGER,"
               "StartDate date,"
               "StartTime time,"
               "EndDate date,"
               "EndTime time,"
               "PRIMARY KEY (StaffCode, StartDate))")


editor.execute("CREATE TABLE Attendance ("
               "StaffCode INTEGER PRIMARY KEY,"
               "Monday TEXT,"
               "Tuesday TEXT,"
               "Wednesday TEXT,"
               "Thursday TEXT,"
               "Friday TEXT)")


editor.execute("CREATE TABLE HoursRecord ("
               "StaffCode INTEGER PRIMARY KEY,"
               "Reception INTEGER,"
               "Dispensary INTEGER,"
               "Admin INTEGER,"
               "Hurley INTEGER,"
               "Scanning INTEGER,"
               "Scripts INTEGER,"
               "NewRegistrations INTEGER,"
               "Other INTEGER)")


editor.execute("CREATE TABLE Levels ("
               "LEVEL INTEGER PRIMARY KEY,"
               "Reception BOOLEAN,"
               "Dispensary BOOLEAN,"
               "Admin BOOLEAN,"
               "Scripts BOOLEAN,"
               "Hurley BOOLEAN,"
               "Scanning BOOLEAN)")


# Experimenting with the tables I have made to work out how they can be read and collaborate
names = editor.execute("""SELECT FirstName, Surname, Email
               FROM StaffDetails
               WHERE Level >= 5
               ORDER BY Level DESC""")
theNames = names.fetchall()
print(names.fetchone()) # Once fetched for the first time, the variable is cleared
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


monJobs = editor.execute("""SELECT FirstName, Surname, Email, Job
                         FROM Week, StaffDetails, Jobs
                         WHERE Week.Day = 'Monday'
                         AND Week.JobCode = Jobs.JobCode
                         AND Week.StaffCode = StaffDetails.StaffCode
                         ORDER BY Surname ASC""")

for record in monJobs.fetchall():
    print(record)

wowJobs = editor.execute("""SELECT Job, Day, StartTime
                         FROM Week, Jobs, StaffDetails
                         WHERE Week.StaffCode = StaffDetails.StaffCode
                         AND Week.JobCode = Jobs.Jobcode
                         AND StaffDetails.FirstName = 'Bowerick' 
                         AND StaffDetails.Surname = 'Wowbagger'
                         ORDER BY StartTime ASC""")

for record in wowJobs.fetchall():
    print(record)


editor.execute("""UPDATE Week
               SET StartTime = '09:00:00'
               WHERE StaffCode = 2
               AND Day = 'Monday'""")


wowJobs = editor.execute("""SELECT Job, Day, StartTime
                         FROM Week, Jobs, StaffDetails
                         WHERE Week.StaffCode = StaffDetails.StaffCode
                         AND Week.JobCode = Jobs.Jobcode
                         AND StaffDetails.FirstName = 'Bowerick' 
                         AND StaffDetails.Surname = 'Wowbagger'
                         ORDER BY StartTime ASC""")

for record in wowJobs.fetchall():
    print(record)

    
con.commit()