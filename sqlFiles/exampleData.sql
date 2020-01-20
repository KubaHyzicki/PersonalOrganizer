Insert into  Alarm (volume_level,active,whenAlarm,alarmMethod,ID_event) values (null,null,null,'zmiana',null);
Insert into  Alarm (volume_level,active,whenAlarm,alarmMethod,ID_event) values (null,null,null,'default',null);
Insert into  Alarm (volume_level,active,whenAlarm,alarmMethod,ID_event) values ('500','1',null,'default','2');


Insert into  AlarmType (arlarmMetchod) values ('default');
Insert into  AlarmType (arlarmMetchod) values ('metoda alarmu do usuniecia');
Insert into  AlarmType (arlarmMetchod) values ('zmiana');



Insert into  Category (name,description,alarm_id) values ('birthday','birthday',3);
Insert into  Category (name,description,alarm_id) values ('meeting','biznes meeting',3);
Insert into  Category (name,description,alarm_id) values ('imprezy','imprezy towarzystkie',1);



Insert into  Event (name,status,description,participants,creationDate,date,repeatable,ID_user) values ('urodziny babci','niewykonane',null,null,STR_TO_date('18,05,2019','%d,%m,%Y'),STR_TO_date('18,06,2019','%d,%m,%Y'),null,'2');
Insert into  Event (name,status,description,participants,creationDate,date,repeatable,ID_user) values ('urodziny dziadka','niewykonane',null,null,STR_TO_date('18,05,2019','%d,%m,%Y'),STR_TO_date('18,06,2019','%d,%m,%Y'),null,'3');

Insert into  EventsCategories (ID_event,id_category) values ('2','2');

Insert into  User (lastName,email,password,firstName,permissions) values ('makarena','makarenacosablena@kakaka.pl','sha256$7u1KyGus$990f1a1057a4fdfa3bd52130633ac9e8fe00d7d60e34bd9d259e49832d8d3b5b','cosablena',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('jahas','jahas320@gov.pl','sha256$06Db5yJa$ba19c09d42bf8ac1edf18ce9a5cd14f103ef2585498a3986dee60af81b6808d6','domino',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('pede','dadadal@gov.pl','sha256$7HfyFQ4q$0d0bb22c1602065b4d5d17de57e0fdd44baf713e94e80c95df6c27b83547ffd2','kup se krede',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('maciejecki','dalniel@gov.pl','sha256$4YjTYu3U$cf088755b0676b2f7d3dafed4b3149a3c7feee93ed211a0770fc362bce54983e','daniel',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('maka','mak@gov.pl','sha256$gwDUIWwi$4ec9532034ce9430c1345d172ad22cbbdeefc05e410d0fdaf394ffe647e0a222','paka',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('zolek','benek@sad.ss','sha256$Nef1nMmv$e8efb2b112b0220f713648d6ab9ef697c3400fad93c4856316b08342a5501f9b','benek',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('dmin','admin@admin.com','sha256$yKSR8dsY$73a5cd8218e8b6cc9a84bba63d4258799ec6946bc5c748922e60700b27513839','A','admin');