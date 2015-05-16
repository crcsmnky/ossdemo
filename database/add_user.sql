CREATE DATABASE metrics;

CREATE USER 'mysql'@'localhost';
GRANT ALL PRIVILEGES ON *.* to 'mysql'@'localhost' WITH GRANT OPTION;

CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpass';
GRANT ALL PRIVILEGES ON *.* to 'testuser'@'%' WITH GRANT OPTION;
