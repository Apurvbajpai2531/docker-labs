# GST Billing System

A Django-based GST Billing and Invoice Management System with Docker support.

## Features

* GST invoice generation
* Inventory management
* Automatic tax calculation
* Bill printing
* Simple and lightweight UI

## Tech Stack

* Python
* Django
* Docker
* Docker Compose
* SQLite

## Run with Docker

```bash
docker compose up --build
```

Open:

```text
http://localhost:8000
```

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Author

Apurv Bajpai
