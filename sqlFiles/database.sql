DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Alarm;
DROP TABLE IF EXISTS AlarmType;
DROP TABLE IF EXISTS EventsCategories;


CREATE TABLE User(
  ID_user INT AUTO_INCREMENT PRIMARY KEY,
  lastName VARCHAR(255),
  email VARCHAR(255),
  password VARCHAR(255),
  firstName VARCHAR(255),
  permissions VARCHAR(255)
);

CREATE TABLE Event(
  ID_event INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  status VARCHAR(255),
  description VARCHAR(255),
  participants VARCHAR(255),
  creationDate date,
  date date,
  repeatable VARCHAR(255),
  weitht INT,
  ID_user INT,
  ID_alarm INT
);

CREATE TABLE Category(
  ID_category INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  alarm_id INT,
  description VARCHAR(255),
  weight INT,
  colour INT
);

CREATE TABLE EventsCategories(
  ID_EventCategory INT AUTO_INCREMENT PRIMARY KEY,
  ID_category INT,
  ID_event INT
);

CREATE TABLE Alarm(
  ID_alarm INT AUTO_INCREMENT PRIMARY KEY,
  volume_level INT,
  active BOOLEAN,
  whenAlarm date,
  alarmMethod VARCHAR(255),
  ID_event INT
);

CREATE TABLE AlarmType(
  arlarmMetchod VARCHAR(255)
);










DROP TRIGGER IF EXISTS CASCADE_DELETE_EVENT;

DELIMITER $$
 
CREATE TRIGGER CASCADE_DELETE_EVENT
before delete
ON Event
FOR each row
BEGIN
  DELETE FROM EventsCategories
  WHERE ID_event = OLD.ID_event;

  DELETE FROM Alarm -- trzeba dodac kolumne ID_event w tabeli alarm
  WHERE ID_event = OLD.ID_event;
END$$    
 
DELIMITER ;

DROP TRIGGER IF EXISTS delete_AlarmType;

DELIMITER $$
 
CREATE TRIGGER delete_AlarmType
before delete
ON AlarmType FOR each row
BEGIN
  UPDATE Alarm
  SET alarmMethod = 'default'
  WHERE alarmMethod = OLD.arlarmMetchod;
END$$    
 
DELIMITER ;

DROP TRIGGER IF EXISTS update_AlarmType;

DELIMITER $$
 
CREATE TRIGGER update_AlarmType
before update
ON AlarmType FOR each row
BEGIN
  UPDATE Alarm
  SET alarmMethod = NEW.arlarmMetchod
  WHERE alarmMethod = OLD.arlarmMetchod;
END$$    
 
DELIMITER ;


DROP TRIGGER IF EXISTS delete_Category;

DELIMITER $$
 
CREATE TRIGGER delete_Category
before delete
ON Category FOR each row
BEGIN
  DELETE FROM EventsCategories
  WHERE ID_category = OLD.ID_category;
END$$    
 
DELIMITER ;

DROP TRIGGER IF EXIST CASCADE_DELETE_USER

DELIMITER $$
 
CREATE TRIGGER CASCADE_DELETE_USER
before delete
ON User FOR each row
BEGIN
  DELETE FROM Event
  WHERE ID_user = OLD.ID_user;
END$$    
 
DELIMITER ;