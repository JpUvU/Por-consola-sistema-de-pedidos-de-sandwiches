import json
import os
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent.parent / "data" / "database.json"

def ensure_db():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DB_FILE.exists():
        initial = {"users": [], 
                   "stores": [], 
                   "orders": [], 
                   "promotions": []}
        save_db(initial)

def load_db():
    ensure_db()
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def next_id(items: list):
    if not items:
        return 1
    return max(i["id"] for i in items) + 1
