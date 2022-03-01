def accordingToArrivalTime(newTasks):
    n = len(newTasks[0])
    for i in range(n):
        for j in range(i + 1, n):
            if newTasks[1][i] > newTasks[1][j]:
                newTasks[1][i], newTasks[1][j] = newTasks[1][j], newTasks[1][i]
                newTasks[0][i], newTasks[0][j] = newTasks[0][j], newTasks[0][i]
                newTasks[2][i], newTasks[2][j] = newTasks[2][j], newTasks[2][i]
                newTasks[3][i], newTasks[3][j] = newTasks[3][j], newTasks[3][i]

    return newTasks


def secStep(sortedList):
    # total Execution Time
    sortedList.append([])
    # turnarround Time
    sortedList.append([])
    # Waiting Time
    sortedList.append([])

    # First job exucution time
    sortedList[4].append(sortedList[1][0] + sortedList[3][0])
    # Turnarround Time
    sortedList[6].append(sortedList[4][0] - sortedList[1][0])
    # Waiting Time
    sortedList[5].append(sortedList[6][0] - sortedList[3][0])
    #print(sortedList)


def sortedByBurstTime(sortedByArrival):
    workingTime = []
    for i in range(1, len(sortedByArrival[0])):
        workingTime.append(sortedByArrival[3][i])
    workingTime.sort()
    return workingTime


def work(sortedByArrival, sortedByBurstTime, n):
    newList = []
    #print(sortedByArrival)
    for i in range(len(sortedByArrival)):
        newList.append([])

    for k in range(0, 4):
        newList[k].append(sortedByArrival[k][0])

    # print(newList)
    # print(sortedByBurstTime)

    for l in range(1, n):
        valueOf = sortedByBurstTime[l - 1]
        indexInArrivalList = sortedByArrival[3].index(valueOf)
        newList[0].append(sortedByArrival[0][indexInArrivalList])
        newList[1].append(sortedByArrival[1][indexInArrivalList])
        newList[2].append(sortedByArrival[2][indexInArrivalList])
        newList[3].append(sortedByArrival[3][indexInArrivalList])

        for m in range(4):
            sortedByArrival[m].pop(indexInArrivalList)
    #print(newList)
    return newList


def toString(newList, n):
    turnArroundTime = []
    totalWorkingTime = 0
    waitingTime = []

    for i in range(n):

        if i == 0:
            totalWorkingTime += newList[3][0] + newList[1][i]
            turnArroundTime.append(totalWorkingTime - newList[1][i])
            waitingTime.append(turnArroundTime[i] - newList[3][i])
            #print(totalWorkingTime)

        else:
            totalWorkingTime += newList[3][i]
            turnArroundTime.append(totalWorkingTime - newList[1][i])
            waitingTime.append(turnArroundTime[i] - newList[3][i])
            #print(totalWorkingTime)

    totalString = "Shortest Job First Scheduling\n\n"

    strin = "Will Run Name: {0}\n\nPriority: {1}\n\nBurst: {2}\n\nTask {0} Finished\n\n"
    for i in range(len(newList[0])):
        totalString += strin.format(newList[0][i], newList[2][i], newList[3][i])
        # print(strin.format(newTasks[0][i], newTasks[2][i], newTasks[3][i]))
    totalString += "\nAverage Turn Arround Time:  {0}\n\nAverage Waiting Time: {1}".format(sum(turnArroundTime)/n,sum(waitingTime)/n)

    return totalString


    #print(turnArroundTime, waitingTime, sum(turnArroundTime) / n, sum(waitingTime) / n)
    ### Waiting = Turnarround time - burst time
    ### Turnarround = Bitirdiği süre - geldiği süre

