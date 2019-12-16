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
	WHERE ID_categ = OLD.ID_categ;
END$$    
 
DELIMITER ;
