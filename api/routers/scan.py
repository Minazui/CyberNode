from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import Scan
from api.auth import verify_api_key
from analysis.anomaly import evaluate_risk

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def receive_scan(data: dict, 
                 db: Session = Depends(get_db),
                 _: str = Depends(verify_api_key)):

    scan = Scan(
        device_id=data.get("device_id"),
        ssid=data.get("ssid"),
        bssid=data.get("bssid"),
        rssi=data.get("rssi"),
        channel=data.get("channel"),
    )

    db.add(scan)
    db.commit()
    db.refresh(scan)

    risk = evaluate_risk(scan)

    return {
        "status": "stored",
        "risk_level": risk
    }

@router.get("/")
def get_scans(db: Session = Depends(get_db)):
    return db.query(Scan).order_by(Scan.timestamp.desc()).limit(100).all()