from app import users, stores, orders, payments, promotions

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Registrar local")
        print("3. Crear pedido")
        print("4. Pedidos Pendientes")
        print("5. Pagar pedido")
        print("6. Crear promoción")
        print("7. Ver promociones")
        print("0. Salir")

        choice = input("Seleccione una opción: ")

        match choice:
            case "1":
                users.add_user()
            case "2":
                stores.add_store()
            case "3":
                orders.add_order()
            case "4":
                payments.pay_order()
            case "6":
                promotions.add_promotion()
            case "7":
                promotions.list_promotions()
            case "0":
                print("👋 Hasta luego")
                break
            case _:
                print("❌ Opción inválida")

if __name__ == "__main__":
    menu()
