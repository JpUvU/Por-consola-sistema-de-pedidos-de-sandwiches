from app.storage import load_db, save_db

def pay_order():
    db = load_db()
    order_id = int(input("Id del pedido: "))
    for o in db["orders"]:
        if o["id"] == order_id:
            o["payment_status"] = "pagado"
            o["status"] = "listo para recoger" if not o["delivery"] else "en camino"
            save_db(db)
            print("✅ Pago registrado")
            return
    print("❌ Pedido no encontrado")
