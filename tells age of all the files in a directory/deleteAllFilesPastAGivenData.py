import os
import sys
import datetime
reqdPath=input("enter file path")
age=3
if not os.path.exists(reqdPath) :
    print("enter a valid path")
    sys.exit(1)
if os.path.isfile(reqdPath) :
    print("please enter a directory path not a file path")
    sys.exit(2)
today=datetime.datetime.now()
for eachfile in os.listdir(reqdPath) :
    eachfilePath= os.path.join(reqdPath,eachfile)
    if os.path.isfile(eachfilePath):
        file_create_date=datetime.datetime.fromtimestamp(os.path.getctime(eachfilePath))
        differenceDates=(today-file_create_date).days
        if differenceDates>age :
            print(eachfilePath,differenceDates)

