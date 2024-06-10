-- day 31/8/23
--AS
select sum(amount) as rate_transction  from payment;

select count(amount) as num_transaction from payment;

select customer_id, sum(amount)  from payment
group by customer_id;

select customer_id, sum(amount) as total_spent  from payment
group by customer_id;

select customer_id, sum(amount)  from payment
group by customer_id
having sum(amount)>100

select customer_id, sum(amount) AS total_spent  from payment
group by customer_id
having sum(amount)>100;

--refereing the alis name in the having clause
select customer_id, sum(amount) AS total_spent  from payment
group by customer_id
having total_spent>100;

select customer_id ,amount as new_name
from payment
where amount>2;

----refereing the alis name in the having clause
select customer_id ,amount as new_name
from payment
where new_name>2;

-------------------join---------------------------------------
--1.inner join
--select all the column from the  both the table 
select* from payment inner join customer
on payment.customer_id =customer.customer_id;

--selecting the specific column  from both the table
select customer.customer_id,payment.payment_id,customer.first_name,
payment.payment_date from customer inner join payment
on customer.customer_id=payment.customer_id;

--2. full outer join
-- is null in the  full outer join
select * from customer full outer join payment
on customer.customer_id= payment.customer_id
where customer.customer_id is NULL
or payment.customer_id is NULL;


--3.left outer join
--select left outer join
select film.film_id,title,inventory_id,store_id
from film left join inventory on inventory.film_id=film.film_id;

--3.00 pm
select * from film;

select * from inventory;
--extract the null value  by using the null value
select film.film_id,title,inventory_id,store_id
from film left join inventory on inventory.film_id=film.film_id
where inventory.film_id is null;

--challenge

select district,email from address inner join customer 
on address.address_id=customer.address_id
where district='California';

select district from address;

select district,email from address inner join customer 
on address.address_id=customer.address_id
where district='QLD';
-- multiple
select * from film;
select * from film_actor;

select * from actor inner join film_actor
on actor.actor_id=film_actor.actor_id;

select * from actor inner join film_actor
on actor.actor_id=film_actor.actor_id
inner join film  on 
file_actor.film_id=film.film_id






-- 		ADVANCED SQL
show all;

show timezone;

select now();

select timeofday();

select current_date;

select * from payment;

select extract (year from payment_date) as my_year
from payment;

select EXTRACT (Month from payment_date) as pay_month
from payment;

select extract (quarter from payment_date) as pay_month
from payment;

select age(payment_date) from payment;

select to_char(payment_date,' ') from payment;


select to_char(payment_date,'MM/DD/YYYY') from payment;


select to_char(payment_date,'dd-mm-yyyy') from payment;

select distinct(to_char(payment_date,'month')) from payment;