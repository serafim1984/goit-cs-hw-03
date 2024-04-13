-- Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.

SELECT 
    t.id, 
    t.title,
    t.description
FROM tasks t
WHERE user_id = 27;

-- Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.

SELECT 
    t.id, 
    t.title,
    t.description,
    t.status_id
FROM tasks t
WHERE status_id = (SELECT id 
    FROM status 
    WHERE name = 'new');

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.

UPDATE tasks
SET status_id = (select id from status where name = 'in progress')
WHERE id = 10;

-- Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.

SELECT 
    u.id, 
    u.fullname,
    u.email
FROM users u
WHERE id not in  (SELECT user_id from tasks *);

-- Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.

INSERT INTO tasks (title, description, status_id, user_id)
values ('new', 'new task for Tim', (select s.id from status s where name='in progress'), 30);

-- Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'

SELECT 
    t.id, 
    t.title,
    t.description    
FROM 
    tasks t
JOIN 
    status s ON t.status_id = s.id
WHERE 
    s.name != 'completed';

-- Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id

DELETE FROM tasks
WHERE id = 15;

-- Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.

select fullname FROM users where email like 'zmiller%';

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE

UPDATE users
SET fullname = ('Serafymovych Roman')
WHERE id = 28;

-- Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.

SELECT s.name, count(t.id) from tasks t join status s ON t.status_id = s.id group by s.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').

SELECT t.id, t.title, t.description from tasks t join users u ON t.user_id = u.id where u.email like '%@example.org';

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.

SELECT t.id, t.title from tasks t where t.description = '';

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.

SELECT u.fullname, t.title, t.status_id from users u inner join tasks t on t.user_id = u.id where t.status_id = (select id from status where name = 'in progress') group by u.fullname, t.title, t.status_id;

-- Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.

SELECT u.fullname, count(t.id) from users u left join tasks t on u.id = t.user_id group by u.fullname;

