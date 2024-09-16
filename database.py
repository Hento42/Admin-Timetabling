import sqlite3
con = sqlite3.connect("databases.db") # Connecting to the database

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
               (3, 'Zaphod', 'Beeblebrox', 1, 'president@theuniverse.com', '11:30:00', '14:00:00', '09:30:00', '10:00:00', '12:00:00', '15:00:00', '08:00:00', '09:00:00', '15:00:00', '16:00:00')""")

con.commit()