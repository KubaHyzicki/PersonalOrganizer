CREATE USER 'application_user'@'localhost' IDENTIFIED BY 'password_user';

GRANT delete, select, insert, update ON * . * TO 'application_user'@'localhost';



CREATE USER 'application_admin'@'localhost' IDENTIFIED BY 'password_admin';

GRANT ALL PRIVILEGES ON * . * TO 'application_admin'@'localhost';