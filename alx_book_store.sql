--create database
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store

--CREATE BOOKS TABLE
CREATE TABLE IF NOT EXISTS Books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130),
    author_id (Foreign Key referencing Authors table),
    price DOUBLE,
    publication_date DATE,
);

--CREATE AUTHORS TABLE
CREATE TABLE IF NOT EXISTS Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215),
);

--CREATE CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT,
);

--CREATE ORDERS TABLE
CREATE TABLE IF NOT EXISTS Orders(
order_id INT AUTO_INCREMENT PRIMARY KEY,
customer_id (Foreign Key referencing Customers table),
order_date DATE,
);

--CREATE ORDERS_DETAILS TABLE
CREATE TABLE IF NOT EXISTS Orders_Details(
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id (Foreign Key referencing Orders table),
    book_id (Foreign Key referencing Books table),
    quantity DOUBLE,
);


