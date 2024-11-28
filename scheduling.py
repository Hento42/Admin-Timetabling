from classes import *      # Importing the classes and subprograms from classes.py for use in this program
                            # Split between files to improve modularisation
import sqlite3 

con = sqlite3.connect("databases.db") # Connecting to the database
editor = con.cursor()   # Linking to the database


# Subprogram for the scheduling part of the program, so it can be imported into and called by main.py
def schedule(pJobs, pStaff, pHours, day):
    maxPriority = 0
    priorities = [record[4] for record in pJobs]    # Gets a list of all the priorities
    mergeSort(priorities)                           
    maxPriority = priorities[-1]                    # Sorts the priorities and finds  the largest
    jobStack = Stack([])

    while maxPriority >= 0:
        currentList = []
        
        for job in pJobs:
            if job[4] == maxPriority:
                currentList.append(job)     # Generates a 2D list for ech priority level
                
        jobStack.push(currentList)          # Pushes this list to the stack, then decreases the max priority
        maxPriority -= 1
    
    # Placeholder for the scheduling algorithm        
    def schedulingAlgorithm(pJobList, pStaffList, pHourList, pDay):
        pass