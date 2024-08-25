def schedule(pJobs, pStaff):
    
    currentPriority = 0
    currentList = []
    maxPriority = 0
    
    for job in pJobs:
        if job[4] == currentPriority:   # Collects the required jobs
            currentList.append(job)
        elif job[4] > maxPriority:   # Finds the greatest priority to allow the loop to be broken
            maxPriority = job[4]
            
    def schedulingAlgorithm(pJobList, pStaffList):
        pass
    
    schedulingAlgorithm(currentList,pStaff)
    
    while currentPriority < maxPriority:   # Loops until there are no job priorities left
        
        currentPriority += 1    # Increments the priority
        currentList = []
        
        for job in pJobs:
            if job[4] == currentPriority:   # Collects all the jobs for the given priority
                currentList.append(job)
        
        # Run sub for each priority
        
    # End sub