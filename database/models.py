from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String)
    ssid = Column(String)
    bssid = Column(String)
    rssi = Column(Float)
    channel = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)