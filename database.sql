DROP TABLE User;
DROP TABLE Event;
DROP TABLE Category;
DROP TABLE Alarm;
DROP TABLE AlarmType;
DROP TABLE EventsCategories;


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
  ID_categ INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  alarm_id INT,
  description VARCHAR(255)
);

CREATE TABLE EventsCategories(
  ID_EventCateg INT AUTO_INCREMENT PRIMARY KEY,
  ID_categ INT,
  ID_event INT
);

CREATE TABLE Alarm(
  ID_alarm INT AUTO_INCREMENT PRIMARY KEY,
  volume_level INT,
  active BOOLEAN,
  whenAlarm date,
  alarmMethod VARCHAR(255)
);

CREATE TABLE AlarmType(
  arlarmMetchod VARCHAR(255)
);

