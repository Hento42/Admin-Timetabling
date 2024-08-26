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


def schedule(pJobs, pStaff, pHours, day):
    
    maxPriority = 0
    
    priorities = [record[4] for record in pJobs]
    mergeSort(priorities)

    maxPriority = priorities[-1]
    jobStack = Stack([])
    
    while maxPriority >= 0:
        currentList = []
        for job in pJobs:
            if job[4] == maxPriority:
                currentList.append(job)
        jobStack.push(currentList)
        maxPriority -= 1
    
    jobStack.pop()
    
            
    def schedulingAlgorithm(pJobList, pStaffList, pHourList, pDay):
        pass
    
    
    
schedule(pJobs=[[1,"Reception",40,["Mon","Tue","Wed","Thur","Fri"],0],
          [2,"Dispensary",40,["Mon","Tue","Wed","Thur","Fri"],1],
          [3,"Dispensary",40,["Mon","Tue","Wed"],0],
          [4,"Dispensary",40,["Mon","Tue","Wed","Thur","Fri"],6],
          [5,"Dispensary",40,["Tue","Wed","Thur","Fri"],4],
          [6,"Dispensary",40,["Mon","Wed","Fri"],5],
          [7,"Dispensary",40,["Mon","Tue","Wed","Thur","Fri"],3],
          [8,"Dispensary",40,["Thur","Fri"],2],
          [9,"Dispensary",40,["Fri"],1],
          [10,"Dispensary",40,["Mon","Tue","Wed","Thur","Fri"],3],
          [11,"Dispensary",40,["Tue","Wed","Thur"],1],
          [12,"Dispensary",40,["Mon"],0]], 
         pStaff=["aa", "Arthur Dent", [3,4,7,10],
         ["ab", "Ford Prefect", [2,5,8,10]]],
         day="Mon", pHours=[])