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

Insert into  EventsCategories (ID_event,ID_categ) values ('2','2');

Insert into  User (lastName,email,password,firstName,permissions) values ('makarena','makarenacosablena@kakaka.pl','makapaka','cosablena',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('jahas','jahas320@gov.pl','domino12345','domino',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('pede','dadadal@gov.pl','pepepepepep00','kup se krede',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('maciejecki','dalniel@gov.pl','makanananana','daniel',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('maka','mak@gov.pl','asdasd','paka',null);
Insert into  User (lastName,email,password,firstName,permissions) values ('zolek','benek@sad.ss','benek2000','benek',null);
