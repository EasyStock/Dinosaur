select * from allDailyData;

select count(*) from allDailyData;

select * from allDailyData where date = '2020-04-07';

select distinct date from allDailyData;

select distinct sid from allDailyData;

select * from allDailyData where sid = '600519.SH' and date>='2020-12-01';


CREATE TABLE IF NOT EXISTS AAA (
    fileName  TEXT     NOT NULL,
    PRIMARY KEY(fileName)
);