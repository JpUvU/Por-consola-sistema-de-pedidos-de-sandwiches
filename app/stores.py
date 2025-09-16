from app.storage import load_db, save_db, next_id

def add_store():
    name = input("Nombre del local: ")
    owner = input("Dueño: ")
    address = input("Dirección: ")
    has_delivery = input("¿Ofrece delivery? (s/n): ").lower() == "s"

    db = load_db()
    new_id = next_id(db["stores"])
    store = {"id": new_id, 
             "name": name, 
             "owner": owner, 
             "address": address, 
             "has_delivery": has_delivery}
    
    db["stores"].append(store)
    save_db(db)
    print(f"✅ Local creado con id {new_id}")
