# ---------------------------
# STAGE 1: Builder
# ---------------------------
FROM python:3.12-slim AS builder

WORKDIR /app

# system deps (optional but good practice)
RUN apt-get update && apt-get install -y build-essential

# install dependencies in venv-like layer
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------------------------
# STAGE 2: Runtime
# ---------------------------
FROM python:3.12-slim

WORKDIR /app

# copy installed packages from builder
COPY --from=builder /install /usr/local

# copy project files
COPY . .


ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["python", "app.py"]
