from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador (asegúrate de tener el driver adecuado en tu PATH)
driver = webdriver.Chrome()

# URL del sitio web a raspar
url = 'https://www.amazon.com.mx/robots.txt'

# Acceder a la página web
driver.get(url)

# Esperar un poco a que la página cargue completamente
time.sleep(5)

try:
    # Encontrar el elemento que contiene el precio por su clase
    precio_element = driver.find_element(By.CLASS_NAME, 'a-price')
    precio = precio_element.text
    print(f"Precio: {precio}")
except:
    print("No se pudo obtener el precio.")

# Cerrar el navegador
driver.quit()
