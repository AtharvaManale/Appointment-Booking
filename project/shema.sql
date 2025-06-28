CREATE DATABASE IF NOT EXISTS smartvolt;
USE smartvolt;

CREATE TABLE login (
    Email VARCHAR(100),
    Username VARCHAR(100),
    Password VARCHAR(100)
);

CREATE TABLE appointments (
    username VARCHAR(100),
    station_id VARCHAR(100),
    date_ DATE,
    time_ VARCHAR(20)
);

CREATE TABLE alogin (
    Username VARCHAR(100),
    Password VARCHAR(100)
);

INSERT INTO alogin(Username, Password)
VALUES('Atharva', '1234')