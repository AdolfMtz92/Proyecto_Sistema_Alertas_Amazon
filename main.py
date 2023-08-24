from alert_service import AlertService
from product import Product
from user import User
from alert import Alert
from amazon_api import AmazonAPI
from decorators import measure_time

# Crear una instancia de AlertService fuera de la función main
alert_service = AlertService()
amazon_api = AmazonAPI()  # Declarar amazon_api aquí como global

def main():
    # Crear productos
    product1 = Product("Product 1", "https://www.amazon.com.mx/SAMSUNG-Galaxy-A04-4GB_64GB-Blanco/dp/B0BJN6WRG9")
    product2 = Product("Product 2", "https://www.amazon.com.mx/SAMSUNG-Galaxy-A04-4GB_64GB-Blanco/dp/B0BJN6WRG9")

    # Crear usuarios
    user1 = User("Adolfo", "agorjonmtz@hotmail.com")
    user2 = User("Adolfo", "agorjonmtz@hotmail.com")

    # Crear alertas
    alert1 = Alert(user1, product1, 12000)
    alert2 = Alert(user2, product2, 600)

    # Agregar alertas al servicio
    alert_service.add_alert(alert1)
    alert_service.add_alert(alert2)

    # Consultar precios y verificar alertas

    process_alerts()

@measure_time
def process_alerts():
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
