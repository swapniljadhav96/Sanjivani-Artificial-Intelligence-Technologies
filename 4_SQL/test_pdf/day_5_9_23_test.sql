--test 5/9/23
--Q1.1.	How can you retrieve all the information from the cd.facilities table?
select * from cd.facilities;
-----------------------------------------------------------------
---Q2.	You want to print out a list of all of the facilities 
--and their cost to members. How would you retrieve a list of 
--only facility names and costs?
select name from cd.facilities;
select name ,membercost from cd.facilities
where membercost<=5
limit 4;
-------------------------------------------------------------------
--Q3.	How can you produce a list of facilities that charge a fee to members?
Select * from cd.facilities where membercost>0;
-------------------------------------------------------------------
--Q4.	How can you produce a list of facilities 
--that charge a fee to members, and that 
--fee is less than 1/50th of the monthly maintenance cost?
--Return the facid, facility name, member cost, and monthly
--maintenance of the facilities in question.
Select facid, name, membercost, monthlymaintenance from cd.facilities
where membercost>0 and membercost<(monthlymaintenance/50);
---------------------------------------------------------------------
--Q5.How can you produce a list of all facilities with 
--the word 'Tennis' in their name?
select* from cd.facilities
where name like '%Tennis%';
-----------------------------------------------------------------------
--Q6.How can you retrieve the details of facilities with 
--ID 1 and 5? Try to do it without using the OR operator.
select * from cd.facilities
where facid IN (1,5);
---------------------------------------------------------------------------
--Q7.How can you produce a list of members who joined after the start of
--September 2012? Return the memid, surname, firstname, and joindate of the 
--members in question.
select joindate from cd.members;
select memid,surname,firstname, joindate from cd.members
where joindate>'2012-09-01';
-------------------------------------------------------------------------
--Q8.How can you produce an ordered list of the 
--first 10 surnames in the members table? The list must not contain duplicates.
select distinct(surname) from cd.members
order by surname asc
limit 10;
-----------------------------------------------------
--Q9.You'd like to get the 
--signup date of your last member. How can you retrieve this information?
select joindate from cd.members
order by joindate desc
limit 1;
----------------------------------------------------------------
--Q10.	Produce a count of the number of 
--facilities that have a cost to guests of 10 or more
select count(guestcost) from cd.facilities
where guestcost>=10;
--or
select count(facid) from cd.facilities 
where guestcost>10;
---------------------------------------------------------------------

---Q11.Produce a list of the total number of slots booked 
--per facility in the month of September 2012. Produce an output 
--table consisting of facility id and slots, sorted by the number of slots.
select facid,sum(slots) as TotalSlots from cd.bookings
where starttime between '2012-09-01' and '2012-10-01'
group by facid;
----------------------------------------------------------------------
---Q12.	Produce a list of facilities with more than 1000 slots booked.
--Produce an output table consisting of facility id and total slots, 
--sorted by facility id.
select facid, sum(slots)  as total_slots from cd.bookings
group by facid
having sum(slots)>1000
order by facid asc;
-----------------------------------------------------------------------

--Q13.How can you produce a list of the start times for
--bookings for tennis courts, for the date '2012-09-21'?
--Return a list of start time and facility name pairings, ordered by the time.
--error

select starttime from cd.bookings;


select name,starttime as start  from cd.bookings inner join cd.facilities
on cd.bookings.facid=cd.facilities.facid
where  name like 'Tennis Court%' and starttime between '2012-09-21' and '2012-09-22' 
order by starttime ;


--------------------------------------------------------------------------
--Q14.14.How can you produce a list of the start times
--for bookings by members named 'David Farrell'?
select starttime from cd.bookings inner join cd.members
on cd.bookings.memid=cd.members.memid
where firstname='David' and surname='Farrell';
--------------------------------------------------------------------------

--Q13--Siranch aahe he khalch
select cd.bookings.starttime, cd.facilities.name
from cd.facilities
inner join cd.bookings
on cd.bookings.facid = cd.facilities.facid
where cd.facilities.facid in (0,1)
and cd.bookings.starttime >='2012-09-21'
and cd.bookings.starttime < '2012-09-22'
order by cd.bookings.starttime;