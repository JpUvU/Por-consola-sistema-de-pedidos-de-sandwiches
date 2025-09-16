import os
import json
from app import main

# Ruta del archivo de base de datos
DB_FILE = os.path.join("data", "database.json")

def init_db():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB_FILE) or os.path.getsize(DB_FILE) == 0:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump({"users": [], "stores": [], "orders": [], "promotions": []}, f, indent=4)

if __name__ == "__main__":
    init_db()
    main.menu()
