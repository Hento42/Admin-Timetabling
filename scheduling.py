from classes import *      # Importing the classes and subprograms from classes.py for use in this program
                            # Split between files to improve modularisation
import sqlite3, datetime as D, calendar as C

con = sqlite3.connect("databases.db") # Connecting to the database
editor = con.cursor()   # Linking to the database

theDate = D.date.today()


staffDict, levelNums = linkStaff()
def linkJob(pLevels):
    
    jobs = Stack([])
    
    priorities = editor.execute("""SELECT Priority
                                FROM JOBS
                                ORDER BY PRIORITY ASC""")
    
    maxpriority = priorities.fetchall()[-1][0]

    for priority in range(maxpriority,-1,-1):
        jobQueue = Queue([])
        jobList = editor.execute(f"""SELECT *
                                FROM Jobs
                                WHERE Priority = {priority}
                                ORDER BY HourType ASC, HoursNeeded ASC""")
        
        theJobs = jobList.fetchall()
        index = 0
        while index != len(theJobs)-1:
            if theJobs[index][7] != theJobs[index+1][7]:
                levelOne = levelNums[theJobs[index][7]][theJobs[index][8]]
                levelTwo = levelNums[theJobs[index+1][7]][theJobs[index+1][8]]
                if levelOne > levelTwo:
                    temp = theJobs[index]
                    theJobs[index] = theJobs[index+1]
                    theJobs[index+1] = temp
                else:
                    index += 1
            else:
                index += 1

        for theJob in theJobs:
            if theJob[2] == "D":
                if "Reception" in theJob[1]:
                    jobQueue.enQueue(Reception(int(theJob[1][-1]),theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5],theJob[9]))
                else:
                    jobQueue.enQueue(DailyJob(theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5],theJob[9]))
            elif theJob[2] == "W":
                jobQueue.enQueue(WeeklyJob(theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5],theJob[9]))
            elif theJob[2] == "M":
                jobQueue.enQueue(MonthlyJob(theJob[3],False,theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5],theJob[9]))

        jobs.push(jobQueue)
    

    return jobs, maxpriority


def resetAttendance():                  # Resetting the Attendance table so it can be repopulated with False
    editor.execute("""UPDATE Attendance
                            SET Mon = 'True', Tue = 'True', Wed = 'True', Thur = 'True', Fri = 'True'""")




def UpdateAttendance(pDay):              # Checking each Staff members Attendance based on their hours worked to update Attendance accordingly

    theDate = D.date.today()

    if pDay == "Mon":

        editor.execute(f"""UPDATE Attendance
                        SET Mon = 'False'
                        WHERE Attendance.StaffCode IN (SELECT StaffDetails.StaffCode
                                FROM StaffDetails
                                WHERE (StaffDetails.MonStart = '00:00:00'
                                OR StaffDetails.MonFinish = '00:00:00'))
                                """)
            
    elif pDay == "Tue":

        editor.execute(f"""UPDATE Attendance
                        SET Tue = 'False'
                        WHERE Attendance.StaffCode IN (SELECT StaffDetails.StaffCode
                                FROM StaffDetails
                                WHERE StaffDetails.TueStart = '00:00:00'
                                OR StaffDetails.TueFinish = '00:00:00')
                                """)
        
    elif pDay == "Wed":

        editor.execute(f"""UPDATE Attendance
                        SET Wed = 'False'
                        WHERE Attendance.StaffCode IN (SELECT StaffDetails.StaffCode
                                FROM StaffDetails
                                WHERE StaffDetails.WedStart = '00:00:00'
                                OR StaffDetails.WedFinish = '00:00:00')
                       """)

    elif pDay == "Thur":

        editor.execute(f"""UPDATE Attendance
                        SET Thur = 'False'
                        WHERE Attendance.StaffCode IN (SELECT StaffDetails.StaffCode
                                FROM StaffDetails
                                WHERE StaffDetails.ThurStart = '00:00:00'
                                OR StaffDetails.ThurFinish = '00:00:00')
                       """)
                       
    elif pDay == "Fri":

        editor.execute(f"""UPDATE Attendance
                        SET Fri = 'False'
                        WHERE Attendance.StaffCode IN (SELECT StaffDetails.StaffCode
                                FROM StaffDetails
                                WHERE StaffDetails.FriStart = '00:00:00'
                                OR StaffDetails.FriFinish = '00:00:00')
                       """)



        
resetAttendance()
        
UpdateAttendance("Mon")
UpdateAttendance("Tue")
UpdateAttendance("Wed")        
UpdateAttendance("Thur")
UpdateAttendance("Fri")

con.commit()




LEVELKEY = {0:"DIS", 1:"HUR", 2:"SCR", 3:"ADM", 4:"WSC"}  # Constant for conversion between the different level identifiers
DAYS = ["MO","TU","WE","TH","FR"]

for day in DAYS:
    jobStack, maxPriority = linkJob(levelNums)
    print((day.upper()))
    print( )
    print( )
    while not jobStack.isEmpty():       # Making its way down the stack
        jobQueue = jobStack.pop()
        
        while not jobQueue.isEmpty():       # Making its way through the queue
            theJob = jobQueue.deQueue()
            jobID, jobDays = theJob.getDays()
            
            if jobDays == "ALL" or jobDays == "SOME" or jobDays == "ANY" or day in jobDays:
                availableStaff = {}
                jobNum, levelNum, levelVal = theJob.getLevelNum()
                
                                            # Collecting all the staff working on each day
                if day == "MO":
                    possibleStaff = editor.execute("""SELECT StaffCode
                                                FROM Attendance
                                                WHERE Mon = 'True'""")
                elif day == "TU":
                    possibleStaff = editor.execute("""SELECT StaffCode
                                                FROM Attendance
                                                WHERE Tue = 'True'""")
                elif day == "WE":
                    possibleStaff = editor.execute("""SELECT StaffCode
                                                FROM Attendance
                                                WHERE Wed = 'True'""")
                elif day == "TH":
                    possibleStaff = editor.execute("""SELECT StaffCode
                                                FROM Attendance
                                                WHERE Thur = 'True'""")
                elif day == "FR":
                    possibleStaff = editor.execute("""SELECT StaffCode
                                                FROM Attendance
                                                WHERE Fri = 'True'""")
                    
                theStaff = possibleStaff.fetchall()

                for staff in theStaff:
                    theID, levels = staffDict[staff[0]].getLevel()

                    if levelNum != -1 and levelVal != -1:
                        if levels[LEVELKEY[levelNum]] >= levelVal:
                            availableStaff[staff[0]] =  staffDict[staff[0]]
                    else:
                        availableStaff[staff[0]] =  staffDict[staff[0]]

                #print(availableStaff)
                #print(type(availableStaff[0]).__name__)
                #print(theJob.getRecord())
                #print(theJob.getDescription())
                startStaff = {}
                otherStaff = {}
                theKeys = [14]

                for key in availableStaff.keys():
                    theTimes = editor.execute(f"""SELECT MonStart, TueStart, WedStart, ThurStart, FriStart
                                              FROM StaffDetails
                                              WHERE StaffCode = {key}""")
                    timeList = theTimes.fetchall()
                    index = DAYS.index(day)

                    startTime = timeList[0][index]
                    #print(startTime)

                    busy = editor.execute(f"""SELECT StartTime, EndTime
                                          FROM Week
                                          WHERE StaffCode = {key}
                                          AND Day = '{day}'""")
                    
                    # For the morning, checking which staff are available for jobs needed from 8
                    
                    busyList = busy.fetchall()
                    if len(busyList) > 0:
                        if busyList[0][index] >= "08:00:00" and busyList[0][index] <= "13:00:00":     # Checking to see if the staff's job start time is between 8 and 1 - in the morning part
                            theKeys.append(key)


                    if startTime != "08:00:00":
                        theKeys.append(key)

                    if key not in theKeys:
                        startStaff[key] = availableStaff[key]
                    

                    


                print(startStaff)
                print(otherStaff)



            elif jobDays == "TDB":
                pass

            
            

            

                
                
            
            
                
            
            
            # Work out the different staff hour records
            # Pick a staff member with not many hours comparatively
            # Must have right level for job
            # Must be covered enough based on the HourType code given
            # Covered for the correct number of hours
            # Check which days are needed
            # Factor in supervisors/trainers
            # Add trainees in where possible with other job objects, but only when possible 
            # Prioritise admin where level given in that way
            # Changeover of jobs between 12:00 and 13:30, lunch not needed as worked out by staff
