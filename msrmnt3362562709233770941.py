def readFile(file):
    temps = []
    try:
        with open(file, mode="r") as fileobj:
            for tempLine in fileobj:
                if tempLine[0].isalpha():
                    continue
                columns = tempLine.rstrip().split(";")
                time = columns[0].split(':')
                # hours * 3600 + mins * 60 + seconds
                seconds = int(time[0])*3600 + int(time[1])*60 + int(time[2])
                columns[0] = seconds
                temps.append(columns)
        return temps
    except IOError:
        print(f"Error in reading the file!")
        return None

def writeFile(temps, output):
    try:
        with open(output, mode="w") as fileobj:
            for item in range(len(temps)-1):

                y = lambda x: x.replace(',','.')

                changeSec = float(temps[item+1][0])-float(temps[item][0])

                changeTemp1 = (float(y(temps[item+1][1]))- float(y(temps[item][1])))/changeSec

                changeTemp2 = (float(y(temps[item+1][2]))-float(y(temps[item][2])))/changeSec

                changeTemp3 = (float(y(temps[item+1][3]))-float(y(temps[item][3])))/changeSec
                changeSecStr = format(changeSec,'.1f')
                changeTemp1Str=format(changeTemp1,'.1f')
                changeTemp2Str=format(changeTemp2,'.1f')
                changeTemp3Str=format(changeTemp3,'.1f')
                fileobj.write(changeSecStr+';'+changeTemp1Str+';'+changeTemp2Str+';'+changeTemp3Str+'\n')

            print(f"Information saved successfully.")
    except IOError:
        return None

def main():
    file = input("Enter the name of the file to be read: ")
    temps = readFile(file)
    if temps is None:
        return
    else:
        output = input("Enter the name of the file to be written: ")
        writeFile(temps, output)
main()
