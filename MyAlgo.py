import csv
import sys
from Call import Call
from building import building


def readCsv(fileCsv):
    rows = []
    listCall = []
    with open(fileCsv, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    for r in rows:
        c = Call(r)
        listCall.append(c)
    return listCall


def fastElv(elevators):
    m = -1
    for j in elevators:
        if m < j.speed:
            res = j
            m = j.speed
    return res


def TimeAlg(Elv):
    TotalTime = 0
    m = sys.maxint
    for z in Elv:
        for w in z.CallsElv:
            TotalTime += z.waitingTime(w.src, w.disT)
        if m > TotalTime:
            m = TotalTime
            e = z
    TotalTime = 0
    return e


def csvLoad(CallList, outputFile):
    with open(outputFile, 'w') as File:
        w = csv.writer(File)
        w.writerows(CallList)


def Done(elv):
    for e in elv.CallsElv:
        if elv.pos == e.desT:
            elv.CallsElv.remove(e)

    return elv.CallsElv


def allocate(JsonFile, csvFile, outputFile):
    ActiveElv = []
    NonActiveElv = []
    loadBuilding = building(JsonFile)
    listCalls = readCsv(csvFile)
    NonActiveElv = loadBuilding.elevators
    for i in listCalls:
        for el in ActiveElv:
            if len(Done(el)) == 0:
                NonActiveElv.append(el)

        if len(NonActiveElv) > 0:
            f = fastElv(NonActiveElv)
            i.allocTo = f.id
            f.CallsElv.append(i)
            ActiveElv.append(f)
            NonActiveElv.remove(f)
        else:
            El = TimeAlg(ActiveElv)
            i.allocTo = El.id
            El.CallsElv.append(i)
    ##csvLoad(listCalls, outputFile)


if __name__ == '__main__':
    allocate("C:\Users\User\Desktop\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B1.json",
             "C:\Users\User\Desktop\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_Calls\Calls_a.csv",
             "C:\Users\User\Desktop\OOP_2021-main\Assignments\Ex1\data\Ex1_input\Ex1_output\output\B1_a.csv"
             )
