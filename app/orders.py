from app.storage import load_db, save_db, next_id
from datetime import datetime, timedelta

def add_order():
    db = load_db()

    try:
        user_id = int(input("Id del usuario: "))
        store_id = int(input("Id del local: "))

        items = []
        while True:
            name = input("Nombre del producto: ")
            price = float(input("Precio: "))
            qty = int(input("Cantidad: "))

            if qty <= 0 or price <= 0:
                print("⚠️ La cantidad y el precio deben ser mayores que 0")
                continue

            items.append({"name": name, "price": price, "qty": qty})
            
            cont = input("¿Agregar otro producto? (s/n): ")
            if cont.lower() != "s":
                break

        if not items:
            print("❌ No se agregó ningún producto, pedido cancelado.")
            return

        delivery = input("¿Con delivery? (s/n): ").lower() == "s"
        total = sum(i["price"] * i["qty"] for i in items)

        new_id = next_id(db["orders"])
        pickup_time = (datetime.now() + timedelta(minutes=15)).strftime("%H:%M")

        # Crear pedido solo si todo fue válido
        order = {
            "id": new_id,
            "user_id": user_id,
            "store_id": store_id,
            "items": items,
            "total": total,
            "delivery": delivery,
            "pickup_time": pickup_time,
            "status": "pendiente",
            "payment_status": "no pagado"
        }

        db["orders"].append(order)
        save_db(db)
        print(f"✅ Pedido creado con id {new_id}, recoger a las {pickup_time}")

    except ValueError:
        print("❌ Dato inválido: se esperaba un número.")
    except KeyboardInterrupt:
        print("\n❌ Operación cancelada por el usuario.")
    except Exception as e:
        print(f"🚨 Error inesperado: {e}")

