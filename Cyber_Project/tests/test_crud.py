
from app.db import init_db, get_db_session
from app import crud, schemas
def test_create_and_summary(tmp_path, monkeypatch):
    # use temporary sqlite
    import os
    dbfile = tmp_path/"app.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{dbfile}")
    init_db()
    db = get_db_session()
    item = schemas.LogCreate(src_ip="1.2.3.4", path="/test", user_agent="u")
    crud.create_log(db, item)
    s = crud.get_summary(db)
    assert s["total_logs"]==1
