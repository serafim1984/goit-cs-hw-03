import logging

from faker import Faker
import random
import psycopg2
from psycopg2 import DatabaseError

fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="serafim")
cur = conn.cursor()

# Додавання користувачів
for _ in range(3):

    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fake.name(), fake.email()))



# Додавання статусів

statuses = [('new',), ('in progress',), ('completed',)]

for _ in range(3):
    cur.execute("INSERT INTO status (name) VALUES (%s)", (statuses[_]))

# Додавання тасків

cur.execute("SELECT id FROM users")

u_ids = cur.fetchall()

user_ids = [u_id[0] for u_id in u_ids]

cur.execute("SELECT id FROM status")

s_ids = cur.fetchall()

status_ids = [s_id[0] for s_id in s_ids]



for _ in range(10):

    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (fake.word(), fake.text(), status_ids[random.randint(0, 2)], user_ids[random.randint(0, 2)]))


try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cur.close()
    conn.close()

