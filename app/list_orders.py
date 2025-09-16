from app.storage import load_db, save_db



def list_promotions():
    db = load_db()
    if not db["promotions"]:
        print("⚠️ No hay promociones registradas")
    else:
        for p in db["promotions"]:
            print(f"({p['id']}) {p['description']} - {p['discount']}% off")