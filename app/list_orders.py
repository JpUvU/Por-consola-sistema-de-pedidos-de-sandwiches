from app.storage import load_db, save_db


def list_promotions():
    db = load_db()
    if not db["orders"]:
        print("⚠️ No hay ordenes pendientes")
    else:
        for p in db["orders"]:
            if p['status'] == "pendiente":
                print(f"ID Pedido: ({p['id']}) - Tienda ID: {p['store_id']} - {p['items']}% off  -  {p['total']} - Delivery: {p['delivery']} - {p['payment_status']}")