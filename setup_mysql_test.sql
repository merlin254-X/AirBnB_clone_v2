-- Script to configure MySQL server for development environment
-- Establish a development database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Set up a development user hbnb_test with full access to hbnb_test_db
-- Assign password hbnb_test_pwd to the user if not already present
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Provide SELECT privilege to hbnb_test on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Allocate full privileges to hbnb_test on the hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

