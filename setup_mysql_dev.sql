-- Script to configure MySQL server for development environment
-- Establish a development database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Set up a development user hbnb_dev with full access to hbnb_dev_db
-- Assign password hbnb_dev_pwd to the user if not already present
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Provide SELECT privilege to hbnb_dev on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Allocate full privileges to hbnb_dev on the hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
