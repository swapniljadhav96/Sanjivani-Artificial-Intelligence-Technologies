-- day_7_9_23
--3.00
-- write the sql statememnt to create a simple countries
--inculiding column country_id ,country_name,region_id
--import andexport
create table countries(
country_id varchar(20),
country_name varchar(45),
region_id decimal(10,0));

select * from countries;

--write a sql statement to create the structure of the table dup_countries
--similar to the countries
create table dup_countries as (
select * from countries);

select * from dup_countries;


-- write the a sql statement to create a table countries ,set the constraint null
create table if not exists  countries(
country_id varchar(20) not null,
country_name varchar(45) not null,
region_id decimal(10,0) not null);
select * from countries;

-- write the sql statement to create a table name job including the columns
--job_id ,job_title ,min salary,max_salary and
--check whether the max_salary amount execeading the upper limit  25000;
create table job(
job_id  varchar(20) not null,
job_title varchar(29) not null,
min_salary int not null,
max_salary int check(max_salary<=25000));

insert into job values(1,'a',123,212453);

insert into job values(2,'b',123,2453);--error

select * from job;

--write the sql statemnet  to created a table named countries including coumns 
--country_id, country_name and region_id make sure that the no countries
--accept betwwen italy ,india and chine will be enter in the table
create table if not exists  countries(
country_id varchar(20) not null ,
country_name varchar(45) check (country_name in('italy','india','china')),
region_id decimal(10,0) not null);
select * from countries;

--write the sql statemnet  to created a table named countries including coumns 
--country_id, country_name and region_id and make sure that no duplicates data against
-- column country_id
create table if not exists  countries(
country_id serial primary key,
country_name varchar(45),
region_id decimal(10,0) not null);

--sira cha
create table if not exists  countries(
country_id serial primary key,
country_name varchar(45),
region_id decimal(10,0) not null
unique(country_id))
;

--  write the sql statement to create a table name job including the columns
--job_id ,job_title ,min salary,max_salary and make sure that default value for job title
--is blank and min_salary is 8000 and max_salary is null will be  entre automatically
-- at the time of insertion if no values 
-- assingend to soecific column.
drop table job;
create table  if not exists job(
job_id  varchar(20) not null,
job_title varchar(29)  default '',
min_salary int  default 8000,
max_salary int default 0);

insert into job values (3,'k');
select * from job;



-- -write the sql statemnet  to created a table named countries including coumns 
--country_id, country_name and region_id ansd make sure that country_id column will be may filed
--which will not contain any duplicate date at the time if insertion
create table if not exists  countries(
country_id serial primary key,
country_name varchar(45),
region_id decimal(10,0) not null);

select * from countries;

--sircah
create table if not exists  countries(
country_id varchar(2) not null unique primary key,
country_name varchar(45),
region_id decimal(10,0) not null);

-- -write the sql statemnet  to created a table named countries including coumns 
--country_id, country_name and region_id and make sure that country_id
-- will be unique and store an auto_incremnetal value
create table if not exists  countries(
country_id SERIAL not null unique primary key,
country_name varchar(45),
region_id decimal(10,0) not null);


--write the sql statemnet  to created a table named countries including coumns 
--country_id, country_name and region_id and make sure that country_id and region_name unique
create table if not exists  countries(
country_id SERIAL not null unique default '' ,
country_name varchar(45),
region_id decimal(10,0) not null,
primary key(country_id,region_id));

---------------
--write the sql to create a table job_history
--including  columns employee_id, start_date ,end_date job_id and deparment _id and make sure
--that the employee_id column
create table job_history(
employee_id decimal(6,0) not null Primary key,
start_date date not null,
end_date date not null,
job_id varchar(10) not null,
department_id decimal (4,0) default NULL,
foreign key(job_id) references job(job_id));

--assigment
--Write a query to find the addresses 
--(location_id, street_address, city, state_province, country_name) 
--of all the departments.
drop table location ;
create table location(
location_id serial not null ,
street_address varchar(300) not null,
postal_code int not null,
city varchar(200) not null,
start_province varchar(200),
country_id varchar(200) not null);

create table if not exists  countries(
country_id varchar(200) not null,
country_name varchar(45),
region_id decimal(10,0) not null);


select location_id, street_address, city, 
start_province, country_name 
from location inner join countries
on location.country_id= countries.country_id;

--
--Write a query to make a join with employees and departments table to 
--find the name of the employee, including first_name and last name, 
--department ID and name of departments
create table employee(
employee_id serial not null ,
first_name varchar(300) not null,
last_name varchar(200) not null,
email varchar(200) not null unique,
phone_number varchar(20) not null,
hire_date date ,
job_id varchar(200) not null,
salary decimal(6,0) not null);

drop table departments;
create table departments
(
department_id serial not null,
departement_name varchar(120) not null,
manger_id serial not null,
location_id varchar(2000) not null);

select first_name,last_name ,department_id ,
departement_name from employee inner join departments
on employee.employee_id=departments.manger_id;
