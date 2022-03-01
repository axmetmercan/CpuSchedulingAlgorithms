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


def toFcfsString(newTasks):
    turnArroundTime = []
    totalWorkingTime = 0
    waitingTime = []
    n = len(newTasks[0])
    for i in range(n):

        if i == 0:
            totalWorkingTime += newTasks[3][0] + newTasks[1][i]
            turnArroundTime.append(totalWorkingTime - newTasks[1][i])
            waitingTime.append(turnArroundTime[i] - newTasks[3][i])
            # print(totalWorkingTime)

        else:
            totalWorkingTime += newTasks[3][i]
            turnArroundTime.append(totalWorkingTime - newTasks[1][i])
            waitingTime.append(turnArroundTime[i] - newTasks[3][i])


    totalString = "First Come First Served Scheduling\n\n"

    strin ="Will Run Name: {0}\n\nPriority: {1}\n\nBurst: {2}\n\nTask {0} Finished\n\n"
    for i in range(len(newTasks[0])):
        totalString += strin.format(newTasks[0][i], newTasks[2][i], newTasks[3][i])


    totalString += "\nAverage Turn Arround Time:  {0}\n\nAverage Waiting Time: {1}".format(sum(turnArroundTime) / n,sum(waitingTime) / n)

    return (totalString)
