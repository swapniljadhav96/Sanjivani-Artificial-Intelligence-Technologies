--opertion onn the customer table
select * from customer;

select * from  customer
order by first_name;

select * from customer
order by first_name ASC;

select * from customer
order by First_name DESC;

select * from customer 
order by store_id;

select store_id ,first_name,last_name from customer
order by store_id,first_name;


select store_id, first_name,last_name from customer
order by store_id ASC ,first_name DESC;

select * from payment 
order by payment_date DESC 
LIMIT 5;
--challenge1

select * from payment 
where amount!=0.00
order by  payment_date DESC
limit 5;
--challenge2
select customer_id from customer
order by customer_id ASC
limit 10;
--challeng3
select title,length from film
order by length ASC
limit 5;

select count(title) from film
where length<='50';

--between
select * from payment
limit 2;


select * from payment
where amount between 8 and 9;


select count(*) from payment
where amount between 8 and 9;

select count(*) from payment
where amount NOT between 8 and 9;

select * from payment
where payment_date between '2007-01-01' and '2007-02-15';


select distinct(amount) from payment;

select distinct(amount) from payment
order by amount;

select * from payment
where amount IN (0.09,1.99,1.98);

select count(*) from payment
where amount IN (0.09,1.98,1.99);

select count(*) from payment
where amount NOT IN (0.09,1.98,1.99);

select * from customer
where first_name IN ('John','Jake','Julie');

select * from customer
where first_name NOT IN ('John','Jake','Julie');

--like
select * from customer
where first_name like'J%';

select * from customer
where first_name like'j%';


select count(*) from customer
where first_name like 'J%';

select * from customer
where first_name like 'J%' And last_name like 'S%';

select * from customer 
where first_name like 'j%';

select * from customer
where first_name ilike 'j%' AND last_name ilike 'j%';

select * from customer
where first_name ilike 'j%'AND last_name ilike 's%';

select * from customer 
where first_name like '%er%';

select * from customer
where first_name like '%her%';

select * from customer
where first_name like '_her%';

select * from customer
where first_name like 'A%';

select * from customer
where first_name like'A%'
order by lats_name;

select * from customer
where first_name like 'A%' AND last_name  NOT like 'B%'
order by last_name;


select count(amount) from payment
where amount>5;

select count(*) from actor
where first_name like 'P%';
