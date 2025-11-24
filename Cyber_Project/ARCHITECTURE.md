
# Architecture Notes

- FastAPI backend exposes ingestion and analytics endpoints.
- SQLite for simplicity; swap with Postgres in prod.
- ML: IsolationForest anomaly detector trained on synthetic features.
- Dashboard uses Chart.js and fetches summary API.
- Dockerized for one-command deployment.
