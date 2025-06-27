--Write a script that inserts a single row in the table customer (database alx_book_store)
INSERT INTO CUSTOMERS (
    CUSTOMER_ID,
    CUSTOMER_NAME,
    EMAIL,
    ADDRESS
) VALUES (
    1,
    'Cole Baidoo',
    'cbaidoo@sandtech.com',
    '123 Happiness Ave.'
);

SELECT 'New customer added successfully!' AS MESSAGE;
