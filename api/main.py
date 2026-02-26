from fastapi import FastAPI
from database.db import init_db
from api.routers import scan
import threading
from workers.keepalive import keep_alive
from workers.tasks import periodic_report

app = FastAPI(title="CyberNode")

init_db()

app.include_router(scan.router, prefix="/scan", tags=["Scan"])

@app.get("/")
def root():
    return {"status": "CyberNode running"}

@app.on_event("startup")
def start_keepalive():
    thread = threading.Thread(target=keep_alive, daemon=True)
    thread.start()

@app.on_event("startup")
def start_reporter():
    thread = threading.Thread(target=periodic_report, daemon=True)
    thread.start()