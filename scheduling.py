from classes import *      # Importing the classes and subprograms from classes.py for use in this program
                            # Split between files to improve modularisation
import sqlite3, datetime as D, calendar as C

con = sqlite3.connect("databases.db") # Connecting to the database
editor = con.cursor()   # Linking to the database


def linkJob():
    
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
                                ORDER BY JobCode ASC""")
        for theJob in jobList.fetchall():
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


jobStack, maxPriority = linkJob()
staffDict, levelNums = linkStaff()

while not jobStack.isEmpty():
    jobQueue = jobStack.pop()
    
print(levelNums)