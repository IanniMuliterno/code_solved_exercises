CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE
);

INSERT INTO Customers (customer_id, first_name, last_name, date_of_birth)
VALUES 
    (1, 'John', 'Doe', '1985-07-15'),
    (2, 'Jane', 'Smith', '1990-12-01'),
    (3, 'Alice', 'Johnson', '1982-03-22');

CREATE TABLE Policies (
    policy_id INT PRIMARY KEY,
    customer_id INT,
    policy_type VARCHAR(50),
    issue_date DATE,
    premium DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Policies (policy_id, customer_id, policy_type, issue_date, premium)
VALUES 
    (101, 1, 'Auto', '2022-05-08', 300),
    (102, 2, 'Home', '2023-01-15', 450),
    (103, 3, 'Life', '2021-08-30', 550);
    
/*
Exercise 1: Basic Data Retrieval
Objective: Retrieve information about insurance policies and the customers who hold them, focusing on policies that were issued in the last year.
Query: Write an SQL query to select the customer's full name, policy type, and premium for policies that were issued in the last year.



-- step 1: filter policies by year(issue_date) = (year(current_date()) - 1) 
-- step 2: join tables by customerid
-- select concat(first_name,last_name) as full_name, policy_type,premium

Exercise 2
Objective: Calculate the total premiums collected for each type of insurance policy.
Query: Write an SQL query to group the policies by their type and sum the premiums for each type.

Exercise 3
Objective: Identify customers who have both 'Home' and 'Auto' policies.
Query: Write an SQL query that selects the first name and last name of customers who own both an Auto and a Home policy.
*/
--exc 1 answer
select c.first_name || ' ' || c.last_name AS full_name, policy_type,premium
from policies p
join customers c on p.customer_id = c.customer_id
WHERE strftime('%Y', issue_date) = strftime('%Y', date('now', '-1 year'))

--exc 2 answer
select policy_type, sum(premium) as total_premium
from Policies
GROUP by policy_type


-- exc 3 solution steps
-- join tables
-- filter home and auto policies
-- select first_name, last_name
