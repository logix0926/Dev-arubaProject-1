import pexpect
import datetime
import sys
#from timeout_decorator import timeout
import timeout
import re
import csv
import json

def write_error_log(st):
    dt_now = datetime.datetime.now()
    try:
        f = open('logfile.log','a')
        f.writelines("{} >> :  {}\n".format(dt_now, st))
        f.close()
    except:
        print("write_log error")

@timeout.timeout(duration=45)
def conect_ssh(i):
    try:
        ssh = pexpect.spawn("ssh admin@10.0.0.5{}".format(str(i)), timeout=10, encoding='utf-8')
        ssh.expect("admin@10.0.0.5{}'s password:".format(str(i)))
    except:
        #Settings for verification environment start
        try:
            ssh = pexpect.spawn("ssh admin@10.0.0.5{} -p 200{}".format(str(i),str(i)), timeout=10, encoding='utf-8')
            ssh.expect("admin@10.0.0.5{}'s password:".format(str(i)))
        except:
            write_error_log("AP{} Segment error or Dfferent account name or IP address".format(str(i)))
            return 0,0
        else:
            return try_ssh_login(ssh,i)
        #Settings for verification environmentn end
    else:
        return try_ssh_login(ssh,i)

def try_ssh_login(ssh,i):
    try:
        ssh.sendline("Secure1!")
        ssh.expect("AP{}#".format(str(i)))
    except:
        #Settings for verification environment start
        try:
            ssh.expect("$")
        except:
            write_error_log("AP{} Failed password login".format(str(i)))
            return 0,0
        else:
            try:
                ssh.sendline("show ap association")
                ssh.expect("$")
                association = ssh.before
                return i,association
            except:
                write_error_log("AP{} Failed to execute command on aruba".format(str(i)))
                return 0,0
    else:
        try:
            ssh.sendline("show ap association")
            ssh.expect("AP{}#".format(str(i)))
            association = ssh.before
            return i,association
        except:
            write_error_log("AP{} Failed to execute command on aruba".format(str(i)))
            return 0,0

def create_json(connect_list):
    try:
        csv_file = open("./test.csv","r",encoding="ms932")
    except:
        write_error_log("Cannot Open CSV Error")
    try:
        f=csv.reader(csv_file, delimiter=",",doublequote=True,lineterminator="\r\n",quotechar='"',skipinitialspace=True)
    except:
        write_error_log("Cannot Read CSV Error")
    else:
        json_list = {}
    try:
        j = 0
        for row in f:
            if (row != []):
                l=row[0].split()
                if 'AP' in l[0]:
                    json_list[l[2]] = l[0]
            j+=1
    except:
        write_error_log("Cannot Create List Error")
    try:
        json_res=json.dumps(json_list, indent=4)
    except:
        write_error_log("Cannot Convert List to Json Error")
    print(json_res)

try:
    connect_list=[]
    csv_string=""
    for i in range(1,10):
        a,b = conect_ssh(i)
        if (a != 0)and(b != 0):
            connect_list.append(a)
            csv_string+=b
    csv_list = csv_string.splitlines()
    with open("./test.csv","w",newline="") as f:
        #writer= csv.writer(f)
        #writer.writer(csv_list)
        for index in range(len(csv_list)):
            f.write(csv_list[index])
            f.write("\n")
    create_json(connect_list)
except timeout.TimeoutException:
    write_error_log("timeout(ssh)")

