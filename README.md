# Cloud Computing Project: Book Manager

This is a cloud-based book management application built with Django and PostgreSQL. It allows users to manage their book collection with a "read" or "not read" status.

## Features
- Manage books with attributes: title, author, and read status.
- RESTful API for CRUD operations.
- Dockerized setup for seamless deployment.
- Uses PostgreSQL as the database backend.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)

---

## Project Overview
The **Book Manager** is designed to demonstrate fundamental concepts of cloud computing, including containerization, database integration, and RESTful API development.

---

## Technologies Used
- **Python 3.10**
- **Django 4.x**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Postman (for API testing)**

---

## Installation

### Prerequisites
- Docker and Docker Compose installed on your system.
- Git installed to clone the repository.

### Steps
1. Clone the repository:
```bash
git clone https://github.com/Erfan003/cloud_computing_Project.git
cd cloud_computing_Project
```

2. Create a .env file in the root directory with the following format:
```env
DATABASE_NAME=book_manager
DATABASE_USER=book_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=postgres_db
DATABASE_PORT=5432
```

3. Build and start the containers:
```bash
docker-compose -f docker-compose.db.yml up --build -d
docker-compose -f docker-compose.app.yml up --build -d
```
4. Running Migrations Inside the Container
```bash
docker exec -it django_app bash
```
```bash
python manage.py migrate
```
```bash
exit
```

5. Access the application:

- Django API: http://localhost:8000

---

### Usage
1. Test the API using tools like Postman or Curl.

2. Example API requests:
- GET all books: GET http://localhost:8000/api/books/
- Create a book
```
POST http://localhost:8000/api/books/
Content-Type: application/json
{
  "title": "Fahrenheit 451",
  "author": "Ray Bradbury",
  "is_read": true
}
```
3. To stop the application:
```bash
docker-compose down
```
API Endpoints
Method	Endpoint	Description
GET	/api/books/	List all books
POST	/api/books/	Add a new book
GET	/api/books/<id>/	Retrieve a book
PUT	/api/books/<id>/	Update a book
DELETE	/api/books/<id>/	Delete a book

## API Endpoints

| Method | Endpoint              | Description           |
|--------|-----------------------|-----------------------|
| GET    | `/api/books/`         | List all books        |
| POST   | `/api/books/`         | Add a new book        |
| GET    | `/api/books/<id>/`    | Retrieve a book       |
| PUT    | `/api/books/<id>/`    | Update a book         |
| DELETE | `/api/books/<id>/`    | Delete a book         |
