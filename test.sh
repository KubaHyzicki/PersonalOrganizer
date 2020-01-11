#!/usr/bin/env bash

source run.sh &
sleep 3
echo & echo 'say hello' & echo
curl 'http://127.0.0.1:5000/'
sleep 1
echo & echo 'register' & echo
curl -X POST 'http://127.0.0.1:5000/register' -d 'lastName=Ciastek3&email=ciastek3@gmail.com&password=admin&firstName=Pan&permissions=client'
sleep 1
echo & echo 'test to fail' & echo
curl 'http://127.0.0.1:5000/testLogin'
sleep 1
echo & echo 'login' & echo
curl 'http://127.0.0.1:5000/login' -d 'email=jahas320@gov.pl&password=domino12345' --cookie-jar ./cookie
sleep 1
echo & echo 'login again?' & echo
curl 'http://127.0.0.1:5000/login' -d 'email=jahas320@gov.pl&password=domino12345' --cookie ./cookie
sleep 1
echo & echo 'check' & echo
curl 'http://127.0.0.1:5000/testLogin' --cookie ./cookie
sleep 1
echo & echo 'get current user events' & echo
curl 'http://127.0.0.1:5000/getUserEvents' -d 'ID_user=2' --cookie ./cookie
sleep 1
echo & echo 'print users' & echo
curl 'http://127.0.0.1:5000/getAllUsers' --cookie ./cookie
sleep 1
echo & echo 'logout' & echo
curl 'http://127.0.0.1:5000/logout' --cookie ./cookie
sleep 1
kill `ps aux | grep -i flask | grep python | sed -E 's/([a-z]+ *)([0-9]+)(.*)/\2/g'`



exit
############################---curls_to_use---############################
curl -X POST 'http://127.0.0.1:5000/' -d '&'

curl -X POST 'http://127.0.0.1:5000/addUser' -d 'lastName=Ciastek3&email=ciastek3@gmail.com&password=admin&firstName=Pan&permissions=client'

curl 'http://127.0.0.1:5000/getAllUsers'

curl 'http://127.0.0.1:5000/getUser' -d 'ID_user=12'

curl 'http://127.0.0.1:5000/removeUser' -d 'ID_user=12'

curl 'http://127.0.0.1:5000/editUser' -d 'ID_user=12&password=newPass&firstName=newName'

curl 'http://127.0.0.1:5000/getAllEvents'

curl 'http://127.0.0.1:5000/login' -d 'email=admin@admin.com&password=admin'

curl 'http://127.0.0.1:5000/login' -d 'email=benek@sad.ss&password=benek2000'

############################---decoded_passwords---############################
makarena -> makapaka 		sha256$7u1KyGus$990f1a1057a4fdfa3bd52130633ac9e8fe00d7d60e34bd9d259e49832d8d3b5b
jahas -> domino12345 		sha256$06Db5yJa$ba19c09d42bf8ac1edf18ce9a5cd14f103ef2585498a3986dee60af81b6808d6
pede -> pepepepepep00 		sha256$7HfyFQ4q$0d0bb22c1602065b4d5d17de57e0fdd44baf713e94e80c95df6c27b83547ffd2
maciejecki -> makanananana 	sha256$4YjTYu3U$cf088755b0676b2f7d3dafed4b3149a3c7feee93ed211a0770fc362bce54983e
maka -> asdasd 				sha256$gwDUIWwi$4ec9532034ce9430c1345d172ad22cbbdeefc05e410d0fdaf394ffe647e0a222
zolek -> benek2000 			sha256$Nef1nMmv$e8efb2b112b0220f713648d6ab9ef697c3400fad93c4856316b08342a5501f9b
admin -> admin 				sha256$yKSR8dsY$73a5cd8218e8b6cc9a84bba63d4258799ec6946bc5c748922e60700b27513839