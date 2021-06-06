#! /bin/sh
echo "Reading Bash File"
sleep 3
if pgrep -f "python sendfile.py" &>/dev/null; 
then
    echo "Send File Script Started Successfully!"
    exit
else
    python sendfile.py
fi