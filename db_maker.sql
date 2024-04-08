CREATE TABLE company
(
	company_id int NOT NULL UNIQUE PRIMARY KEY,
	company_name varchar(60),
	open_vacancies int,
	vacancies_url varchar(60)
);

CREATE TABLE vacancies
(
	vacancy_id int NOT NULL UNIQUE PRIMARY KEY,
	vacancy_name varchar(100),
	published_at date,
	salary int,
	salary_currency varchar(30),
	schedule varchar(30),
	experience varchar(30),
	company_id int
	REFERENCES company(company_id),
	contacts_mail varchar(30) DEFAULT 'none'
);