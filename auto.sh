#! /bin/sh
echo "Reading Bash File"
sleep 3
if ! ps ax | grep -q "[s]endfile.py"; 
then
    echo "Send File Script Started Successfully!"
    python sendfile.py
fi
