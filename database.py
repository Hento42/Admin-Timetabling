import sqlite3
con = sqlite3.connect("databases.db") # Connecting to the database

editor = con.cursor()   # Linking to the database
editor.execute("CREATE TABLE StaffDetails ("
                "StaffCode INTEGER PRIMARY KEY,"
                "FirstName TEXT,"
                "Surname TEXT,"
                "Level INTEGER," 
                "Email TEXT,"
                "MonStart date,"
                "MonFinish date,"
                "TueStart date,"
                "TueFinish date," 
                "WedStart date,"
                "WedFinish date,"
                "ThurStart date,"
                "ThurFinish date,"
                "FriStart date,"
                "FriFinish date)")