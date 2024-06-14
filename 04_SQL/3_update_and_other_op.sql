--day 6/9/23
--update
update account 
set last_login=CURRENT_TIMESTAMP;

select * from account;

--update from two table
update account 
set last_login = current_timestamp;

select * from account;

update account
set last_login=created_on
returning user_id,last_login;

select * from job;
select * from account_job;

update account_job
set hire_date=account.created_on
from account
where account_job.user_id= account.user_id;

select * from account;
select * from account_job;

--returing  the affected row
update account
set last_login=current_timestamp
returning email,created_on,last_login;

--delete
insert into job(job_name)
values('Cowboy');

select * from job;

delete from job where job_name ='Cowboy'
returning job_id,job_name;

select * from job;

--alter
create TABLE information( info_id SERIAL PRIMARY KEY,
						title varchar(500) NOT NULL,
						person varchar(50) not NULL unique
						);
select * from information;
alter table information
rename to new_info;

select * from information;
select * from new_info;

--rename column
alter table new_info
rename column person to people;
select * from new_info;

insert into new_info(title)
values('some new  title');--error

insert into new_info(title)
values('some_new_title');
--first drop that column that you can created in the previous  table
alter table new_info
alter column people 
drop not NULL;

--now insert the value in two new info
insert into new_info (title)
values('some new title');

select *  from new_info;

--drop
select * from new_info;

alter table new_info
drop column people;

select * from new_info;

alter table new_info
drop column people;

alter table new_info
drop column if exists people; -- it like the exceptional handling try catch andd throw

--3.00----------------------------------
--check
create table employees(
	emp_id SERIAL PRIMARY KEY,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	birthdate date check(birthdate >'1900-01-01'),
	hire_date date check(hire_date> birthdate),
	salary integer check(salary>0));
	
--insert into the table
insert into employees(first_name,last_name,birthdate,hire_date,salary)
values('Jose','Portilla','1899-11-03','2010-01-01','12345');--error due to check

insert into employees(first_name,last_name,birthdate,hire_date,salary)
values('Jose','Portilla','1999-11-03','2010-01-01','12345');

select * from employees;

insert into employees(first_name,last_name,birthdate,hire_date,salary)
values('Jose','Portilla','1999-11-03','2010-01-01','-12345');-- error due to the check constraint

select * from employees;

insert into employees(first_name,last_name,birthdate,hire_date,salary)
values('sammy','jain','1990-11-03','2011-01-01','100');

select * from employees;

-----------------------------
-----------------case ---------------------------
--if you want to execte this code then you must need to go in the 
-- dvdrenatl database and then execte this code
--******case***********************
select * from customer;
-- from customer id we can derive one more column

select customer_id ,
case WHEN (customer_id <=100) THEN 'Premium'
	when (customer_id between 100 and 200) then  'Plus'
	else 'Normal'
END 
from customer;

-- give the name to the derived column
select customer_id ,
case WHEN (customer_id <=100) THEN 'Premium'
	when (customer_id between 100 and 200) then  'Plus'
	else 'Normal'
END  AS label
from customer;


--***************case and expression***************
select customer_id ,
case customer_id		-->expression
	when 2 then 'Winner'
	when 5 then 'Second palace'
	else 'normal'
END AS raffel_result
from customer;

----------------------------------
select * from film;
select rental_rate from film;

select 
case rental_rate		-->expression
	when 0.99 then 1
	else 0
end 
from film;

select  
sum(case rental_rate		-->expression
	when 0.99 then 1
	else 0
end ) as number_of_bargains
from film;
--two column in one case statement
select  
sum(case rental_rate		-->expression
	when 0.99 then 1
	else 0
end ) as bargains,
sum(case rental_rate		-->expression
	when 2.99 then 1
	else 0
end ) as regular
from film;

--more column
select  
sum(case rental_rate		-->expression
	when 0.99 then 1
	else 0
end ) as bargains,
sum(case rental_rate		-->expression
	when 2.99 then 1
	else 0
end ) as regular,
sum(case rental_rate		-->expression
	when 4.99 then 1
	else 0
end ) as premium
from film;