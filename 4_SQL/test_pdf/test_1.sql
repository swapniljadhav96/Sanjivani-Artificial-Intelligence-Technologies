--1. Write a SQL statement to create a table named jobs including 
--columns job_id, job_title, min_salary, max_salary
--and check whether the max_salary amount exceeding the upper limit 25000.
drop table jobs;
create table jobs(
				  job_id serial not null,
				  job_title varchar(300) not null,
				  min_salary decimal(10,0) not null,
				  max_salary decimal(10,0) not null
					);
insert into jobs values(1,'a',23000,25345);
insert into jobs values(2,'b',2300,35345);
insert into jobs values(3,'w',230,29345);
insert into jobs values(4,'y',200,20345);
insert into jobs values(5,'r',2000,25045);
insert into jobs values(6,'s',3000,2545);

select * from jobs;

select job_id , job_title from jobs
where max_salary>25000;

--Q 2Write a SQL statement to change the email column of the employees 
--table with 'not available' for all employees.
truncate email_id;

alter table jobs add email_id varchar(30);
select * from jobs;

update jobs
set email_id='not available'
where job_id between 1 and 6;

select * from jobs;

--Q3. Write a SQL statement to rename the table jobs to jobs_new.
drop table jobs_new;
alter table jobs rename to jobs_new;

--Q.4 Write a SQL statement to add a column dept_id to the table locations.
alter table jobs_new add dept_id serial not null; 

select * from jobs_new;

--Q.5 Write a SQL statement to insert a record with
--your own value into the table jobs_new against each column.

insert into jobs_new values(7,'p',300,25245,'sytar@gmail.com',7);
insert into jobs_new values(8,'o',30,2245,'sytar@gmail.com',8);

select * from jobs_new;
--Q.6 Write a query to display the names (job_id,dept_id) .
select job_id,dept_id from jobs_new;

--7 Write a query to get the maximum total salaries payable to employees.
select sum(max_salary) from jobs_new;

--8. Write a query to get the average salary and number of employees
--are working
select count(job_id), avg(max_salary) from jobs_new;


--Q.9 Create a table manager_details comprises of 
--manager_id,manager_name ,dept_id and 
--Write a query to make a join with two tables jobs_new and manager_details
drop table mana_deta;
create table mana_deta
	(
	manager_id serial not null,
	manager_name  varchar(300) not null,
	dept_id serial not null 
	);
insert into mana_deta values(1,'q',1);
insert into mana_deta values(2,'t',2);
insert into mana_deta values(6,'d',5);
insert into mana_deta values(7,'r',7);
insert into mana_deta values(8,'f',8);

select * from mana_deta;

select job_id,job_title,min_salary,max_salary,manager_id,manager_name 
from jobs_new inner join mana_deta on
jobs_new.dept_id=mana_deta.dept_id;

--10 Write a SQL subquery to find the emp_id  of all
--employees  from jobs_new table who works in the IT department.

