from fastapi import FastAPI
from database.db import init_db
from api.routers import scan

app = FastAPI(title="CyberNode")

init_db()

app.include_router(scan.router, prefix="/scan", tags=["Scan"])

@app.get("/")
def root():
    return {"status": "CyberNode running"}