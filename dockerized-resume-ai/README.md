# 🐳 Dockerized AI Resume Analyzer

A simple AI-powered Resume Analyzer that compares resumes with job descriptions using RoBERTa-based semantic matching.

It extracts text from PDFs, analyzes skills, and shows match score, missing skills, and improvement suggestions.

The whole project is containerized with Docker for easy setup and deployment.

## 🚀 Run (Docker)

```bash
chmod +x run.sh
./run.sh
```

OR manual:

```bash
docker compose up --build
```

Then open:
http://localhost:5000

## 🧠 Tech

Flask, RoBERTa, Transformers, PyMuPDF, Docker

---

Made for learning AI + Docker + NLP.


## 📦 Important Note (Models)

- ❌ `models_cache/` folder is NOT included in this repository (added in `.gitignore`)
- 🚀 This is intentional because model files are large (>100MB limit of GitHub)
- 🧠 The required RoBERTa model will be automatically downloaded from HuggingFace when the project runs for the first time
- ⚠️ Internet connection is required on first run to download the model

If models are not downloaded automatically, run:
```bash
python -c "from transformers import pipeline; pipeline('ner', model='dslim/bert-base-NER')"
