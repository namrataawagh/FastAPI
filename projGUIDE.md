# What I Learned Today - Introduction to Dynamic Software and HTTP

## 🧱 Static vs Dynamic Software

- **Static Software/Websites**:  
  These are non-interactive. The content is fixed and doesn't change unless updated by a developer.
  - Example: A basic portfolio website that only displays text and images.
  
- **Dynamic Software/Websites**:  
  These allow user interaction. The content can change based on user inputs or data manipulation.
  - Example: Instagram, Amazon, or any blog with comments.

---

## 🔄 CRUD Operations

Dynamic software typically supports operations known as **CRUD**:
- **C**: Create – Add new data (e.g., posting a new blog)
- **R**: Retrieve – View existing data (e.g., reading a blog)
- **U**: Update – Modify existing data (e.g., editing your post)
- **D**: Delete – Remove data (e.g., deleting a comment)

Any one or more of these operations make a software *dynamic*.

---

## 🌐 The Role of Web Servers and Clients

- When software becomes a website, it is hosted on a **web server**.
- Anyone accessing that website using a browser becomes a **client**.
- The client and the server communicate using **HTTP** (Hypertext Transfer Protocol).

---

## 📡 What is HTTP?

HTTP is the protocol that governs communication between clients (like your browser) and servers (where the website lives). It defines how messages are formatted and transmitted, and how servers and browsers should respond to various commands.

---

## 🧪 Common HTTP Methods

HTTP methods are used by clients to perform actions on server resources:

| Method  | Action                     | Use Case                           |
|---------|----------------------------|------------------------------------|
| **GET** | Retrieve data              | View a webpage or fetch content    |
| **POST**| Create new data            | Submit a form                      |
| **PUT** | Update/Replace existing data | Edit profile info                  |
| **DELETE** | Remove data            | Delete a blog post                 |

---

This is the foundational knowledge I gained today. It forms the backbone of understanding how modern websites and applications function.


# 🏥 Patient Management System API

## 📌 Overview

Today we started building a **simple FastAPI application** designed for **doctors** to manage patient records. This project helps demonstrate how RESTful APIs work in a real-world use case.

The API reads patient data from a JSON file and serves it through different HTTP endpoints.


---

## 🧠 What We Built

### project.py

```python
from fastapi import FastAPI
import json

app = FastAPI()

# Helper function to load data
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get("/view")
def view():
    data = load_data()
    return data
```

---

## 📦 Sample `patients.json`

Here is an example of what the `patients.json` file might contain:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "age": 45,
    "condition": "Diabetes"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": 29,
    "condition": "Asthma"
  }
]
```

---

## 🔍 API Endpoints

| Method | Endpoint     | Description                                      |
|--------|--------------|--------------------------------------------------|
| GET    | `/`          | Returns a welcome message for the API           |
| GET    | `/about`     | Provides info about the purpose of the API      |
| GET    | `/view`      | Displays all patient records from the JSON file |

---

## 🧪 Run the App

Make sure to install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Then start the server:

```bash
uvicorn main:app --reload
```

Visit:  
- `http://127.0.0.1:8000/` for the welcome page  
- `http://127.0.0.1:8000/docs` for the interactive Swagger UI  

---

## ✅ What I Learned

- Basics of how APIs work
- What endpoints are and how to define them
- How to serve and read data using JSON
- How to structure a small but functional FastAPI project

---
