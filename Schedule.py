import sys
from Reading import *
from writing import writeString



if sys.argv[1] =="fcfs":
    from Fcfs import *
    aList = seperatedLists(reading(sys.argv[2]))
    accordingToArrivalTime(aList)
    aList =toFcfsString(aList)
    writeString(aList)


elif sys.argv[1] == "sjf":
    from sjf1 import *
    sortedListAccordingArrivalTime = accordingToArrivalTime(seperatedLists(reading(sys.argv[2])))
    sortedByBurstime = sortedByBurstTime(accordingToArrivalTime(seperatedLists(reading(sys.argv[2]))))
    length = len(sortedListAccordingArrivalTime[0])
    work = work(sortedListAccordingArrivalTime, sortedByBurstTime(sortedListAccordingArrivalTime), length)
    writeString(toString(work, length))


elif sys.argv[1] == "pri":


    from Reading import reading

    def getWaitingTimeAsFCFS(waitingTime):

        cumulativeBurstTime = [0] * 5

        cumulativeBurstTime[0] = 0
        waitingTime[0] = 0

        for i in range(1, totalprocess):
            cumulativeBurstTime[i] = process[i - 1][1] + cumulativeBurstTime[i - 1]
            waitingTime[i] = cumulativeBurstTime[i] - process[i][0] + 1

            if (waitingTime[i] < 0):
                waitingTime[i] = 0

    def getTurnArroundTime(tat, wt):

        for i in range(totalprocess):
            tat[i] = process[i][1] + wt[i]

    def run():
        waitingTime = [0] * 5
        turnArroundTime = [0] * 5

        averageWaitingTime = 0
        averageTurnArroundTime = 0

        getWaitingTimeAsFCFS(waitingTime)
        getTurnArroundTime(turnArroundTime, waitingTime)

        stime = [0] * 5
        ctime = [0] * 5
        stime[0] = 1
        ctime[0] = stime[0] + turnArroundTime[0]

        for i in range(1, totalprocess):
            stime[i] = ctime[i - 1]
            ctime[i] = stime[i] + turnArroundTime[i] - waitingTime[i]



        for i in range(totalprocess):
            averageWaitingTime += waitingTime[i]
            averageTurnArroundTime += turnArroundTime[i]
            a = "T" + str(process[i][3])


        totalString = "Priority Scheduling\n\n"

        strin = "Will Run Name: {0}\n\nPriority: {1}\n\nBurst: {2}\n\nTask {0} Finished\n\n"
        for i in range(totalprocess):
            a = "T" + str(process[i][3])
            totalString += strin.format(a, process[i][2], process[i][1])
            # print(strin.format(newTasks[0][i], newTasks[2][i], newTasks[3][i]))

        totalString += "\nAverage Turn Arround Time:  {0}\n\nAverage Waiting Time: {1}".format((averageTurnArroundTime) / totalprocess,(averageWaitingTime) / totalprocess)
        return (totalString)


    if __name__ == '__main__':


        aList = reading(str(sys.argv[2]))

        totalprocess = len(aList)
        process = []
        for i in range(totalprocess):
            l = []
            for j in range(4):
                l.append(0)
            process.append(l)

        arrivaltime = []
        bursttime = []
        priority = []

        for i in range(len(aList)):
            arrivaltime.append(aList[i][1])
            bursttime.append(aList[i][3])
            priority.append(aList[i][2])

        #print(arrivaltime, bursttime, priority)

        #print()
        for i in range(totalprocess):
            process[i][0] = arrivaltime[i]
            process[i][1] = bursttime[i]
            process[i][2] = priority[i]
            process[i][3] = i + 1

        process = sorted(process, key=lambda x: x[2])
        process = sorted(process)
        writeString(run())



elif sys.argv[1] == "rr":
    from rr import *
    process = []
    burstTime = []
    priority = []

    aList = reading(str(sys.argv[2]))
    # print(a)
    for i in range(len(aList)):
        burstTime.append(aList[i][3])
        process.append(int(aList[i][0].replace("T", "")))
        priority.append(aList[i][2])
    n = len(process)



    timeQuantum = 10;
    averageTurnArroundTime(process, n, burstTime, timeQuantum, aList, priority)
    writeString(averageTurnArroundTime(process, n, burstTime, timeQuantum, aList, priority))

elif sys.argv[1] == "pri-rr":
    print("pri-rr is working")

