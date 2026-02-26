from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal, init_db
from database.models import Scan

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/scan")
def receive_scan(data: dict, db: Session = Depends(get_db)):
    scan = Scan(
        device_id=data.get("device_id"),
        ssid=data.get("ssid"),
        bssid=data.get("bssid"),
        rssi=data.get("rssi"),
        channel=data.get("channel"),
    )
    db.add(scan)
    db.commit()
    return {"status": "ok"}

@app.get("/scans")
def get_scans(db: Session = Depends(get_db)):
    return db.query(Scan).all()