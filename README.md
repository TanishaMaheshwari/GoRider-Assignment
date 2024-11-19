# **Flask MongoDB CRUD API**  
A simple Flask-based REST API for performing CRUD operations on a MongoDB database for a User resource. The API exposes endpoints to manage users, including creating, reading, updating, and deleting users.

---

## **Table of Contents**  
- [Introduction](#introduction)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup and Installation](#setup-and-installation)  
- [API Endpoints](#api-endpoints)  
- [Usage](#usage)  
- [Contributing](#contributing)  

---

## **Introduction**  
This application is a RESTful API built using Flask and MongoDB, designed to manage user data through a set of HTTP endpoints. The application uses Docker for containerization and is ideal for managing user data in a simple, scalable manner.

---

## **Features**  
- **CRUD Operations**:  
  Perform Create, Read, Update, and Delete operations on user data.
- **User Resource**:  
  Manage user data with fields like `id`, `name`, `email`, and `password`.
- **MongoDB Integration**:  
  Store user data in a MongoDB database.
- **Dockerized Application**:  
  The application is containerized using Docker for ease of deployment.

---

## **Tech Stack**  
- **Flask**: Lightweight Python web framework for building REST APIs.
- **MongoDB**: NoSQL database for storing user data.
- **Docker**: Containerization tool for packaging and deploying the application.
- **Flask-PyMongo**: Flask extension for MongoDB integration.

---

## **Setup and Installation**  

### **Prerequisites**  
- Python 3.x  
- Docker  
- Docker Compose  

### **Installation**  
1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/yourusername/flask-mongodb-crud.git  
   cd flask-mongodb-crud


2. **Build and run the application with Docker**:  
   ```bash  
   docker-compose up --build  
   ```

   This will set up the Flask application and MongoDB in Docker containers.

---

## **API Endpoints**  
### **GET /users**  
Returns a list of all users.  
**Response**:  
```json  
[  
  {  
    "id": "1",  
    "name": "John Doe",  
    "email": "john@example.com",  
    "password": "hashed_password"  
  },  
  ...  
]  
```

### **GET /users/<id>**  
Returns a single user with the specified ID.  
**Response**:  
```json  
{  
  "id": "1",  
  "name": "John Doe",  
  "email": "john@example.com",  
  "password": "hashed_password"  
}  
```

### **POST /users**  
Creates a new user. Requires JSON data for `name`, `email`, and `password`.  
**Request Body**:  
```json  
{  
  "name": "Jane Doe",  
  "email": "jane@example.com",  
  "password": "password123"  
}  
```

**Response**:  
```json  
{  
  "id": "2",  
  "name": "Jane Doe",  
  "email": "jane@example.com",  
  "password": "hashed_password"  
}  
```

### **PUT /users/<id>**  
Updates the user with the specified ID.  
**Request Body**:  
```json  
{  
  "name": "Updated Name",  
  "email": "updated_email@example.com",  
  "password": "newpassword123"  
}  
```

**Response**:  
```json  
{  
  "id": "2",  
  "name": "Updated Name",  
  "email": "updated_email@example.com",  
  "password": "hashed_password"  
}  
```

### **DELETE /users/<id>**  
Deletes the user with the specified ID.  
**Response**:  
```json  
{  
  "message": "User deleted successfully."  
}  
```

---

## **Usage**  

After setting up the application, you can interact with the API using tools like [Postman](https://www.postman.com/) or `curl` by sending HTTP requests to the appropriate endpoints.

For example, you can test the CRUD operations:

1. **Create a new user**:  
   - Use a POST request to `/users` with user data in the body.

2. **Get all users**:  
   - Use a GET request to `/users`.

3. **Update a user**:  
   - Use a PUT request to `/users/<id>` with the updated user data.

4. **Delete a user**:  
   - Use a DELETE request to `/users/<id>`.

---

## **Contributing**  
Feel free to fork the repository, make changes, and submit a pull request. All contributions are welcome!

---

## **Acknowledgements**  
- [Flask](https://flask.palletsprojects.com/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/)

```
