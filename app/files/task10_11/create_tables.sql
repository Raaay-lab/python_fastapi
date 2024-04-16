CREATE TABLE IF NOT EXISTS users
  ( 
     person_code integer PRIMARY KEY, 
     first_name  varchar(15), 
     last_name   varchar(20), 
     hiredate    DATE 
  ); 

CREATE TABLE IF NOT EXISTS product 
  ( 
     product_name     varchar(25) PRIMARY KEY, 
     product_price    numeric(8, 2), 
     quantity_on_hand numeric(5, 0), 
     laststockdate    DATE 
  ); 

CREATE TABLE IF NOT EXISTS purchase 
  ( 
     product_name  varchar(25) references product(product_name), 
     salesperson   integer references users(person_code),
     purchase_date DATE, 
     quantity      numeric(4, 2) 
  );  

