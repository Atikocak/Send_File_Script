import os
import time

myPath = "/root/mydisk/chia-blockchain/dest"


def checklist():
    mylist = os.listdir(myPath)
    newlist = []
    for i in mylist:
        if i.endswith(".plot"):
            newlist.append(i)
    return(newlist)


def send():
    zaman = time.ctime()
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
        "rclone move /root/mydisk/chia-blockchain/dest/plot-* myremote:ati_project1 -P"
    )
    os.system(
        "echo *** Sending file operation started *** "+zaman
    )


while True:
    zaman = time.ctime()
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
                    "echo *** Sending file operation finished *** "+zaman
                )
                time.sleep(10)
                break
    else:
        os.system(
            "echo There is no finished jobs!"
        )
        time.sleep(120)
