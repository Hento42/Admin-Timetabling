# Creates a stack data structure to store the jobs in priority order
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


# Subprogram for a recursive merge sort to sort the jobs by priority    
def mergeSort(numList):
    newList = []
    leftList = []
    rightList = []
    if len(numList) > 1:
        mid = len(numList) // 2
        leftList = numList[:mid]
        rightList = numList[mid:]
        mergeSort(rightList)       
        mergeSort(leftList) 
        i = 0; j = 0; k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                numList[k] = leftList[i]
                i += 1
            else:
                numList[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            numList[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            numList[k] = rightList[j]
            j += 1; k += 1


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
    
    
# Random test data to ensure functionality
schedule(pJobs=[[1,"Reception",40,["Mon","Tue","Wed","Thur","Fri"],0],
          [2,"Dispensary",40,["Mon","Tue","Wed","Thur","Fri"],1],
          [3,"Admin",40,["Mon","Tue","Wed"],0],
          [4,"Scripts",40,["Mon","Tue","Wed","Thur","Fri"],6],
          [5,"Job 1",40,["Tue","Wed","Thur","Fri"],4],
          [6,"Job 2",40,["Mon","Wed","Fri"],5],
          [7,"Job 3",40,["Mon","Tue","Wed","Thur","Fri"],3],
          [8,"Job 4",40,["Thur","Fri"],2],
          [9,"Job 5",40,["Fri"],1],
          [10,"Job 6",40,["Mon","Tue","Wed","Thur","Fri"],3],
          [11,"Job 7",40,["Tue","Wed","Thur"],1],
          [12,"Job 8",40,["Mon"],0]], 
         pStaff=["aa", "Arthur Dent", [3,4,7,10],
         ["ab", "Ford Prefect", [2,5,8,10]],
         ["ac", "Zaphod Beeblebrox", [1,2,3]]],
         day="Mon", pHours=[]) # pHours left blank currently as is not needed yet and required formatting is currently unknown