# Cloud Computing Project: medium

This is blogtest project that you can share your blogs

## Features
- watch the top blogs
- write new blog
- be a writer

---

## Project Overview
The **Book Manager** is designed to demonstrate fundamental concepts of cloud computing, including containerization, database integration, and RESTful API development.

---

## Technologies Used
- **Python 3.10**
- **Django 4.x**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Html**
- **Css**
- **JS**

---

## Installation

### Prerequisites
- Docker and Docker Compose installed on your system.
- Git installed to clone the repository.

### Steps


1. Build and start the containers:
```bash
docker-compose -f docker-compose.db.yml up --build -d
docker-compose -f docker-compose.app.yml up --build -d
```
2. Running Migrations Inside the Container
```bash
docker exec -it django_app bash
```
```bash
python manage.py migrate
```
```bash
exit
```

3. Access the application:

- Django API: http://localhost:8000

---

