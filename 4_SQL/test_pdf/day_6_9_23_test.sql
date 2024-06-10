--day 6-9-23
--test
create table student(
	student_id int primary key,
	first_name varchar(500) not NULL,
	last_name varchar(500) not NULL,
	homeroom_number int not null unique,
	phone varchar(20) not NULL unique,
	email varchar(200) not null unique,
	graduation_year date);

create table teacher(
	teacher_id int primary key,
	homeroom_number int not null unique,
	department varchar(200) not null,
	email varchar(200) not null unique,
	phone varchar(20) not null unique);


insert into student values(1,'Rahul','Galande',
						  5, 7775551234,'Rahul.galande@gmail.com',
						  '2023-02-01');
select * from student;


drop table teacher;

create table teacher(
	teacher_id int primary key,
	first_name varchar(200) not null,
	last_name varchar(200) not null,
	homeroom_number int not null unique,
	department varchar(200) not null,
	email varchar(200) not null unique,
	phone varchar(20) not null unique);
	
insert into teacher values(1,'Chandrashekhar','Gogte',
						  5,'Biology','Chandrashekhar.gogte@gamil.com ',7775554321);	
select * from teacher;
--perform all the opertion on the above two table
--update 
update TABLE student
set first_name ='ram';