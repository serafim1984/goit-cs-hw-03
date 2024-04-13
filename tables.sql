-- Таблиця користувачів
drop table if exists users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR(100) NOT null,
  email VARCHAR(100) UNIQUE NOT NULL
);

-- Таблиця статусів
drop table if exists status;
CREATE TABLE status (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT null unique check (name in ('new', 'in progress', 'completed'))
);

-- Таблиця завдань
drop table if exists tasks;
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT null,
  description text,
  status_id INTEGER,
  user_id INTEGER,
  foreign key (status_id) references status (id),
  foreign key (user_id) references users (id)
    on delete cascade
);
