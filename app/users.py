from app.storage import load_db, save_db, next_id

def add_user():
    name = input("Nombre del usuario: ")
    email = input("Email: ")
    phone = input("Teléfono: ")
    address = input("Dirección: ")

    db = load_db()
    new_id = next_id(db["users"])
    user = {"id": new_id, 
            "name": name, 
            "email": email, 
            "phone": phone, 
            "address": address}
    
    db["users"].append(user)
    save_db(db)
    print(f"✅ Usuario creado con id {new_id}")
