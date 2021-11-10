-- Database: dvdrental

-- DROP DATABASE dvdrental;

-- select * from customer

-- select first_name || ' ' || last_name as full_name from customer 

-- select distinct create_date from customer  

-- select * from customer order by first_name desc

-- select film_id, title, description, release_year, rental_rate from film
-- order by rental_rate asc

-- select address,phone from address
-- where district = 'Texas'

-- select * from film 
-- where film_id in (15,150)

-- select film_id, title, description, length, rental_rate from film
-- where title = 'South Wait'

-- select film_id, title, description, length, rental_rate from film
-- where title ilike 'Su%'

-- select * from film
-- order by rental_rate asc limit 10

-- select * from film
-- order by rental_rate asc offset 10 fetch first 10 rows only;

-- select customer.customer_id, amount, payment_date from payment
-- full join customer on payment.customer_id = customer.customer_id
-- order by customer_id asc

-- select title, film.film_id, inventory.film_id from film
-- left join inventory
-- on inventory.film_id=film.film_id
-- where inventory.film_id is NULL

-- select city_id,city,country.country,country.country_id from city
-- left join country
-- on country.country_id = city.country_id
-- order by country asc