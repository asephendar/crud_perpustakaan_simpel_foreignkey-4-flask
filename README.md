# crud_perpustakaan_simpel_foreignkey-4-flask

Membuat query database :

CREATE TABLE categories (
	name VARCHAR(255) UNIQUE NOT NULL PRIMARY KEY,
	description TEXT
)

CREATE TABLE authors (
	name VARCHAR(255) NOT NULL PRIMARY KEY, 
	nationality VARCHAR(255) NOT NULL, 
	year_birth INT
)

CREATE TABLE books (
	title VARCHAR(255) UNIQUE NOT NULL PRIMARY KEY, 
	author VARCHAR(255) NOT NULL, 
	year INT NOT NULL, 
	total_pages INT NOT NULL, 
	category VARCHAR(255),
	
	FOREIGN KEY (category) REFERENCES categories(name),
	FOREIGN KEY (author) REFERENCES authors(name)
)
