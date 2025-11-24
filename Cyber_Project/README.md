
# Advanced Cybersecurity Platform (10/10 Project)

**What's included**
- FastAPI backend (API) for ingesting honeypot logs and serving analytics
- Simple ML-based anomaly detector (trained on synthetic data)
- SQLite database + Alembic migrations (lightweight)
- Web dashboard (HTML + Chart.js) to visualize events and alerts
- Dockerfile + docker-compose for easy deployment
- Unit tests and sample data
- Clear runbook and architecture notes

## Run locally (quick)
1. Create venv: `python3 -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Initialize DB and train model: `python manage.py init && python manage.py train_model`
4. Run server: `uvicorn app.main:app --reload`
5. Open dashboard: `http://localhost:8000/static/dashboard.html`

## Run with Docker
`docker-compose up --build`

## Structure
- app/             -> backend FastAPI application
- ml/              -> ML model training & detector
- web/             -> dashboard static files
- scripts/         -> utility scripts (init DB, seed data)
- docker-compose.yml, Dockerfile
- tests/           -> unit tests

