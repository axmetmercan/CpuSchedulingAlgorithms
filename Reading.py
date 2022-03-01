def reading(filename):
    with open(filename, "r") as tempF:
        rangeOfFile = len(tempF.readlines())
        tempF.close()
        #print(rangeOfFile)

    with open("schedule.txt", "r") as file:

        task = []

        for i in range(rangeOfFile):
            s = file.readline()
            s = s.replace("\n","").split(",")
            if s != [""]:
                task.append(s)
        for i in range(len(task)):
            for j in range(4):
                task[i][j] = task[i][j].replace(" ", "")
                if j != 0 :
                    task[i][j] = int (task[i][j])


        return task

def seperatedLists(newTask):
    TaskName = []
    arrivalTime =[]
    priority =[]
    cpuBurst = []
    generalList = []
    for i in newTask:
        TaskName.append(i[0])
        arrivalTime.append(i[1])
        priority.append(i[2])
        cpuBurst.append(i[3])
    generalList.append(TaskName)
    generalList.append(arrivalTime)
    generalList.append(priority)
    generalList.append(cpuBurst)

    return generalList

