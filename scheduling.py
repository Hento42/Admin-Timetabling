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
    
    
