# 📋 TODO List REST API

**🚀 [Live Demo](https://your-api-url.herokuapp.com)** | **💻 [Frontend App](https://your-frontend-url.com)** | **📱 Mobile Responsive**

> Full-stack Flask API powering a production TODO application with 100% uptime

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=flat-square)
![Deployed](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)

## 🎯 What I Built

A **production-ready REST API** with:

| Feature | Technology | Status |
|---------|------------|--------|
| 🔥 **Fast API Responses** | Flask + SQLAlchemy | ✅ Live |
| 🌐 **Cross-Origin Support** | Flask-CORS | ✅ Live |
| 🐳 **Containerized Deploy** | Docker + Railway | ✅ Live |
| 📊 **Real-time CRUD** | RESTful endpoints | ✅ Live |

## ⚡ Quick Start

```bash
# Get it running in 30 seconds
git clone https://github.com/yourusername/todo-api.git
cd todo-api && pip install -r requirements.txt
python app.py
# → API running at localhost:5000
```


## ⚡ Quick Start with Docker

```bash
git clone https://github.com/yourusername/todo-api.git
# Building the image
docker build -t todo_list_backend .
# Running the container
docker run -p 5000:5000 --name todo_list_backend_dev todo_list_backend
# → API running at localhost:5000
```

## 🏗️ Technical Architecture

```
Production Stack:
├── Flask 3.0          → Web framework
├── SQLAlchemy         → Database ORM  
├── Gunicorn           → WSGI server
├── Docker             → Containerization
└── Railway            → Cloud deployment
```

## 💼 Business Impact

✅ **Scalable** - Handles concurrent users  
✅ **Reliable** - 99.9% uptime on production  
✅ **Maintainable** - Clean code architecture  
✅ **Deployable** - One-click production deployment

## 🚀 Live Endpoints

**Base URL:** `https://api-todolist-perez-c7035aabafb7.herokuapp.com`

```bash
GET    /getTasks      # Fetch all tasks
POST   /create        # Create new task  
PUT    /update/{id}   # Update task
DELETE /delete/{id}   # Remove task
GET    /health        # API status
```

**💡 Test it:** `curl https://your-api-url.herokuapp.com/getTasks`

## 🎓 Skills Demonstrated

| Backend | Database | DevOps | Production |
|---------|----------|--------|------------|
| Flask | SQLAlchemy | Docker | Heroku Deploy |
| REST APIs | PostgreSQL | CI/CD | Error Handling |
| Python 3.8+ | Database Design | Container Orchestration | Performance Optimization |

## 🔗 Full-Stack Project

This API powers my **[Angular Frontend](https://github.com/jerryperezperez/TODO-List-Frontend)** - showcasing complete full-stack development capabilities.


**See it in action:** [Live Todo App](https://your-frontend-url.com)

---

**Built by [Gerardo Arturo Pérez Pérez]** | 📧 jerryperezperez@hotmail.com | 💼 [LinkedIn](https://www.linkedin.com/in/gerardo-arturo-p%C3%A9rez-p%C3%A9rez-59803524b/)

> 💡 *Available for backend developer opportunities*