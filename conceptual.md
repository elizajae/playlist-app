### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

A relational database system

- What is the difference between SQL and PostgreSQL?

SQL is a language, PostgreSQL is a database system

- In `psql`, how do you connect to a database?

`\c <database name>`

- What is the difference between `HAVING` and `WHERE`?

Having is like a where clause but the where statement focuses on individual rows.

- What is the difference between an `INNER` and `OUTER` join?

Inner joiun keeps information from both tables that are related to eachother but an outer join keeps information that is not related to eachother.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

LEFT OUTER returns all records from the left table and the right outer returns all records from the right table as well as matched records from the left

- What is an ORM? What do they do?

An ORM is an object relational mapper. It maps objects to a relational database and created a brige between object oriented programming and relational database systems.

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?

AJAX is a way to make requests from the client side and requests is a way to make requests from the server side. AJAX requests are from the javascript frontend and requests is from the python backend.

- What is CSRF? What is the purpose of the CSRF token?

CSRD stands for Cross site request forgery and is a type of attack that forces a user to execute unwanted actions. The token's purpose is to identify the user and it must be included in the request to be valid.

- What is the purpose of `form.hidden_tag()`?

Used to protect the form from CSRF attacks
