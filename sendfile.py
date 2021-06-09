import os
import time

myPath = "/root/mydisk/chia-blockchain/dest" #enter your destination path here
myBucket = "myproject1" #enter your gcloud bucket name here
network = "wasabi" #enter your rclone network name here

def checklist():
    mylist = os.listdir(myPath)
    newlist = []
    for i in mylist:
        if i.endswith(".plot"):
            newlist.append(i)
    return(newlist)


def send():
    now = time.ctime()
    mylist = os.listdir(myPath)
    valid = []
    for file in mylist:
        if file.endswith(".plot"):
            valid.append(file)
    os.system(
        "echo Files to send = "
    )
    print(valid)
    time.sleep(2)
    os.system(
        "rclone move "+myPath+"/plot-* "+network+":"+myBucket+" -P"
    )
    os.system(
        "echo *** Sending file operation started *** "+now
    )


while True:
    now = time.ctime()
    if checklist():
        send()
        while True:
            if checklist():
                os.system(
                    "echo File sending operation is still in progress..."
                )
                time.sleep(60)
            else:
                os.system(
                    "echo *** Sending file operation finished *** "+now
                )
                time.sleep(10)
                break
    else:
        os.system(
            "echo There is no finished jobs!"
        )
        time.sleep(120)
