# 1. Создать проект

```bash
django-admin startproject <Название сайта>
```

# 2. Добавить приложение

```bash 
python manage.py startapp <название приложения>
```

# 3. Создать файл миграций (если были изменения в models.py)

```bash
python manage.py makemigrations
```

# 4. Выполнить миграцию (обновить базу данных)

```bash
python manage.py migrate
```