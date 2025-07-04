# 🚀 Project Manager API

REST API для управления проектами и вакансиями.

## 📋 Описание

Бэкенд-сервис для хранения и управления проектами и вакансиями.
Реализованы все основные CRUD-операции для обеих сущностей, а также автоматическая
документация через Swagger и ReDoc.

---

## 🛠️ Технологии

- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- drf-yasg (Swagger/OpenAPI)
- poetry (для управления зависимостями)
- dotenv (для переменных окружения)

---

## ⚡ Быстрый старт

1. **Клонируйте репозиторий:**
    ```bash
    git clone <ссылка_на_ваш_репозиторий>
    cd <папка_проекта>
    ```

2. **Установите зависимости:**
    ```bash
    poetry install
    ```

3. **Создайте файл `.env` в корне проекта и заполните его, например:**
    ```
    SECRET_KEY=your-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_NAME=project_db
    DB_USER=postgres
    DB_PASSWORD=yourpassword
    DB_HOST=localhost
    DB_PORT=5432
    ```

4. **Примените миграции:**
    ```bash
    poetry run python manage.py migrate
    ```

5. **Запустите сервер:**
    ```bash
    poetry run python manage.py runserver 8000
    ```

6. **Откройте в браузере:**
    - [API](http://127.0.0.1:8000/api/projects/)
    - [Swagger UI](http://127.0.0.1:8000/swagger/)
    - [ReDoc](http://127.0.0.1:8000/redoc/)

---

## 📚 Примеры запросов

### Проекты

#### Получить список проектов
```http
GET /api/projects/
```

#### Создать проект
```http
POST /api/projects/
Content-Type: application/json

{
  "name": "My Project",
  "description": "Описание проекта",
  "owner": "Иван",
  "status": "active",
}
```

#### Получить проект по id
```http
GET /api/projects/1/
```

#### Обновить проект
```http
PUT /api/projects/1/
Content-Type: application/json

{
  "name": "New Name",
  "description": "Новое описание",
  "owner": "Иван"
}
```

#### Удалить проект
```http
DELETE /api/projects/1/
```

### Вакансии

#### Получить список вакансий
```http
GET /api/vacancies/
```

#### Получить вакансии по проекту
```http
GET /api/vacancies/?project=1
```

#### Создать вакансию
```http
POST /api/vacancies/
Content-Type: application/json

{
  "name": "Backend Developer",
  "description": "Python/Django",
  "owner": "Иван",
  "project": 1
}
```

#### Получить вакансию по id
```http
GET /api/vacancies/1/
```

#### Обновить вакансию
```http
PUT /api/vacancies/1/
Content-Type: application/json

{
  "name": "Backend Developer",
  "description": "Обновлённое описание",
  "owner": "Иван",
  "project": 1
}
```

#### Удалить вакансию
```http
DELETE /api/vacancies/1/
```

---

## 📝 Документация
- Swagger UI: [`/swagger/`](http://127.0.0.1:8000/swagger/)
- ReDoc: [`/redoc/`](http://127.0.0.1:8000/redoc/)

---

## 🧪 Мок-данные
Для тестирования можно использовать следующий пример:

```json
{
  "name": "Test Project",
  "description": "Тестовое описание",
  "owner": "Тестовый пользователь"
}
```

---

## 👤 Автор
maxx (m.petrykin@gmx.de | Telegram: @max_p95)