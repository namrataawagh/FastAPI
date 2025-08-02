# FastAPI
## *INTRODUCTION:*
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints

# 🏎️ FastAPI Summary Notes

## 🚀 Why FastAPI?

FastAPI is:
- **Fast to code** ✅
- **Fast to run** ⚡

---

## 🌐 How APIs Work in Web Servers

1. A **web server** receives an **HTTP request** from the user.
2. This request is passed to an **API**.
3. The API processes the request — e.g., runs a **machine learning model** to predict outcomes based on user input.
4. The result is returned as an **HTTP response** to the user.

---

## 🔄 Translating Between HTTP and Python

- Since **HTTP** is a web protocol and **APIs are written in Python**, we need a **translator**.
- This translator is called **SGI (Server Gateway Interface)**.

There are two types of SGIs:

### 1. **WSGI (Web Server Gateway Interface)**
- **Synchronous** & **blocking**
- Works on one request at a time — others must wait.
- Common tools:
  - **Werkzeug**: Library for building WSGI apps.
  - **Gunicorn**: WSGI-compatible HTTP server.
- Example framework: **Flask**

### 2. **ASGI (Asynchronous Server Gateway Interface)**
- **Asynchronous** & **non-blocking**
- Can handle multiple requests concurrently.
- Common tools:
  - **Starlette**: ASGI framework (used internally by FastAPI)
  - **Uvicorn**: ASGI-compatible HTTP server
- Example framework: **FastAPI**

---

## 🔁 Key Difference: Sync vs Async

| Feature          | WSGI (Flask) | ASGI (FastAPI)     |
|------------------|--------------|---------------------|
| Processing Type  | Synchronous  | Asynchronous        |
| Request Handling | One at a time| Multiple concurrently|
| Latency          | High         | Low                 |
| Server           | Gunicorn     | Uvicorn             |
| Protocol Lib     | Werkzeug     | Starlette           |
| Async Support    | ❌ No         | ✅ Yes (uses `async`/`await`) |

---

## ⚡ Why FastAPI is *Fast to Run*

- **ASGI-based** → async & non-blocking
- **Uses Uvicorn + Starlette**
- Can handle many users simultaneously without waiting

---

## 🧑‍💻 Why FastAPI is *Fast to Code*

- ✅ **Automatic input validation** (via type hints + Pydantic)
- ✅ **Auto-generated interactive docs** (Swagger UI, ReDoc)
- ✅ **Seamless integration** with:
  - Docker
  - OAuth2
  - Kubernetes
  - SQLModel / Databases

---

# Running a Basic FastAPI App

##  Sample FastAPI Code

```python
from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

# Define route for a GET request at the root endpoint "/"
@app.get("/")  # Home URL
def hello():
    return {'message': 'Hello World!'}

# Define another route at "/about"
@app.get("/about")
def about():
    return {'message': 'This is what happens when you create another endpoint called about'}
```
# ▶️ How to Run This Code

To run the FastAPI app, use the following command:

```bash
uvicorn main:app --reload
```

### Explanation:

* `main`: This is the name of your Python file (e.g., `main.py`). You write `main` without the `.py` extension.
* `app`: This is the FastAPI app instance created using `app = FastAPI()`.
* `--reload`: This enables auto-reload. Any changes you make to the code will automatically refresh the server during development — no need to restart manually.

---

#  What Happens in the Background?

When you run the command `uvicorn main:app --reload`, the following happens:

* The **Uvicorn server** starts running.
* It listens for **HTTP requests**.
* Routes like `/` and `/about` are handled by the functions decorated with `@app.get(...)`.
* These functions run the logic defined inside them and return responses.

---

#  Accessing the Routes in Your Browser

After running the app, go to the following URLs:

### 🔹 Root Endpoint

* **URL**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Response**:

  ```json
  { "message": "Hello World!" }
  ```

### 🔹 About Endpoint

* **URL**: [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)
* **Response**:

  ```json
  { "message": "This is what happens when you create another endpoint called about" }
  ```

---

#  API Documentation (Auto-Generated)

FastAPI automatically generates documentation for your API.

### Available at:

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → **Swagger UI** (Interactive)
* [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) → **ReDoc** (Clean & structured)

These docs are generated based on:

* Your defined endpoints
* The input/output data (especially useful when using type hints and models)

---

#  Summary

* ✅ FastAPI app is created using `FastAPI()` and assigned to `app`.
* ✅ Routes are defined using decorators like `@app.get("/")`.
* ✅ Uvicorn is used to run the server: `uvicorn main:app --reload`
* ✅ `--reload` helps auto-refresh during development.
* ✅ Built-in documentation is instantly available at `/docs` and `/redoc`.

> **FastAPI makes building, testing, and documenting APIs incredibly fast and easy **

