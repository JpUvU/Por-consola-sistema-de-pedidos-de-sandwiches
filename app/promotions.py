from app.storage import load_db, save_db, next_id

def add_promotion():
    db = load_db()
    desc = input("Descripción de la promoción: ")
    discount = float(input("Descuento (%): "))
    new_id = next_id(db["promotions"])
    promo = {"id": new_id, "description": desc, "discount": discount}
    db["promotions"].append(promo)
    save_db(db)
    print(f"✅ Promoción creada con id {new_id}")

def list_promotions():
    db = load_db()
    if not db["promotions"]:
        print("⚠️ No hay promociones registradas")
    else:
        for p in db["promotions"]:
            print(f"({p['id']}) {p['description']} - {p['discount']}% off")
