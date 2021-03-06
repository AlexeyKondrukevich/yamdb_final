# YAMDB_FINAL
>"Review and comment your favourites"

![](https://img.shields.io/badge/Developed%20by-Kondr-blue) ![Yamdb Workflow Status](https://github.com/AlexeyKondrukevich/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

REST API проект для сервиса YaMDb — сбор отзывов о фильмах, книгах или музыке. 

Проект развернут тут [84.252.142.162/redoc/](http://84.252.142.162/redoc/)
## Описание 
 
Проект YaMDb собирает отзывы пользователей на произведения. 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Список категорий  может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
### Как запустить проект: 
Все описанное ниже относится к ОС Linux. 
Клонируем репозиторий и и переходим в него: 
```sudo 
git clone git@github.com:AlexeyKondrukevich/yamdb_final.git
cd yamdb_final 
cd api_yamdb 
``` 
 
Создаем и активируем виртуальное окружение: 
```sudo 
python3 -m venv venv 
source /venv/bin/activate (source /venv/Scripts/activate - для Windows) 
python -m pip install --upgrade pip 
``` 
 
Ставим зависимости из requirements.txt: 
```sudo 
pip install -r requirements.txt 
``` 

Переходим в папку с файлом docker-compose.yaml: 

```
cd infra 
``` 
 
Поднимаем контейнеры (infra_db_1, infra_web_1, infra_nginx_1): 
```sudo 
docker-compose up -d --build 
``` 

Выполняем миграции: 
```sudo 
docker-compose exec web python manage.py makemigrations reviews 
``` 
```sudo 
docker-compose exec web python manage.py migrate --run-syncdb
``` 

Создаем суперпользователя: 
```sudo 
docker-compose exec web python manage.py createsuperuser 
``` 

Србираем статику: 
```sudo 
docker-compose exec web python manage.py collectstatic --no-input 
``` 

Создаем дамп базы данных (нет в текущем репозитории): 

```
sudo docker-compose exec web python manage.py dumpdata > dumpPostrgeSQL.json 
``` 

Останавливаем контейнеры: 

```
sudo docker-compose down -v 
``` 

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env 
``` 
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db 
DB_PORT=5432 
``` 
### Документация API YaMDb 
Документация доступна [тут](http://84.252.142.162/redoc/)
