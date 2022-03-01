def writeString(string):
    with open("output.txt" ,"w") as file:
        file.write(str(string))
        file.close()

def appendString(string):
    with open("output.txt", "a") as file:
        file.write(str(string))
        file.close()