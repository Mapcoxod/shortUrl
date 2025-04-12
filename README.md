
# shortUrl

Сервис для сокращения ссылок на Django.

## Описание

Сервис позволяет:
- Сокращать длинные ссылки
- Смотреть статистику по переходам
- Делать редирект по короткой ссылке
- Отображать статистику всех созданных ссылок в виде таблицы
- Работает через web-форму

---

## Технологии

- Python 3.11+
- Django 4.x
- Django REST Framework
- Bootstrap 5
- crispy-bootstrap5

---

## Запуск проекта

1. Клонировать репозиторий:
```bash
git clone https://github.com/Mapcoxod/shortUrl.git
cd shortUrl
```

2. Создать .env файл на основе .env.example

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Выполнить миграции:
```bash
python manage.py migrate
```

5. Запустить сервер:
```bash
python manage.py runserver
```

---

## Примеры ссылок:

- Главная страница: `/`
- Статистика всех ссылок: `/stats/`
- Переход по короткой ссылке: `/<short_token>/`

---

## Автор

- [Mapcoxod](https://github.com/Mapcoxod)
