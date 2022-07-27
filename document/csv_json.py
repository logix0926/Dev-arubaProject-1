import json 
import pexpect
import time
import subprocess
import csv
import datetime

now = datetime.datetime.now()
log = open('logfile.log','a')

def create_json():
    try:
        csv_file = open("./test.csv","r",encoding="ms932")
    except:
        log.write(str(now)+":Cannot Open CSV Error\n")
    try:
        f = csv.reader(csv_file, delimiter=",",doublequote=True,lineterminator="\r\n",quotechar='"', skipinitialspace=True)
    except:
        log.write(str(now)+":Cannot Read CSV Error\n")
    else:
        i=0
        json_list = {}
    try:
        for row in f:
            if i>15:
                l=row[0].split()
                if 'Num' in l[0]:
                    break
                json_list[l[2]] = l[0]
            i+=1
    except:
        log.write(str(now)+":Cannot Create List Error\n")
    try:
        json_res = json.dumps(json_list, indent=4)
    except:
        log.write(str(now)+":Cannot Convert List to Json Error\n")
    print(json_res)

subprocess.run("python3 test.py>test.csv",shell=True)
create_json()
