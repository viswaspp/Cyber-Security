
from fastapi import FastAPI, Request, HTTPException
from app import crud, schemas
from app.db import get_db_session
from app.models import Base, engine
from fastapi.responses import FileResponse, HTMLResponse
import os

app = FastAPI(title="Advanced Cybersecurity Platform")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/ingest/log")
async def ingest_log(item: schemas.LogCreate):
    db = get_db_session()
    try:
        entry = crud.create_log(db, item)
        return {"status":"ok","id": entry.id}
    finally:
        db.close()

@app.get("/analytics/summary")
def summary():
    db = get_db_session()
    try:
        s = crud.get_summary(db)
        return s
    finally:
        db.close()

@app.get("/static/{path:path}")
def static(path: str):
    file_path = os.path.join("web", path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail="Not found")
