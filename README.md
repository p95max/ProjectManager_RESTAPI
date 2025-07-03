# Project Manager API
REST API для управления проектами и вакансиями.

## Описание
Это бэкенд-сервис для хранения и управления проектами.  
Реализованы все основные CRUD-операции для проектов, а также автоматическая документация через Swagger и ReDoc.

## Технологии
- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- drf-yasg (Swagger/OpenAPI)
- poetry (для управления зависимостями)
- dotenv (для переменных окружения)

## Быстрый старт
1. Клонируйте репозиторий:
    ```bash
    git clone <ссылка_на_ваш_репозиторий>
    cd <папка_проекта>
    ```

2. Установите зависимости:
    ```bash
    poetry install
    ```

3. Создайте файл `.env` в корне проекта и заполните его, например:
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

4. Примените миграции:
    ```bash
    poetry run python manage.py migrate
    ```

5. Запустите сервер:
    ```bash
    poetry run python manage.py runserver 8000
    ```

6. Откройте в браузере:
    - API: [http://127.0.0.1:8000/api/projects/](http://127.0.0.1:8000/api/projects/)
    - Swagger: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
    - ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Примеры запросов

### Получить список проектов

```http
GET /api/projects/
Создать проект
http
Copy Code
POST /api/projects/
Content-Type: application/json

{
  "name": "My Project",
  "status": "active",
  "description": "Описание проекта"
}
Получить проект по id
http
Copy Code
GET /api/projects/1/
Обновить проект
http
Copy Code
PUT /api/projects/1/
Content-Type: application/json

{
  "name": "New Name",
  "status": "archived",
  "description": "Новое описание"
}
Удалить проект
http
Copy Code
DELETE /api/projects/1/
Документация
Swagger UI: /swagger/
ReDoc: /redoc/
Мок-данные
Для тестирования можно использовать следующий пример:

json
Copy Code
{
  "name": "Test Project",
  "status": "active",
  "description": "Тестовое описание"
}
Деплой
Проект можно развернуть на любом хостинге, поддерживающем Python и PostgreSQL (например, Render, Railway, Heroku и др.).

Автор
Максим (или ваше имя)