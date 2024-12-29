from classes import *      # Importing the classes and subprograms from classes.py for use in this program
                            # Split between files to improve modularisation
import sqlite3, datetime as D, calendar as C

con = sqlite3.connect("databases.db") # Connecting to the database
editor = con.cursor()   # Linking to the database

staffDict, levelNums = linkStaff()
print(levelNums)
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
        print(theJobs)
        index = 0
        while index != len(theJobs)-1:
            if theJobs[index][7] != theJobs[index+1][7]:
                levelOne = levelNums[theJobs[index][7]]
                levelTwo = levelNums[theJobs[index+1][7]]
                if levelTwo > levelOne:
                    temp = theJobs[index]
                    theJobs[index] = theJobs[index+1]
                    theJobs[index+1] = temp
                else:
                    index += 1
            else:
                index += 1
                
        print(theJobs)
        print()
        
        for theJob in theJobs:
            if theJob[2] == "D":
                if "Reception" in theJob[1]:
                    jobQueue.enQueue(Reception(int(theJob[1][-1]),theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[4],theJob[5]))
                else:
                    jobQueue.enQueue(DailyJob(theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[4],theJob[5]))
            elif theJob[2] == "W":
                jobQueue.enQueue(WeeklyJob(theJob[3],theJob[0],theJob[1],theJob[6],theJob[7],theJob[4],theJob[5]))
            elif theJob[2] == "M":
                jobQueue.enQueue(MonthlyJob(theJob[3],False,theJob[0],theJob[1],theJob[6],theJob[7],theJob[4],theJob[5]))

        jobs.push(jobQueue)
    

    return jobs, maxpriority


jobStack, maxPriority = linkJob(levelNums)


while not jobStack.isEmpty():
    jobQueue = jobStack.pop()
    while not jobQueue.isEmpty():
        theJob = jobQueue.deQueue()
        
        
        # Need to find all available staff
        # Work out the different staff hour records - need to add data to table for that
        # Pick a staff member with not many hours comparatively
        # Must have right level for job
        # Must be covered enough based on the HourType code given
        # Covered for the correct number of hours
        # Check which days are needed
        # Factor in supervisors/trainers
        # Add trainees in where possible with other job objects, but only when possible 
        # Prioritise admin where level given in that way
