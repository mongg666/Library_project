# Django Library
Простой проект для учёта книг в библиотеке (Python, Django, SQLite, Bootstrap).

Инструкции по запуску в проекте / README.

# 📚 Django Library

Веб-приложение для учёта книг в библиотеке.  
Реализовано:
- Авторизация (Django auth)
- CRUD для книг
- Поиск и фильтрация каталога
- Интерфейс на Bootstrap
- База данных SQLite

---

## 🚀 Запуск проекта

### 1. Клонируйте репозиторий или распакуйте архив
```bash
git clone https://github.com/username/library_project.git
cd library_project

2. Создайте виртуальное окружение
```bash
python -m venv venv

Активация
Windows: venv\Scripts\activate
Linux / Mac: source venv/bin/activate

3. Установите зависимости
```bash
pip install -r requirements.txt

4. Примените миграции
```bash
python manage.py makemigrations
python manage.py migrate

5. Создайте суперпользователя
```bash
python manage.py createsuperuser

6. Запустите сервер
```bash
python manage.py runserver

7. Откройте в браузере

Главная страница: http://127.0.0.1:8000/

Админка: http://127.0.0.1:8000/admin/
