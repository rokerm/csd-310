-- Malachi Roker
-- 08/05/2023
-- CYBR410
-- WhatABook: Database and Table Creation

-- drop test user if it is present
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop fk constraints if they are present
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;

-- drop tables if they are present
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;

-- create user table
CREATE TABLE user (
user_id  INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(75) NOT NULL,
last_name VARCHAR(75) NOT NULL,
PRIMARY KEY(user_id)
);

-- create book table
CREATE TABLE book (
book_id INT NOT NULL AUTO_INCREMENT,
book_name VARCHAR(200) NOT NULL,
details VARCHAR(500),
author VARCHAR(200) NOT NULL,
PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
wishlist_id INT NOT NULL AUTO_INCREMENT,
user_id INT NOT NULL,
book_id INT NOT NULL,
PRIMARY KEY(wishlist_id),
CONSTRAINT fk_user
FOREIGN KEY(user_id)
	REFERENCES user(user_id),
CONSTRAINT fk_book
FOREIGN KEY(book_id)
	REFERENCES book(book_id)
);

CREATE TABLE store (
store_id INT NOT NULL,
locale VARCHAR(500) NOT NULL,
PRIMARY KEY(store_id)
);

-- insert into user records
INSERT INTO user(first_name, last_name)
	VALUES('Maximillian', 'Pegasus');
    
INSERT INTO user(first_name, last_name)
	VALUES('Laura', 'Croft');
    
INSERT INTO user(first_name, last_name)
	VALUES('Quincy', 'Newkirk');
    

-- insert into book records
INSERT INTO book(book_name, author, details)
	VALUES('Dark Psychology and Manipulation', 'Brandon Goleman', "The Ultimate Guide to Persuasion");
    
INSERT INTO book(book_name, author, details)
	VALUES('A Wrinkle in Time', 'Madeleine Lengle', "A dangerous and extrodinary adventure" );
    
INSERT INTO book(book_name, author, details)
	VALUES('The Last Stand of Fox Comapany', 'Bob Drury and Tom Clavin', "A true story of U.S. Marine Combat");
    
INSERT INTO book(book_name, author, details)
	VALUES('City of Bones', 'Cassandra Clare', "First Shadow Hunters Novel");
    
INSERT INTO book(book_name, author, details)
	VALUES('City of Ashes', 'Cassandra Clare', "Second Shadow Hunters Novel");
    
INSERT INTO book(book_name, author, details)
	VALUES('The Titans Curse', 'Rick Riordan', "Book Three of Percy Jackson and the Olympians");
    
INSERT INTO book(book_name, author, details)
	VALUES('Man and His Symbols', 'Carl Jung', "Carl Jung examines the full world of the unconscious");
    
INSERT INTO book(book_name, author, details)
	VALUES('The Everything Box', 'Richard Kadrey', "Starting the apocalypse is not easy");
    
INSERT INTO book(book_name, author, details)
	VALUES('Basic Fishing: A Beginners Guide', 'Wade Bourne', "A great beginner's guide for Burgeoning Fishermen");
    
    -- insert wishlist records
INSERT INTO wishlist(user_id, book_id)
	VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Maximillian'),
        (SELECT book_id FROM book WHERE book_name = 'Dark Psychology and Manipulation'));
        
INSERT INTO wishlist(user_id, book_id)
	VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Laura'),
        (SELECT book_id FROM book WHERE book_name = 'City of Bones')); 
        
INSERT INTO wishlist(user_id, book_id)
	VALUES(
        (SELECT user_id FROM user WHERE first_name = 'Quincy'),
        (SELECT book_id FROM book WHERE book_name = 'The Everything Box'));
        
INSERT INTO store(locale)
	VALUES('1058 N 114th Ave, Papillion, NE 68046');
    


        
        
	
        
    


    





    