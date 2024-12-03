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
        return self.__top == -1
  
    def pop(self):
        if not self.isEmpty():
            item = self.__items[self.__top]
            self.__items = self.__items[:self.__top]
            self.__top -= 1
            return item
        else:
            return -1


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
# For the instantiation of the classes, for any newly defined inputs I have included the data type.
# This allows me to easily see the data types of each variable to save time when utilising them later in the program.

# Parent class for the staff, with most attributes and methods defined
class Staff(object):
    def __init__(self, id:int, fName:str, sName:str, level:dict, email:str, hours:list, attendance:dict):
        self.__staffID = id
        self.__firstName = fName
        self.__surname = sName
        self.__level = level
        self.__email = email
        self._hoursWorked = hours
        self.__attendance = attendance
        self._type = ""

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
        return self.__staffID, self._type

    
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
        

    def displayDetails(self):
        print(f"""
ID: {self.__staffID}
First Name: {self.__firstName}
Surname: {self.__surname}
Email: {self.__email}
Levels: {self.__level}
Hours: {self._hoursWorked}
Attendance: {self.__attendance}
Contract type: {self._type}""")
        if self._type == "Split":
            print(f"Split hours start times: {self._splitHoursStart}")
            print(f"Split hours end times: {self._splitHoursEnd}")
        elif self._type == "Zero":
            print(f"Zero hours start times: {self._startTime}")
            print(f"Zero hours end time: {self._endTime}")
        print()
    
    
# Subclass for staff on a full hours contract. Doesn't contain any methods, and only has one separate attribute which is defined
class FullHours(Staff):
    def __init__(self, id, fName, sName, level, email, hours, attendance):
        super().__init__(id, fName, sName, level, email, hours, attendance)
        self._type = "Full"

        
# Subclass for a split hours contract, with two extra attributes for storing any splitHours that the staff have, and a method to 
# change the split hours for the staff
class SplitHours(Staff):
    def __init__(self, id, fName, sName, level, email, hours, attendance, splitStart:dict, splitEnd:dict):
        super().__init__(id, fName, sName, level, email, hours, attendance)
        self._splitHoursStart = splitStart
        self._splitHoursEnd = splitEnd
        self._type = "Split"

    def moveSplitHour(self, dayInt, newStart, newEnd):
        try:
            dayInt = int(dayInt)
            valid = re.findall("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]",newStart+","+newEnd)
        except Exception:
            return 0
        else:
            if len(valid) == 2 and dayInt >= 0 and dayInt <= 4:
                self._splitHoursStart[dayInt] = newStart
                self._splitHoursEnd[dayInt] = newEnd
                return 1
            else:
                return 0

        
# Subclass for zero hour contracts, with two extra attributes for the start and end of the times that they are "available" for use 
# on the zero hour contract, with a method to change it which utilises validation for the hours entered
class ZeroHours(Staff):
    def __init__(self, id, fName, sName, level, email, hours, attendance, startTime:list, endTime:list):
        super().__init__(id, fName, sName, level, email, hours, attendance)
        self._startTime = startTime
        self._endTime = endTime
        self._type = "Zero"

    def changeZeroHoursTimes(self, dayInt, newStart, newEnd):
        try:
            dayInt = int(dayInt)
            valid = re.findall("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]",newStart+","+newEnd)
        except Exception:
            return 0
        else:
            if len(valid) == 2 and dayInt >= 0 and dayInt <= 4:
                self._startTime[dayInt] = newStart
                self._endTime[dayInt] = newEnd
                return 1
            else:
                return 0


# Parent class for the job, with most attributes and methods defined    
# A large amount of defensive programming was used to reduce the risk of a severe error.
class Job(object):
    def __init__(self,code:int,desc:str,priority:int,levelNum:int,hourType:int,daysNeeded:str):
        self._jobCode = code        
        self._hourType = hourType
        self.__description = desc
        self.__priority = priority
        self.__levelNum = levelNum
        self.__days = daysNeeded

    def getLevelNum(self):
        return self._jobCode, self.__levelNum
    
    def getPriority(self):
        return self._jobCode, self.__priority

    def getDescription(self):
        return self._jobCode, self.__description

    def getDays(self):
        return self._jobCode, self.__days

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


    def changeHourType(self,newType):
        if type(newType) == int:
            if newType >= 0 and newType <= 3:
                self._hourType = newType
                return 1
            else:
                return 0
        else:
            return 0 

    def changeDays(self,newDays):
        # List of the codes used for the days for each job, they are self all explantory, except TDB - Two Days Before (the end of the month)
        DAYLIST = ["ALL", "ANY", "SOME", "TDB", "MO", "TU", "WE", "TH", "FR"]
        if newDays in DAYLIST:
            self.__days = newDays
            return 1
        else:
            return 0

# Subclass for the jobs which are needed daily. This includes a new attribute of hoursPerDay, which refers to the number of
# hours needed every day. 
class DailyJob(Job):
    def __init__(self,dayHours:int,code,desc,priority,levelNum,hourType,daysNeeded):
        self.__hoursPerDay = dayHours
        super().__init__(code,desc,priority,levelNum,hourType,daysNeeded)

    def getHours(self):
        return self._jobCode, self.__hoursPerDay, self._hourType
        
    def changeDailyHours(self,newhours):
        if str(newhours).isdecimal() and newhours >= 0 and newhours <= 10.5:
            self.__hoursPerDay = newhours
            return 1
        else:
            return 0


# Subclass for the weekly jobs, including the number of hours needed in the week
# Validation is in use to ensure the number of hours entered doesn't exceed the maximum possible
class WeeklyJob(Job):
    def __init__(self, weekHours:int, code, desc, priority, levelNum, hourType, daysNeeded):
        self.__weekHours = weekHours
        super().__init__(code, desc, priority, levelNum, hourType, daysNeeded)

    def getHours(self):
        return self._jobCode, self.__weekHours, self._hourType


    def changeHours(self, newHours):
        if str(newHours).isdecimal():
            if newHours >= 0 and newHours <= 52.5:
                self.__weekHours = newHours
                return 1
            else:
                return 0
        else:
            return 0


# Subclass for the small number of jobs thast are monthly. This includes the hours needed, similarly to the 
# previous subclasses, but also whether the job is complete for the month, so it isn't rescheduled if so
class MonthlyJob(Job):
    def __init__(self, hoursNeeded:int, complete:bool, code, desc, priority, levelNum, hourType, daysNeeded):
        self.__hours = hoursNeeded
        self.__done = complete
        super().__init__(code, desc, priority, levelNum, hourType, daysNeeded)

    def getHours(self):
        return self._jobCode, self.__hours, self._hourType

    def getValid(self):
        return self._jobCode, self.__done


    def changeHours(self, newHours):
        if str(newHours).isdecimal():
            if newHours >= 0:
                self.__hours = newHours
                return 1
            else:
                return 0
        else:
            return 0

    def changeStatus(self):
        if self.__done:
            self.__done = False
        else:
            self.__done = True
        return 1


# Subclass specifically for reception, since it requires the extra attribute of the desk number. This is an inhertance chain
# of 3, which is the largest chain that should be used, so it won't go any further.
class Reception(DailyJob):
    def __init__(self,desk:int,dayHours,code,desc,priority,levelNum, hourType, daysNeeded):
        self.__desk = desk
        super().__init__(dayHours,code,desc,priority,levelNum, hourType, daysNeeded)
    
    def getDesk(self):
        return self._jobCode, self.__desk

    def changeDesk(self, newDesk):
        if type(newDesk) == int:
            if newDesk >= 1 and newDesk <= 4:
                self.__desk = newDesk
                return 1
            else:
                return 0
        else:
            return 0 



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




# Subprogram to connect the data in the database tables to the classes instantiated above
def linkStaff():

    staffList = editor.execute("""SELECT *
                         FROM StaffDetails
                         ORDER BY StaffCode ASC""")

    staff = {}
    for record in staffList.fetchall():
        hourList = []
        for i in range(9,19):
            hourList.append(record[i])

        if record[19] == 0:
            staff[record[0]] = FullHours(record[0],record[1],record[2],{"DIS":record[3],"HUR":record[4],"SCR":record[5],"ADM":record[6],"WSC":record[7]},
                           record[8],hourList,{"MO":False,"TU":False,"WE":False,"TH":False,"FR":False})
        elif record[19] == 1:
            splitStart = {}
            splitEnd = {}
            splitTimes = editor.execute(f"""SELECT Day, StartTime, EndTime
                                        FROM SplitHours
                                        WHERE SplitHours.StaffCode = {record[0]}""")
            for day in splitTimes:
                splitStart[day[0]] = day[1]
                splitEnd[day[0]] = day[2]
            staff[record[0]] = SplitHours(record[0],record[1],record[2],{"DIS":record[3],"HUR":record[4],"SCR":record[5],"ADM":record[6],"WSC":record[7]},
                           record[8],hourList,{"MO":False,"TU":False,"WE":False,"TH":False,"FR":False},splitStart,splitEnd)
        elif record[19] == 2:
            zeroStart = ["","","","",""]
            zeroEnds = ["","","","",""]
            zeroTimes = editor.execute(f"""SELECT Day, StartTime, EndTime
                                        FROM ZeroHours
                                        WHERE ZeroHours.StaffCode = {record[0]}""")
            for item in zeroTimes.fetchall():
                zeroStart[item[0]-1] = item[1]
                zeroEnds[item[0]-1] = item[2]
            staff[record[0]] = ZeroHours(record[0],record[1],record[2],{"DIS":record[3],"HUR":record[4],"SCR":record[5],"ADM":record[6],"WSC":record[7]},
                           record[8],hourList,{"MO":False,"TU":False,"WE":False,"TH":False,"FR":False},zeroStart,zeroEnds)

    return staff
    

def linkJob():
    
    jobs = Stack([])
    
    priorities = editor.execute("""SELECT Priority
                                FROM JOBS
                                ORDER BY PRIORITY ASC""")
    
    maxpriority = priorities.fetchall()[-1][0]

    for priority in range(maxpriority+1,0,-1):
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
    

    return jobs


    
    
con.commit() # Commits all the changes from the program
test = linkStaff()
test[2].displayDetails()
test[0].displayDetails()
test2 = linkJob()
print(test2)
print(test2.pop().deQueue().getPriority())
