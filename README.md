# Cook_Book
 
## Как установить

Python 3.11 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### будет установлен:

django==5.0.1

## Как запустить

Для создания таблиц проведите миграции
```
python manage.py makemigrations
python manage.py migrate
```
Для запуска веб сервера
```
python manage.py runserver
```
Для входа в админку создайте учётную запись
```
python manage.py createsuperuser
```
И авторизуйтесь http://127.0.0.1:8000/admin/