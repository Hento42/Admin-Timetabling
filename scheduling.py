import sqlite3, re
con = sqlite3.connect("databases.db") # Connecting to the database

editor = con.cursor()   # Linking to the database


# Creates a stack data structure to store the jobs in a LIFO priority order
class Stack(object):
    def __init__(self,items):
        self.__items = items
        self.__top = len(items) -1

    def push(self,item):
        self.__top += 1
        self.__items.append(item)

    def isEmpty(self):
        return self.__top == 0
  
    def pop(self):
        item = self.__items[self.__top]
        self.__items = self.__items[:self.__top]
        self.__top -= 1
        print(item)
        return item


# Creates a queue data structure to store the jobs in a FIFO priority order    
class Queue(object):
    def __init__(self,items):
        self.__items = items
        self.__len = len(items) - 1

    def isEmpty(self):
        return self.__len == 0

    def deQueue(self):
        if not self.isEmpty():
            item = self.__items[0]
            del(self.__items[0])
            self.__len -= 1
            return item
        else:
            return -1

    def enQueue(self,item):
        self.__items.append(item)    
        self.__len += 1


# Creating the classes for Staff and Jobs, and using inheritance to produce the different types of each
# In the "setter" methods, I have used a system to return 1 if successful, and 0 if not. 
# This will allow the code to navigate any potential errors encountered in the execution of the method.
class Staff(object):
    def __init__(self, id:int, fName:str, sName:str, level:dict, email:str, hours:list, attendance:dict):
        self.__staffID = id
        self.__firstName = fName
        self.__surname = sName
        self.__level = level
        self.__email = email
        self._hoursWorked = hours
        self.__attendance = attendance
        self.__type = ""

    def getName(self):
        return self.__staffID, self.__firstName, self.__surname
    
    def getEmail(self):
        return self.__staffID, self.__email
    
    def getLevel(self):
        return self.__staffID, self.__level
    
    def getHours(self):
        return self.__staffID, self._hoursWorked
    
    def getAttendance(self):
        return self.__staffID, self.__attendance
    
    def getType(self):
        return self.__staffID, self.__type
    
    def linkToJob(self):
        return self.__staffID, self.__firstName, self.__level
    
    def changeSurname(self, surname):
        if len(surname) > 0:
            self.__surname = surname
            return 1
        else:
            return 0

    def changeLevel(self,levelType,newLevel):
        valid = False
        try:
            if newLevel >= 0 and newLevel <= 3 and int(newLevel) == newLevel:
                valid = True

        except Exception:
            return 0
        keys = self.__level.keys()
        if levelType in keys and valid:
            self.__level[levelType] = newLevel
            return 1
        else:
            return 0

    def changeEmail(self,newEmail):
        if len(newEmail) > 0:
            self.__newEmail = newEmail
            return 1
        else:
            return 0

    def changeAttendance(self,day,newAttendance):
        if newAttendance == True or newAttendance == False:
            keys = self.__attendance.keys()
            if day in keys:
                self.__attendance = newAttendance
                return 1
            else:
                return 0
        else:
            return 0
        
    def changeHours(self, dayInt, newStartTime, newEndTime):
        valid = []
        if not str(dayInt).isdigit():
            return 0
        if (newStartTime != "" or newEndTime != ""):
            valid = re.findall("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]",newStartTime+","+newEndTime)
            if newEndTime == "" or newStartTime == "":
                valid.append("")
        if  len(valid) == 2:
            if dayInt < 0 or dayInt > 4 or (int(dayInt) != dayInt):
                return 0
            elif newStartTime == "":
                self._hoursWorked[dayInt] = [self._hoursWorked[dayInt][0], newEndTime]
                return 1
            elif newEndTime == "":
                self._hoursWorked[dayInt] = [newStartTime, self._hoursWorked[dayInt][1]]
                return 1
            else:
                self._hoursWorked[dayInt] = [newStartTime, newEndTime]
        else:
            return 0
    
    

class FullHours(Staff):
    def __init__(self, id:int, fName:str, sName:str, level:dict, email:str, hours:list, attendance:dict):
        self.__type = "Full"
        super().__init__(id, fName, sName, level, email, hours, attendance)

        
        
class SplitHours(Staff):
    def __init__(self, id, fName, sName, level, email, hours, attendance, splitStart:dict, splitEnd:dict):
        self.__splitHoursStart = splitStart
        self.__splitHoursEnd = splitEnd
        self.__type = "Split"
        super().__init__(id, fName, sName, level, email, hours, attendance)

    def moveSplitHour(self, dayInt, newStart, newEnd):
        try:
            dayInt = int(dayInt)
            valid = re.findall("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]",newStart+","+newEnd)
        except Exception:
            return 0
        else:
            if len(valid) == 2 and dayInt >= 0 and dayInt <= 4:
                self.__splitHoursStart[dayInt] = newStart
                self.__splitHoursEnd[dayInt] = newEnd
                return 1
            else:
                return 0

        
        
class ZeroHours(Staff):
    def __init__(self, id, fName, sName, level, email, hours, attendance, startTime:list, endTime:list):
        self.__startTime = startTime
        self.__endTime = endTime
        self.__type = "Zero"
        super().__init__(id, fName, sName, level, email, hours, attendance)

    def changeZeroHoursTimes(self, dayInt, newStart, newEnd):
        try:
            dayInt = int(dayInt)
            valid = re.findall("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]",newStart+","+newEnd)
        except Exception:
            return 0
        else:
            if len(valid) == 2 and dayInt >= 0 and dayInt <= 4:
                self.__splitHoursStart[dayInt] = newStart
                self.__splitHoursEnd[dayInt] = newEnd
                return 1
            else:
                return 0

    
class Job(object):
    def __init__(self,code:int,desc:str,priority:int,level:int,levelNum:int):
        self._jobCode = code
        self.__description = desc
        self.__priority = priority
        self.__level = level
        self.__levelNum = levelNum

    def getLevel(self):
        return self._jobCode, self.__level, self.__levelNum
    
    def getPriority(self):
        return self._jobCode, self.__priority

    def getDescription(self):
        return self._jobCode, self.__description

    def changePriority(self, newPriority):
        try:
            int(newPriority)
        except ValueError:
            return 0
        else:
            if newPriority == int(newPriority):
                self.__priority = newPriority
                return 1
            else:
                return 0

    def changeLevel(self,newLevel):
        valid = True
        try:
            if int(newLevel) == newLevel and newLevel >= 0 and newLevel <= 0:
                pass
            else:
                valid = False
        except Exception:
            return 0
        else:
            if valid:
                self.__level = newLevel
                return 1          
            else:
                return 0  


class DailyJob(Job):
    def __init__(self,dayHours:int,code,desc,priority,level,levelNum):
        self.__hoursPerDay = dayHours
        super().__init__(code,desc,priority,level,levelNum)

    def getHours(self):
        return self._jobCode, self.__hoursPerDay
        
    def changeDailyHours(self,newhours):
        if str(newhours).isdecimal() and newhours >= 0 and newhours <= 10.5:
            self.__hoursPerDay = newhours


class WeeklyJob(Job):
    def __init__(self, days:list, weekHours:int, code, desc, priority, level, levelNum):
        self.__days = days
        self.__weekHours = weekHours
        super().__init__(code, desc, priority, level, levelNum)

    def getDays(self):
        return self._jobCode, self.__days
        

class MonthlyJob(Job):
    def __init__(self, hoursNeeded:int, dayNeeded:str, complete:bool, code, desc, priority, level, levelNum):
        self.__hours = hoursNeeded
        self.__days = dayNeeded
        self.__done = complete
        super().__init__(code, desc, priority, level, levelNum)
        
        
class Reception(DailyJob):
    def __init__(self,desk:int,dayHours,code,desc,priority,level,levelNum):
        self.__desk = desk
        super().__init__(dayHours,code,desc,priority,level,levelNum)



# Subprogram for a recursive merge sort to sort the jobs by priority    
def mergeSort(numList):
    leftList = []
    rightList = []
    if len(numList) > 1:
        mid = len(numList) // 2
        leftList = numList[:mid]
        rightList = numList[mid:]
        mergeSort(rightList)       
        mergeSort(leftList) 
        a = 0; b = 0; c = 0
        while a < len(leftList) and b < len(rightList):
            if leftList[a] < rightList[b]:
                numList[c] = leftList[a]
                a += 1
            else:
                numList[c] = rightList[b]
                b += 1
            c += 1

        while a < len(leftList):
            numList[c] = leftList[a]
            a += 1; c += 1

        while b < len(rightList):
            numList[c] = rightList[b]
            b += 1; c += 1
    


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
    
    
con.commit() # Commits all the changes from the program