import pytest

from amazon_api import AmazonAPI
from alert import Alert
from alert_service import AlertService
from decorators import measure_time
from product import Product
from user import User

# Crear una instancia de AlertService fuera de la función main
alert_service = AlertService()
amazon_api = AmazonAPI()  # Declarar amazon_api aquí como global


def main():
    """
    Función principal que maneja el flujo del programa.
    """
    print("Bienvenido al sistema de alertas de Amazon")

    while True:
        print("\nMenú:")
        print("1. Agregar producto y alerta")
        print("2. Verificar alertas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto_y_alerta()
        elif opcion == "2":
            verificar_alertas()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


@measure_time
def agregar_producto_y_alerta():
    """
    Agrega un producto y una alerta al sistema.
    """
    nombre_producto = input("Ingrese el nombre del producto: ")
    url_producto = input("Ingrese la URL del producto en Amazon: ")
    umbral_precio = float(input("Ingrese el umbral de precio: "))

    product = Product(nombre_producto, url_producto)
    user = User(input("Ingrese su nombre: "), input("Ingrese su correo electrónico: "))
    alert = Alert(user, product, umbral_precio)

    alert_service.add_alert(alert)
    print("Producto y alerta agregados exitosamente.")


@measure_time
def verificar_alertas():
    """
    Verifica las alertas y notifica a los usuarios si se cumple la condición de umbral.
    """
    print("\nVerificando alertas...")
    for alert in alert_service.alerts:
        product_price = amazon_api.get_product_price(alert.product.url)
        if product_price is not None:
            alert.product.current_price = product_price
            if product_price <= alert.price_threshold:
                print(f"Alerta para {alert.user.name}: El Producto {alert.product.name} está por debajo del umbral de precio.")
                alert_service.notify_user(alert)
            else:
                print(f"No se cumple la condición de umbral para {alert.product.name}.")
        else:
            print(f"No se pudo obtener el precio para {alert.product.name}.")


if __name__ == "__main__":
    main()
