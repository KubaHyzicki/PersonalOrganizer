#!/usr/bin/env bash

source run.sh &
sleep 3
echo & echo 'login' & echo
curl 'http://127.0.0.1:5000/login' -d 'email=jahas320@gov.pl&password=domino12345' --cookie-jar ./cookie
sleep 1
echo & echo 'get current user events' & echo
curl 'http://127.0.0.1:5000/getUserEvents' --cookie ./cookie
sleep 1
echo & echo 'add' & echo
curl 'http://127.0.0.1:5000/addEvent' -d 'name=test&status=niewykonane&description=no ciastka no&participants=&creationDate=18-05-2019&repeatable=&date=18-06-2019' --cookie ./cookie
sleep 1
echo & echo 'get current user events' & echo
curl 'http://127.0.0.1:5000/getUserEvents' --cookie ./cookie
sleep 1

sleep 1
kill `ps aux | grep -i flask | grep python | sed -E 's/([a-z]+ *)([0-9]+)(.*)/\2/g'`
echo
exit