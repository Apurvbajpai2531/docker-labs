#!/bin/bash

# Simple error handling
set -e

echo "Clean everything..."

docker compose down

echo "Building the project with Docker Compose..."

docker compose up --build

echo "Done. Application should be running at http://localhost:5000"
