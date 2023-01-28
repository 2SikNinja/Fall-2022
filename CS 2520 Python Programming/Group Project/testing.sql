create database pomonatransitsystem;
use pomonatransitsystem;

create table bus(busid int primary key, model varchar(15), year int);
select * from bus;
insert into bus values (1, 'A1', 2000);
insert into bus values (2, 'A2', 2009);
insert into bus values (3, 'A3', 2010);
insert into bus values (4, 'A4', 2020);
insert into bus values (5, 'A5', 2010);

create table driver(driverName varchar(30) primary key, PhoneNo varchar(10));
select * from driver;
insert into driver values('Abba', '7154353434');
insert into driver values('Bob', '7252426674');
insert into driver values('Carla', '7232343434');
insert into driver values('Disney', '7144553448');

create table trip(tripNumber int primary key, startlocationname varchar(50), destinationname varchar(50));
select * from trip;
insert into trip values (1, 'A', 'B');
insert into trip values (2, 'B', 'C');
insert into trip values (3, 'C', 'D');
insert into trip values (4, 'D', 'E');
insert into trip values (5, 'E', 'F');

create table stop(stopnumber int primary key, stopaddress varchar(80));
select * from stop;
insert into stop values(1, '12 Anaheim');
insert into stop values(2, '46 Beach');
insert into stop values(3, '3 Crocodile');
insert into stop values(4, '3 Dutch');
insert into stop values(5, '67 Elf');

create table tripstopinfo(tripnumber int, stopnumber int, sequencenumber int, drivingtime int, primary key(tripnumber, stopnumber), foreign key(tripnumber) references trip(tripnumber), foreign key(stopnumber) references stop(stopnumber));
select * from tripstopinfo;
insert into tripstopinfo values (1,2,1,3);
insert into tripstopinfo values (1,3,2,5);
insert into tripstopinfo values (2,3,1,2);
insert into tripstopinfo values (4,5,1,4);
insert into tripstopinfo values (3,4,1,4);

create table tripoffering(tripnumber int references trip(tripnumber), date date, scheduledstarttime varchar(30), scheduledarrivaltime varchar(30), drivername varchar(30) references driver(drivername),
 busid int references bus(busid), primary key(tripnumber, date, scheduledstarttime));
select * from tripoffering;
insert into tripoffering values (1, '2022-11-01', '11', '12', 'Abba', 1);
insert into tripoffering values (2, '2022-11-02', '7', '11', 'Disney', 2);
insert into tripoffering values (1, '2022-11-03', '6', '10', 'Abba', 3);
insert into tripoffering values (3, '2022-11-04', '3', '8', 'Abba', 4);
insert into tripoffering values (4, '2022-11-05', '11', '12', 'Disney', 1);
insert into tripoffering values (5, '2022-11-11', '14', '18', 'Abba', 5);
 
 create table actualtripstopinfo(tripnumber int, date date, scheduledstarttime varchar(30), stopnumber int references stop(stopnumber), 
 scheduledarrivaltime varchar(30) references tripoffering(scheduledarrivaltime), foreign key(tripnumber, date, scheduledstarttime) references tripoffering(tripnumber, date, scheduledstarttime), 
 actualstarttime varchar(30), actualarrivaltime varchar(30), numberofpassengerin int, numberofpassengerout int, primary key(stopnumber, tripnumber, date, scheduledstarttime));
select * from actualtripstopinfo;

