
from app import models, schemas
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import func

def create_log(db: Session, item: schemas.LogCreate):
    entry = models.LogEntry(
        src_ip=item.src_ip,
        dest=item.dest,
        method=item.method,
        path=item.path,
        user_agent=item.user_agent
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def get_summary(db: Session):
    total = db.query(models.LogEntry).count()
    by_ip = db.query(models.LogEntry.src_ip, func.count(models.LogEntry.id)).group_by(models.LogEntry.src_ip).limit(10).all()
    return {"total_logs": total, "top_sources": [{ "ip": ip, "count": c } for ip,c in by_ip]}
