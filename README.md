# 📝 Task Management API - Django & DRF

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/task-manager-api)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/task-manager-api)
![GitHub contributors](https://img.shields.io/github/contributors/yourusername/task-manager-api)
![GitHub forks](https://img.shields.io/github/forks/yourusername/task-manager-api?style=social)

## 📢 Overview
The **Task Management API** is a **Django REST Framework (DRF)**-based backend service that enables users to:
- ✅ **Create tasks**
- ✅ **Assign tasks to users**
- ✅ **Retrieve assigned tasks**
- ✅ **Update task status**
- ✅ **Delete tasks**  

This API follows **RESTful architecture** and supports **multi-user task assignments**.

---

## 📌 Features
- ✅ **User Authentication** (Custom User Model)
- ✅ **CRUD operations on Tasks**
- ✅ **Many-to-Many Task Assignments**
- ✅ **Django REST Framework (DRF) API**
- ✅ **SQLite Database (Switchable to PostgreSQL/MySQL)**
- ✅ **REST API Documentation**
- ✅ **Cloud Deployment Ready**

---

## 📌 Tech Stack
| Technology | Description |
|------------|------------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Core programming language |
| ![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white) | Web framework for backend development |
| ![Django REST Framework](https://img.shields.io/badge/-DRF-red?logo=django) | API development framework |
| ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white) | Default database (Can be changed to PostgreSQL/MySQL) |
| ![Postman](https://img.shields.io/badge/-Postman-FF6C37?logo=postman&logoColor=white) | API testing tool |
| ![Heroku](https://img.shields.io/badge/-Heroku-430098?logo=heroku) | Cloud deployment platform |

---

## 📌 Project Structure
task_manager/ │── task_manager/ │ ├── init.py │ ├── settings.py │ ├── urls.py │ ├── asgi.py │ ├── wsgi.py │── tasks/ │ ├── migrations/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── serializers.py │ ├── views.py │ ├── urls.py │── manage.py │── README.md │── requirements.txt

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

