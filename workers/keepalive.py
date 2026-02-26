import requests
import time
import os

BACKEND_URL = os.getenv("SELF_URL")  # https://cybernode.onrender.com

def keep_alive():
    while True:
        try:
            r = requests.get(f"{BACKEND_URL}/scan/")
            print("Ping:", r.status_code)
        except Exception as e:
            print("Ping error:", e)

        time.sleep(300)  # 5 minutos