## Question 1

You want to generate a relational representation of a menu where an order consists of an order number, a table number, and one selection from each of an entrée, a main course, and a dessert. Draw a diagram to show this as a relational representation. Hint: it should be more than one table. Provide the SQL commands to create this database and give an example of entering data into it.

![[docs/Images/menu.png]]

```sql
CREATE TABLE entrees (
  entree_id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  price INTEGER
);

CREATE TABLE mains (
  main_id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  price INTEGER
);

CREATE TABLE desserts (
  dessert_id INTEGER PRIMARY KEY,
  name VARCHAR(50),
  price INTEGER
);

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  table_number INTEGER,
  entree_id INTEGER REFERENCES entrees(entree_id),
  main_id INTEGER REFERENCES mains(main_id),
  dessert_id INTEGER REFERENCES desserts(dessert_id)
);
```

```sql
INSERT INTO entrees (entree_id, name, price) VALUES (1, 'Caesar Salad', 10);
INSERT INTO mains (main_id, name, price) VALUES (1, 'Steak', 20);
INSERT INTO desserts (dessert_id, name, price) VALUES (1, 'Apple Pie', 7);
INSERT INTO orders (order_id, table_number, entree_id, main_id, dessert_id) VALUES (1, 5, 1, 1, 1);
```
## Question 2

Find a real world use of MongoDB and use a paragraph to explain why it makes sense to use a database such as this for this application. Be specific about the use of NoSQL and the type of NoSQL database in use here.

```
Healthcare professionals need to be able to manage varying clinical workflows and unique patient data

Focusing on patient data, it is obvious that these records can vary grealy amongst each other. They might include text based notes, numerical data from blood work, images from x-rays, etc. MongoDB can allow for diverse and evolving data, which would be much more beneficial than a traditional relational database. 
```

## Question 3 (You will need Week 4's lectures from here on)

In your own words, explain what normalisation is and why we use it.

```
Normalisation is a procedure which we apply to databases to organise data to avoid duplication, which in turn helps to ensure that our use of the database is consistent and accurate, i.e The data we retrieve from the database is the same regardless of the route in which we query it.  

We achieve this by dividing larger tables into smaller ones and defining relationships amongst them to ensure that each table stores an atomic set of relations. 
```

## Question 4

One of the rules of converting to first normal form (1NF) is that all attributes must be _atomic_, that is indivisible. Look at the table below and identity which of these attributes are indivisible and which you think need to be broken up. Submit the table with atomic attributes. You may add as many additional columns as you need. List any assumptions that you've made.

|   |   |   |   |   |
|---|---|---|---|---|
|Name|Address|Physical|year of birth|Debts|
|Jane Smith|10 Alpha St, Kensington|1.70m, 59kg|2001|$20000 HELP, $5K HECS|
|Jim Smith|2 Owen St, Adelaide|1.8m, 75kg|1995|$40000 HELP|
|Jay Smith|10 Scotts Road, Stirling|1.5m, 49kg|2002|$10K HECS|

```
Most of this table can be broken up even further.

Name can be split into first and last name, stored inside a seperate 'users' table.

Address should be turned into a seperate table with an address ID and stores street number, street name, suburb, city. 

Physicals can be turned into a seperate table with a physical ID, that references a 'user' ID and stores height, weight

Year of birth is atomic, should be stored in the users table.

Debts can be turned into a seperate table that references a 'user' ID and stores attributes for each type of debt - HECS, HELP, etc.
```

**Users Table**

|UserID|FirstName|LastName|YearOfBirth|
|---|---|---|---|
|1|Jane|Smith|2001|
|2|Jim|Smith|1995|
|3|Jay|Smith|2002|

**Address Table**

|AddressID|UserID|StreetNumber|StreetName|Suburb|
|---|---|---|---|---|
|1|1|10|Alpha St|Kensington|
|2|2|2|Owen St|Adelaide|
|3|3|10|Scotts Road|Stirling|

**Physicals Table**

|PhysicalID|UserID|Height|Weight|
|---|---|---|---|
|1|1|1.70m|59kg|
|2|2|1.8m|75kg|
|3|3|1.5m|49kg|

**Debts Table**

|DebtID|UserID|Type|Amount|
|---|---|---|---|
|1|1|HELP|$20000|
|2|1|HECS|$5K|
|3|2|HELP|$40000|
|4|3|HECS|$10K|

## Question 5

We want to use a random number generator to simulate car numberplates using a scheme loosely based on the South Australian scheme. Each plate number will consist of a leading S, followed by three alphabetic characters (starting with AAA), where, for each of the alphabetic combinations, we have an associated three digit number starting with 000 and going to 999. Hence. SAAA000, SAAA001, SAAA002, ... SAAA999, SAAB000, SAAB001 and so on. (Real SA plates are the other way around.)

Assume that we start at SAAA000 and the highest possible numberplate possible is SCZZ999. Write a Python program that:

- starts by setting the "match string" to 000.
- LOOP: generates one of these randomly,
- increments a counter
- then checks it to see if the digits generated match the match string (at the start, 000).
- If we match, and the number is not 999, we increment the match string by 1. (hence 000 goes to 001).
- If number is 999, EXIT:, otherwise go back to LOOP:
- EXIT: Display how many random numbers had to be generated until you found all of the match strings in order.

For example:

Starting from SAAA000 to SCZZ999  
Running...  
Finished  
It took 874000 iterations.

Run your code several times with different iterations. What elements can you remove from this code to improve performance without costing accuracy?

```python
import random
import string

def random_plate():
    chars = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits = ''.join(random.choices(string.digits, k=3))
    return f"S{chars}{digits}"

plate_count = 0
current_match = '000'
while current_match != '999':
    plate = random_plate()
    plate_count += 1
    if plate.endswith(current_match):
        current_match = str(int(current_match) + 1).zfill(3)

print(f"It took {plate_count} iterations.")
```

- We can break apart the random choices to limit the value of the first letter to be between a and c
- We can run the same program on multiple threads maybe?
- Instead of relying on the random function to generate letters, we can generate an array of randomly shuffled numbers which will set the seed of every subsequent random plate. This ensures that no plate will ever be found more than once