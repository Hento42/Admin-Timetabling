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
                "FriFinish time,"
                "ContractType INTEGER,"
                "TotalHours INTEGER)")


editor.execute("CREATE TABLE Jobs ("
               "JobCode INTEGER PRIMARY KEY,"
               "Job TEXT,"
               "Type TEXT,"
               "HoursNeeded INTEGER,"
               "HourType INTEGER,"
               "DaysNeeded TEXT,"
               "Priority INTEGER,"
               "LevelNum INTEGER,"
               "LevelNeeded INTEGER,"
               "RecordName TEXT)")


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
               "EndDate date,"
               "StartTime time,"
               "EndTime time,"
               "PRIMARY KEY (StaffCode, StartDate))")


editor.execute("CREATE TABLE Attendance ("
               "StaffCode INTEGER PRIMARY KEY,"
               "Mon TEXT,"
               "Tue TEXT,"
               "Wed TEXT,"
               "Thur TEXT,"
               "Fri TEXT)")


editor.execute("CREATE TABLE HoursRecord ("
               "StaffCode INTEGER PRIMARY KEY,"
               "Reception INTEGER,"
               "Dispensary INTEGER,"
               "Admin INTEGER,"
               "Hurley INTEGER,"
               "Scanning INTEGER,"
               "Scripts INTEGER,"
               "NewRegistrations INTEGER,"
               "Other INTEGER,"
               "Total INTEGER)")


editor.execute("CREATE TABLE ExtraHours ("
               "StaffCode INTEGER,"
               "Day INTEGER,"
               "Type TEXT,"
               "StartTime Time,"
               "EndTime Time,"
               "PRIMARY KEY(StaffCode, Day))")



editor.execute("""INSERT INTO StaffDetails VALUES
               (0, "Maurice", "Moss", 2, 1, 1, 1, 2, "emailplaceholder", "08:00:00", "15:00:00", "08:00:00", "13:30:00", "08:00:00", "15:00:00", "08:00:00", "18:30:00", "11:30:00", "18:30:00", 0, 37),
               (1, "Roy", "Trenneman", 2, 1, 1, 0, 0, "emailplaceholder", "10:30:00", "18:30:00", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "16:00:00", 0, 37),
               (2, "Jen", "Barber", 3, 1, 0, 0, 0, "emailplaceholder", "08:00:00", "13:00:00", "12:00:00", "18:30:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "08:30:00", "14:30:00", 1, 37),
               (3, "Denholm", "Reynholm", 2, 1, 0, 0, 1, "emailplaceholder", "08:00:00", "13:00:00", "08:00:00", "18:30:00", "08:00:00", "13:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", 1, 37),
               (4, "Douglas", "Reynholm", 3, 1, 3, 0, 0, "emailplaceholder", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "08:45:00", "18:30:00", "08:00:00", "15:00:00", "08:45:00", "18:30:00", 0, 38),
               (5, "Richmond", "Avenal", 0, 0, 0, 0, 0, "emailplaceholder", "13:00:00", "18:30:00", "08:00:00", "13:30:00", "00:00:00", "00:00:00", "08:00:00", "13:30:00", "13:00:00", "18:30:00", 0, 22),
               (6, "Graham", "Linehan", 2, 0, 0, 3, 2, "emailplaceholder", "12:00:00", "16:30:00", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "08:00:00", "12:30:00", 0, 30),
               (7, "Richard", "Ayoade", 2, 1, 2, 0, 0, "emailplaceholder", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "10:30:00", "18:30:00", "08:00:00", "16:00:00", 0, 37),
               (8, "Chris", "O'Dowd", 2, 1, 1, 1, 0, "emailplaceholder", "08:00:00", "18:30:00", "08:00:00", "13:00:00", "08:00:00", "17:00:00", "08:00:00", "17:00:00", "08:00:00", "18:30:00", 1, 37),
               (9, "Katherine", "Parkinson", 1, 1, 0, 0, 0, "emailplaceholder", "08:00:00", "17:00:00", "00:00:00", "00:00:00", "08:00:00", "17:00:00", "09:00:00", "18:30:00", "09:00:00", "18:30:00", 0, 37),
               (10, "Chris", "Morris", 2, 1, 2, 0, 2, "emailplaceholder", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "11:30:00", "17:30:00", "08:30:00", "18:30:00", 0, 37),
               (11, "Matt", "Berry", 2, 1, 2, 3, 2, "emailplaceholder", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "10:30:00", "18:30:00", "00:00:00", "00:00:00", "08:00:00", "16:00:00", 0, 37),
               (12, "Noel", "Fielding", 0, 0, 0, 0, 0, "emailplaceholder", "08:00:00", "13:30:00", "13:00:00", "18:30:00", "13:00:00", "18:30:00", "00:00:00", "00:00:00", "13:00:00", "18:30:00", 0, 22),
               (13, "Daniel", "Carey", 0, 0, 0, 3, 0, "emailplaceholder", "08:30:00", "15:30:00", "08:30:00", "15:30:00", "08:30:00", "15:30:00", "00:00:00", "00:00:00", "00:00:00", "00:00:00", 0, 21),
               (14, "Bill", "Crouse", 0, 0, 0, 0, 0, "emailplaceholder", "00:00:00", "00:00:00", "08:00:00", "18:30:00", "08:00:00", "18:30:00", "00:00:00", "00:00:00", "08:00:00", "18:30:00", 2, 31.5)""")


editor.execute("""INSERT INTO ExtraHours VALUES
               (2, 3, 'Split', '12:00:00', '13:00:00'),
               (2, 4, 'Split', '12:00:00', '13:00:00'),
               (3, 2, 'Split', '12:00:00', '13:30:00'),
               (3, 4, 'Split', '12:00:00', '13:30:00'),
               (3, 5, 'Split', '12:00:00', '13:30:00'),
               (8, 1, 'Split', '12:00:00', '14:30:00'),
               (8, 3, 'Split', '12:00:00', '13:00:00'),
               (8, 4, 'Split', '12:00:00', '13:00:00'),
               (8, 5, 'Split', '12:00:00', '14:30:00'),
               (14, 2, 'Zero', "08:00:00", "18:30:00"),
               (14, 3, 'Zero', "08:00:00", "18:30:00"),
               (14, 5, 'Zero', "08:00:00", "18:30:00")""")


editor.execute("""INSERT INTO Jobs VALUES
               (0, "Reception 1", "D", 10.5, 1, "ALL", 1, -1, -1, "Reception"),
               (1, "Reception 2", "D", 10.5, 0, "ALL", 0, -1, -1, "Reception"),
               (2, "Reception 3", "D", 10.5, 2, "ALL", 4, 0, 1, "Reception"),
               (3, "Reception 4", "D", 10.5, 3, "SOME", 5, -1, -1, "Reception"),
               (4, "Dispensary", "D", 10.5, 0, "ALL", 0, 0, 2, "Dispensary"),
               (5, "Dispensary Help", "D", 10.5, 2, "SOME", 4, 0, 1, "Dispensary"),
               (6, "Hurley 1", "D", 10.5, 0, "ALL", 0, 1, 1, "Hurley"),
               (7, "Hurley 2", "D", 10.5, 1, "ALL", 1, 1, 1, "Hurley"),
               (8, "Hurley 3", "W", 10.5, 2, "ANY", 5, 1, 1, "Hurley"),
               (9, "Admin 1", "D", 10.5, 1, "ALL", 1, 3, 2, "Admin"),
               (10, "Admin 2", "D", 10.5, 1, "ALL", 3, 3, 2, "Admin"),
               (11, "Extra Admin 1", "D", 10.5, 3, "ALL", 6, -1, -1, "Admin"),
               (12, "Extra Admin 2", "D", 10.5, 3, "ALL", 6, -1, -1, "Admin"),
               (13, "Non-Workflow Scanning", "W", 2, 0, "ANY", 4, -1, -1, "Scanning"),
               (14, "Workflow Scanning", "D", 4, 0, "ALL", 1, 4, 2, "Scanning"),
               (15, "Weekly Scripts", "W", 4, 1, "FR", 2, 2, 1, "Scripts"),
               (16, "Monthly Scripts", "M", 2, 1, "TDB", 2, 2, 2, "Scripts"),
               (17, "New Registrations", "W", 3, 2, "ANY", 2, -1, -1, "NewRegistrations")""")


editor.execute("""INSERT INTO HoursRecord VALUES
               (0,0,0,0,0,0,0,0,0,0),
               (1,0,0,0,0,0,0,0,0,0),
               (2,0,0,0,0,0,0,0,0,0),
               (3,0,0,0,0,0,0,0,0,0),
               (4,0,0,0,0,0,0,0,0,0),
               (5,0,0,0,0,0,0,0,0,0),
               (6,0,0,0,0,0,0,0,0,0),
               (7,0,0,0,0,0,0,0,0,0),
               (8,0,0,0,0,0,0,0,0,0),
               (9,0,0,0,0,0,0,0,0,0),
               (10,0,0,0,0,0,0,0,0,0),
               (11,0,0,0,0,0,0,0,0,0),
               (12,0,0,0,0,0,0,0,0,0),
               (13,0,0,0,0,0,0,0,0,0),
               (14,0,0,0,0,0,0,0,0,0)""")


editor.execute("""INSERT INTO Attendance VALUES
               (0,"True","True","True","True","True"),
               (1,"True","True","True","True","True"),
               (2,"True","True","True","True","True"),
               (3,"True","True","True","True","True"),
               (4,"True","True","True","True","True"),
               (5,"True","True","True","True","True"),
               (6,"True","True","True","True","True"),
               (7,"True","True","True","True","True"),
               (8,"True","True","True","True","True"),
               (9,"True","True","True","True","True"),
               (10,"True","True","True","True","True"),
               (11,"True","True","True","True","True"),
               (12,"True","True","True","True","True"),
               (13,"True","True","True","True","True"),
               (14,"True","True","True","True","True")""")


editor.execute("""INSERT INTO AnnualLeave VALUES
               (1,'2025-01-31', '2025-01-31', '08:00:00', '18:30:00')""")

con.commit()