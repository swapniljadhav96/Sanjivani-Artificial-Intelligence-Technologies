--day 29_8_23
select count(distinct(district)) from address;
--challenge
select distinct(district) from address;
--chall
select count(rating) from film
where rating ='R' AND replacement_cost between 1 and 15;

select count(*) from film
where title like '%Truman%';



select * from film;

select min(replacement_cost) from film;
select max(replacement_cost),min(replacement_cost) from film;

select avg(replacement_cost) from film;
select round(avg(replacement_cost),2) from film;

select round(avg(replacement_cost),4) from film;

select sum(replacement_cost) from film;


--group by
select * from payment;


select customer_id from customer
GROUP BY customer_id
order by customer_id;

select customer_id ,sum(amount) from payment
group by customer_id;

select customer_id, sum(amount) from payment
group by customer_id
order by sum(customer_id);


select customer_id, sum(amount) from payment
group by customer_id
order by sum(customer_id) desc;

select * from payment;

--group by for multiple  column
select customer_id ,staff_id , sum(amount) from payment
group by staff_id,customer_id;

select customer_id ,staff_id , sum(amount) from payment
group by staff_id,customer_id
order by customer_id;

select date(payment_date), sum(amount) from payment
group by date(payment_date);

select date(payment_date), sum(amount) from payment
group by date(payment_date)
order by sum(amount) desc;

select staff_id,sum(amount) from payment
where staff_id between 1 and 2
group by staff_id;

select staff_id from payment;
