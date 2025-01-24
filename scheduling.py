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
                    jobQueue.enQueue(Reception(int(theJob[1][-1]),theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5]))
                else:
                    jobQueue.enQueue(DailyJob(theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5]))
            elif theJob[2] == "W":
                jobQueue.enQueue(WeeklyJob(theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5]))
            elif theJob[2] == "M":
                jobQueue.enQueue(MonthlyJob(theJob[3],False,theJob[0],theJob[1],theJob[6],theJob[7],theJob[8],theJob[4],theJob[5]))

        jobs.push(jobQueue)
    

    return jobs, maxpriority


jobStack, maxPriority = linkJob(levelNums)

LEVELKEY = {0:"DIS", 1:"HUR", 2:"SCR", 3:"ADM", 4:"WSC"}  # Constant for conversion between the different level identifiers
DAYS = ["MO","TU","WE","TH","FR"]

for day in DAYS:
    while not jobStack.isEmpty():       # Making its way down the stack
        jobQueue = jobStack.pop()
        
        while not jobQueue.isEmpty():       # Making its way through the queue
            theJob = jobQueue.deQueue()
            
            possibleStaff = []
            jobNum, levelNum, levelVal = theJob.getLevelNum()       # Collecting the values of the level for the job
            
            if levelNum != -1 and levelVal != -1:
                
                for key in staffDict.keys():                    # Iterating through all the staff to check which are able to do the job
                    theID, levels = staffDict[key].getLevel()
                    
                    if levels[LEVELKEY[levelVal]] == levelVal:
                        possibleStaff.append([key,staffDict[key]])
            else:
                for key in staffDict.keys():
                    possibleStaff.append([key,staffDict[key]])
                    
            print(possibleStaff)
            
            newList = []
            recordName = theJob.getRecord()
            staffTable = editor.execute(f"""SELECT StaffCode, {recordName}
                                    FROM HoursRecord
                                    ORDER BY {recordName} DESC""")
            staffList = staffTable.fetchall()
            print(staffList)
            
            for staffMem in possibleStaff:
                minHours = 999999
                
                
            
            
                
            
            
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
