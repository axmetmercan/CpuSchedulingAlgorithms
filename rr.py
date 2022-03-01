from Reading import *


def findWaitingTime(processes, lengthOfTasks, burstTime, waitingTime, quantum, priority):
    remainBurstTime = [0] * lengthOfTasks
    aString ="Round Robin Scheduling\n\n"
    toStringrr = ""
    toStringrr += aString
    for i in range(lengthOfTasks):
        remainBurstTime[i] = burstTime[i]
    t = 0

    while (True):
        done = True

        for i in range(lengthOfTasks):

            if (remainBurstTime[i] > 0):
                done = False

                if (remainBurstTime[i] > quantum):
                    t += quantum
                    remainBurstTime[i] -= quantum

                    aString = "Will Run Name: {0}\n\nPriority: {1}\n\nBurst: {2}\n\nTask {0} Quantum {3} Finished\n\n".format("T" + str(processes[i]), priority[i], burstTime[i], quantum)
                    toStringrr += aString
                    #print(a)
                else:
                    t = t + remainBurstTime[i]
                    waitingTime[i] = t - burstTime[i]
                    remainBurstTime[i] = 0
                    #print(processes[i])
                    aString = "Will Run Name: {0}\n\nPriority: {1}\n\nBurst: {2}\n\nTask {0} Quantum Loop Totaly Completed\n\n".format("T" + str(processes[i]), priority[i], burstTime[i])
                    toStringrr += aString
                    #print(a)
        if (done == True):
            return toStringrr
            #break

def turnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]
def averageTurnArroundTime(processes, n, bt, quantum, a, priority):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, bt,wt, quantum,priority)
    turnAroundTime(processes, n, bt, wt, tat)
    a = findWaitingTime(processes, n, bt,wt, quantum,priority)

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]


    return a + "\nAverage waiting time = %.2f " % (total_wt / n) + "\nAverage turn around time = %.2f " % (total_tat / n)
