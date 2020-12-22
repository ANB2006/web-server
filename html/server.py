from datetime import time, datetime as mathtime, date
from time import sleep
import datetime

def timeIs():
    theTime = datetime.datetime.now().strftime('%H%M')
    theTimePure = time(int(theTime[:2]), int(theTime[2:]))
    return theTimePure

def checkTimes():

    programedTime1 = open('/root/web-server/readTimesList.txt', 'r')
    programedTime = programedTime1.read()
    times = programedTime.split(' ')
    programedTime1.close()
    return times

def checkTimesFile():

    programedTime1 = open('/root/web-server/FileTimes.txt', 'r')
    programedTime = programedTime1.read()
    times = programedTime.split(' ')
    programedTime1.close()
    return times

def checkData():
    places1 = open('/root/web-server/directions.txt', 'r')
    places = places1.read()
    placesFinal = places.split('\n')
    places1.close()
    return placesFinal

print(checkData())
nextOrder = 0
for timeSTR in checkTimes():
    if timeSTR == 'None':
        exit()
    else:
        print(time)
        print(type(time))
        timePure = time(int(timeSTR[:2]), int(timeSTR[2:]))
        duration = mathtime.combine(date.min, timePure) - mathtime.combine(date.min, timeIs())
        print('Waiting')
        sleep(duration.total_seconds())
        print('Start')
        theFile = open('readDirection.txt', 'w')
        theFile.write(checkData()[nextOrder])
        theFile.close()

        theTimeFile = open('readTimes.txt', 'w')
        theTimeFile.write(checkTimesFile()[nextOrder])
        theTimeFile.close()
        print('Done')

        nextOrder = nextOrder + 1
        
