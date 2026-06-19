
# Stage 1: Builder
# --------------------------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies for ML libs
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install dependencies in isolated folder
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# --------------------------
# Stage 2: Runtime
# --------------------------
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy project files
COPY . .

# Create folders for uploads
RUN mkdir -p uploads models_cache

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV TRANSFORMERS_CACHE=/app/models_cache

EXPOSE 5000

CMD ["python", "app.py"]
