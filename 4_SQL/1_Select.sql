--day 1/9/23
--challenge 1
select count(*) from payment where extract(dow from payment_date)=1;


--mathematical function
select * from film;
--division
select rental_rate / replacement_cost from film;

select rental_rate + replacement_cost from film;

select rental_rate - replacement_cost from film;

select rental_rate * replacement_cost from film;

select rental_rate % replacement_cost from film;

select rental_rate ^ replacement_cost from film;

select |/ replacement_cost from film;

select ||/ replacement_cost from film;

select factorial(rental_rate)   from film;

select !! rental_rate from film;

-- round()
select round(rental_rate / replacement_rate ,2) from film;

select round(rental_rate / replacement_rate ,4)*100 from film;

select round(rental_rate / replacement_rate ,4) * 100 as present_cost
from film;

select 0.1 * replacement_cost as deposite  from film;

select * from customer;

select length(first_name ) from customer;

select first_name || last_name from customer;

-- givie space between two string
select first_name||' '|| last_name from customer;

select first_name||' '|| last_name as full_name from customer;

select upper(first_name)||' '|| upper(last_name) as full_name from customer;
--creating the email
select left(first_name,1)|| last_name||'@gmail.com' from customer;

select right(first_name,1)|| last_name ||'@gmail.com' from customer;

select lower(left(first_name,1))|| lower(last_name)||'@gmail.com' from customer;

select lower(left(first_name,1))|| lower(last_name)||'@gmail.com' as custom_email
from customer;

--subquery
--film table
select * from film;

select avg(rental_rate) from film;

select title,rental_rate from film
where rental_rate > (select avg(rental_rate ) from film);
--rental table
select * from rental;

select * from inventory;

select * from rental 
where return_date between '2005-05-29' and '2005-05-30';

(select inventory .film_id from rental
inner join inventory on inventory.inventory_id=rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30');

select film_id, title from film
where film_id in 
(select inventory.film_id from rental
inner join inventory on inventory.inventory_id=rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30');

