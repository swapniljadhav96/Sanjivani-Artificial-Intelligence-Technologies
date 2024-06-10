--day_6_9_23
--view
select * from customer;

select * from address;

select first_name,last_name,address from customer inner join address
on customer.address_id=address.address_id;

create VIEW customer_info as select first_name,last_name,address 
from customer inner join address
on customer.address_id=address.address_id;

select * from customer_info;
--create or replace
create or replace VIEW customer_info as select first_name,last_name,address,district
from customer inner join address
on customer.address_id=address.address_id;

select * from customer_info;

-- drop the view
drop view if exists customer_info;

-- alter view and and rename
alter view customer_info rename to c_info;

select * from customer_info;

select * from c_info;

drop view c_info;

--*******************************************
--import and export the file 
--in the database testme 
create table simple(A INTEGER,
				   	B INTEGER,
				   C INTEGER
				   );
				   
				   
SELECT * FROM simple;

select * from simple;