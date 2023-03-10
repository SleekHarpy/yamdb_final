# yamdb_final
![workflow](https://github.com/SleekHarpy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

Документация проекта:
http://51.250.10.2/redoc/

### Технологии:
![Python](https://img.shields.io/badge/Python-3.7-green)
![Django](https://img.shields.io/badge/Django-2.2.16-green)
![Nginx](https://img.shields.io/badge/Nginx-%20-lightgrey)
![Docker-compose](https://img.shields.io/badge/Docker--compose-%20-lightgrey)

### О проекте:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя 
посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут 
быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» 
группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить 
категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку 
в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка 
произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Шаблон наполнения env-файла:

1. Указываем, секретный ключ для settings.py:
```
SECRET_KEY=default-key
```
2. Указываем, что работаем с postgresql:
```
DB_ENGINE=django.db.backends.postgresql
```
3. Указываем имя базы данных:
```
DB_NAME=postgres
```
4. Указываем логин для подключения к базе данных:
```
POSTGRES_USER=login
```
5. Указываем пароль для подключения к БД:
```
POSTGRES_PASSWORD=password
```
6. Указываем название сервиса (контейнера):
```
DB_HOST=db
```
7. Указываем порт для подключения к БД:
```
DB_PORT=5432
```

### Установка

Для запуска приложения проделайте следующие шаги:

1. Клонируйте репозиторий.
```
https://github.com/SleekHarpy/yamdb_final.git
```

2. Перейдити в папку infra и запустите docker-compose.yaml (при установленном и запущенном Docker)
```
cd yamdb_final/infra
```

Образ проекта на DockerHub
```
docker pull rtlistate/yamdb_final
```

3. Запустите docker-compose.yaml (при установленном и запущенном Docker)


```
docker-compose up
```
3. Для пересборки контейнеров выполните команду:
```
docker-compose up -d --build
```
4. В контейнере web выполните миграции:
```
docker-compose exec web python manage.py migrate
```
5. Создатйте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
6. Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Проект запущен и доступен по адресу: [localhost](http://localhost/admin/)

### Загрузка тестовых значений в БД

Чтобы загрузить тестовые значения в базу данных перейдите в каталог проекта и скопируйте файл базы данных в контейнер приложения:
```
docker cp <DATA BASE> <CONTAINER ID>:/app/<DATA BASE>
```
Перейдите в контейнер приложения и загрузить данные в БД: 
```
docker container exec -it <CONTAINER ID> bash
python manage.py loaddata <DATA BASE>
```

### Авторы
- [Влад Шевцов](https://github.com/SleekHarpy)

