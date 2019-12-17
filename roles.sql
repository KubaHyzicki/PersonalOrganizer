CREATE USER 'application_user'@'localhost' IDENTIFIED BY 'password';

GRANT delete, select, insert, update ON * . * TO 'application_user'@'localhost';



CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';