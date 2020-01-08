#!/usr/bin/env bash

source run.sh &
sleep 2
echo & echo say hello & echo
curl 'http://127.0.0.1:5000/'
sleep 2
echo & echo test to fail & echo
curl 'http://127.0.0.1:5000/testLogin'
sleep 2
echo & echo login & echo
curl 'http://127.0.0.1:5000/login' -d 'email=benek@sad.ss&password=benek2000' --cookie-jar ./cookie
sleep 2
echo & echo check & echo
curl 'http://127.0.0.1:5000/testLogin' --cookie ./cookie
sleep 2
echo & echo check & echo
curl 'http://127.0.0.1:5000/getAllUsers'
sleep 2
kill `ps aux | grep -i flask | grep python | sed -E 's/([a-z]+ *)([0-9]+)(.*)/\2/g'`


##curls to use:
#curl -X POST 'http://127.0.0.1:5000/' -d '&'

#curl -X POST 'http://127.0.0.1:5000/addUser' -d "{'lastName':'Ciastek','email':'ciastek@gmail.com','password':'admin','firstName':'Pan','permissions':'client'}"

#curl 'http://127.0.0.1:5000/getAllUsers'

#curl 'http://127.0.0.1:5000/getUser' -d "{'ID_user':'12'}"

#curl 'http://127.0.0.1:5000/removeUser' -d "{'ID_user':'12'}"

#curl 'http://127.0.0.1:5000/editUser' -d {ID_user:12,password:newPass,firstName:newName}
#curl 'http://127.0.0.1:5000/getAllEvents'

#curl 'http://127.0.0.1:5000/login' -d 'email=admin@admin.com&password=admin'

#curl 'http://127.0.0.1:5000/login' -d 'email=benek@sad.ss&password=benek2000'