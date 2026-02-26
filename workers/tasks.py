import requests
import os
import time
from database.db import SessionLocal
from database.models import Scan

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

def periodic_report():
    while True:
        db = SessionLocal()
        total_scans = db.query(Scan).count()
        db.close()

        message = f"""
📡 CyberNode Status Report

Total scans received: {total_scans}
System status: ONLINE
Server: Running on Render
        """

        send_telegram_message(message)

        time.sleep(600)  # cada 10 minutos

def log_event(message: str):
    print(f"[CYBERNODE EVENT] {message}")   