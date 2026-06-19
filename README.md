# 🐳 Docker Foundations

<div align="center">

### Modern Docker & Docker Compose Learning Repository

Build, Package, Deploy, and Manage Applications using Docker through Practical Hands-on Projects.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-326CE5?style=for-the-badge\&logo=docker\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)
![DevOps](https://img.shields.io/badge/DevOps-Practices-blue?style=for-the-badge)

**A complete hands-on guide to mastering containerization and multi-container application deployment using Docker and Docker Compose.**

</div>

---

## 📌 Overview

Docker has become one of the most essential tools in modern software development and DevOps workflows. This repository provides practical examples and real-world projects designed to help developers understand containerization from the ground up.

Through structured modules and hands-on exercises, you'll learn how to:

* Build Docker Images
* Run and Manage Containers
* Configure Volumes
* Create Container Networks
* Use Docker Compose
* Deploy Multi-Container Applications
* Follow Modern DevOps Practices

---

## 🚀 Why Docker?

Traditional application deployments often face issues such as:

❌ Dependency conflicts
❌ Environment inconsistencies
❌ Complex setup processes
❌ Difficult scaling and maintenance

Docker solves these problems by providing:

✅ Environment Consistency
✅ Lightweight Containers
✅ Faster Deployments
✅ Better Resource Utilization
✅ Simplified Dependency Management
✅ Seamless CI/CD Integration
✅ Improved Application Isolation

---

## 🏗 Docker Architecture

```text
+----------------------+
|    Docker Client     |
+----------+-----------+
           |
           v
+----------------------+
|    Docker Engine     |
+----------+-----------+
           |
    ----------------
    |              |
    v              v

+---------+   +---------+
| Images  |   |Volumes  |
+---------+   +---------+

      |
      v

+------------------+
|   Containers     |
+------------------+
```

---

## 📚 Core Docker Components

### 🖼 Docker Images

Images are immutable templates used to create containers.

```bash
docker build -t my-app .
```

---

### 📦 Docker Containers

Containers are isolated running instances of Docker images.

```bash
docker run -p 8000:8000 my-app
```

---

### 📄 Dockerfile

Defines instructions for building custom Docker images.

```dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

### 💾 Docker Volumes

Volumes enable persistent storage independent of container lifecycle.

```bash
docker volume create app_data
```

---

### 🌐 Docker Networks

Networks allow communication between containers.

```bash
docker network create app-network
```

---

## 🧩 Docker Compose

Docker Compose simplifies the management of multi-container applications using a single YAML configuration file.

### Common Use Cases

* Frontend + Backend
* Backend + Database
* Full Stack Applications
* Microservices Architecture
* Development Environments

---

## ⚙️ Docker Compose Example

```yaml
services:

  app:
    build: .
    ports:
      - "8000:8000"

  postgres:
    image: postgres:16

    environment:
      POSTGRES_DB: demo
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: password
```

### Start Application

```bash
docker compose up --build
```

### Stop Application

```bash
docker compose down
```

---

## 🔥 Docker vs Docker Compose

| Feature       | Docker                      | Docker Compose             |
| ------------- | --------------------------- | -------------------------- |
| Purpose       | Single Container Management | Multi-Container Management |
| Configuration | CLI Commands                | YAML Configuration         |
| Networking    | Manual                      | Automatic                  |
| Scalability   | Manual                      | Simplified                 |
| Deployment    | Individual Containers       | Entire Application Stack   |

---

## 🛠 Frequently Used Commands

### Images

```bash
docker images
```

### Build Image

```bash
docker build -t app .
```

### Run Container

```bash
docker run -d -p 8000:8000 app
```

### Running Containers

```bash
docker ps
```

### Stop Container

```bash
docker stop <container-id>
```

### Remove Container

```bash
docker rm <container-id>
```

### Remove Image

```bash
docker rmi <image-id>
```

---

## 📂 Repository Structure

```bash
docker-foundations/
│
├── docker-basics/
├── docker-images/
├── docker-volumes/
├── docker-networking/
├── docker-compose/
├── multi-container/
├── deployment/
└── projects/
```

---

## 🎯 Learning Roadmap

This repository covers:

### Beginner

* Docker Installation
* Docker CLI Basics
* Images & Containers
* Dockerfile Fundamentals

### Intermediate

* Volumes
* Networks
* Multi-stage Builds
* Docker Compose

### Advanced

* Multi-Container Applications
* Container Orchestration Concepts
* CI/CD Integration
* Production Deployment Practices

---

## 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/Apurvbajpai2531/docker-foundations.git
```

Navigate to the project:

```bash
cd docker-foundations
```

Start containers:

```bash
docker compose up --build
```

---

## 📖 Official Documentation

* Docker Documentation → https://docs.docker.com
* Docker Compose Documentation → https://docs.docker.com/compose

---

## 👨‍💻 Author

### Apurv Bajpai

💼 DevOps & Cloud Enthusiast
🚀 Learning Modern Infrastructure & Containerization

GitHub:

https://github.com/Apurvbajpai2531

---

## ⭐ Support

If you found this repository useful:

🌟 Star the Repository
🍴 Fork the Project
📢 Share with Other Developers

---

<div align="center">

### Happy Containerizing! 🐳

</div>
