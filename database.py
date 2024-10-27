import sqlite3
con = sqlite3.connect("databases.db") # Connecting to the database

editor = con.cursor()   # Linking to the database

editor.execute("CREATE TABLE StaffDetails ("
                "StaffCode INTEGER PRIMARY KEY,"
                "FirstName TEXT,"
                "Surname TEXT,"
                "Disp INTEGER,"
                "Hurley INTEGER,"
                "Scripts INTEGER,"
                "Admin INTEGER,"
                "WorkflowScanning INTEGER," 
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


editor.execute("CREATE TABLE Jobs ("
               "JobCode INTEGER PRIMARY KEY,"
               "Job TEXT,"
               "Type TEXT,"
               "HoursNeeded INTEGER,"
               "HourType INTEGER"
               "DaysNeeded TEXT,"
               "Priority INTEGER)")


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


editor.execute("CREATE TABLE SplitHours ("
               "StaffCode INTEGER,"
               "Day INTEGER,"
               "StartTime Time,"
               "EndTime Time,"
               "PRIMARY KEY(StaffCode, Day))")


editor.execute("CREATE TABLE ZeroHours ("
               "StaffCode INTEGER,"
               "Day INTEGER,"
               "StartTime Time,"
               "EndTime Time,"
               "PRIMARY KEY(StaffCode, Day))")


editor.execute("""INSERT INTO StaffDetails VALUES
               (0, "Maurice", "Moss", 2, 1, 1, 1, 2, "emailplaceholder", "08:00:00", "15:00:00", "08:00:00", "13:30:00", "08:00:00", "15:00:00", "08:00:00", "18:30:00", "11:30:00", "18:30:00"),
               (1, "Roy", "Trenneman", 2, 1, 1, 0, 0, "emailplaceholder", "10:30:00", "18:30:00", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "16:00:00"),
               (2, "Jen", "Barber", 3, 1, 0, 0, 0, "emailplaceholder", "08:00:00", "13:00:00", "12:00:00", "18:30:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "08:30:00", "14:30:00"),
               (3, "Denholm", "Reynholm", 2, 1, 0, 0, 1, "emailplaceholder", "08:00:00", "13:00:00", "08:00:00", "18:30:00", "08:00:00", "13:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00"),
               (4, "Douglas", "Reynholm", 3, 1, 3, 0, 0, "emailplaceholder", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "08:45:00", "18:30:00", "08:00:00", "15:00:00", "08:45:00", "18:30:00"),
               (5, "Richmond", "Avenal", 0, 0, 0, 0, 0, "emailplaceholder", "13:00:00", "18:30:00", "08:00:00", "13:30:00", "00:00:00", "00:00:00", "08:00:00", "13:30:00", "13:00:00", "18:30:00"),
               (6, "Graham", "Linehan", 2, 0, 0, 3, 2, "emailplaceholder", "12:00:00", "16:30:00", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "08:00:00", "12:30:00"),
               (7, "Richard", "Ayoade", 2, 1, 2, 0, 0, "emailplaceholder", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "10:30:00", "18:30:00", "08:00:00", "16:00:00"),
               (8, "Chris", "O'Dowd", 2, 1, 1, 1, 0, "emailplaceholder", "08:00:00", "18:30:00", "08:00:00", "13:00:00", "08:00:00", "17:00:00", "08:00:00", "17:00:00", "08:00:00", "18:30:00"),
               (9, "Katherine", "Parkinson", 1, 1, 0, 0, 0, "emailplaceholder", "08:00:00", "17:00:00", "00:00:00", "00:00:00", "08:00:00", "17:00:00", "09:00:00", "18:30:00", "09:00:00", "18:30:00"),
               (10, "Chris", "Morris", 2, 1, 2, 0, 2, "emailplaceholder", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "11:30:00", "17:30:00", "08:30:00", "18:30:00"),
               (11, "Matt", "Berry", 2, 1, 2, 3, 2, "emailplaceholder", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "10:30:00", "18:30:00", "00:00:00", "00:00:00", "08:00:00", "16:00:00"),
               (12, "Noel", "Fielding", 0, 0, 0, 0, 0, "emailplaceholder", "08:00:00", "13:30:00", "13:00:00", "18:30:00", "13:00:00", "18:30:00", "00:00:00", "00:00:00", "13:00:00", "18:30:00"),
               (13, "Daniel", "Carey", 0, 0, 0, 3, 0, "emailplaceholder", "08:30:00", "15:30:00", "08:30:00", "15:30:00", "08:30:00", "15:30:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00"),
               (14, "Bill", "Crouse", 0, 0, 0, 0, 0, "emailplaceholder", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "08:00:00", "18:30:00")""")


editor.execute("""INSERT INTO SplitHours VALUES
               (2, 3, '12:00:00', '13:00:00'),
               (2, 4, '12:00:00', '13:00:00'),
               (3, 2, '12:00:00', '13:30:00'),
               (3, 4, '12:00:00', '13:30:00'),
               (3, 5, '12:00:00', '13:30:00'),
               (8, 1, '12:00:00', '14:30:00'),
               (8, 3, '12:00:00', '13:00:00'),
               (8, 4, '12:00:00', '13:00:00'),
               (8, 5, '12:00:00', '14:30:00')""")


editor.execute("""INSERT INTO ZeroHours VALUES
               (14, 2, "08:00:00", "18:30:00"),
               (14, 3, "08:00:00", "18:30:00"),
               (14, 5, "08:00:00", "18:30:00")""")


editor.execute("""INSERT INTO Jobs VALUES
               (0, "Reception 1", "D", 10.5, 1, "ALL", 1),
               (1, "Reception 2", "D", 10.5, 0, "ALL", 0),
               (2, "Reception 3", "D", 10.5, 2, "ALL", 3),
               (3, "Reception 4", "D", 10.5, 3, "SOME", 5),
               (4, "Dispensary", "D", 10.5, 0, "ALL", 0),
               (5, "Dispensary Help", "D", 2, 10.5, "SOME", 2),
               (6, "Hurley 1", "D", 10.5, 0, "ALL", 0),
               (7, "Hurley 2", "D", 10.5, 1, "ALL", 1),
               (8, "Hurley 3", "W", 10.5, 2, "ANY", 3),
               (9, "Admin 1", "D", 10.5, 1, "ALL", 0),
               (10, "Admin 2", "D", 10.5, 1, "ALL", 1),
               (11, "Extra Admin 1", "D", 10.5, 3, "ALL", 4),
               (12, "Extra Admin 2", "D", 10.5, 3, "All", 5),
               (13, "Non-Workflow Scanning", "W", 2, 0, "ANY", 3),
               (14, "Workflow Scanning", ...),
               (15, "Weekly Scripts", "W", 4, 1, "Fr", 2),
               (16, "Monthly Scripts", "M", 2, 1, "TDB", 2),
               (17, "New Registrations", "W", 3, 2, "ANY", 2)""")


con.commit()