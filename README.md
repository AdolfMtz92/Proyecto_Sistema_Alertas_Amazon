"""
Sistema de Alertas de Amazon

Este script permite a los usuarios agregar productos y definir alertas de precios para recibir notificaciones cuando los productos caen por debajo del umbral de precio.

Requiere las siguientes clases y módulos:
<<<<<<< HEAD
- `alert_service.py`: Define la clase `AlertService` que maneja las alertas y notificaciones por correo electrónico. En los métodos `send_email` de esta clase, asegúrate de especificar los datos de autenticación de la cuenta desde la cual se enviarán los correos de alerta. **Debes usar una cuenta de correo electrónico de GMAIL**.
- `alert.py`: Contiene la clase `Alert` que representa una alerta con información sobre el usuario, el producto y el umbral de precio.
- `amazon_api.py`: Contiene la clase `AmazonAPI` que interactúa con la API de Amazon para obtener precios de productos.
- `decorators.py`: Proporciona un decorador para medir el tiempo de ejecución de funciones.
- `product.py`: Define la clase `Product` que representa un producto y su información.
- `user.py`: Define la clase `User` que almacena los datos del usuario.
- `main.py`: El script principal donde se ejecuta la lógica principal del programa.

"""

## Instrucciones de Uso:
    - Ejecute este script y siga las instrucciones en la consola para agregar productos y alertas, y verificar alertas existentes.

## Amazon Alert System

Amazon Alert System es una aplicación que te permite rastrear el precio de productos en Amazon y recibir alertas por correo electrónico cuando el precio de un producto baja por debajo de un umbral específico.

Instrucciones de Uso:
    - Ejecute este script y siga las instrucciones en la consola para agregar productos y alertas, y verificar alertas existentes.

"""


# Amazon Alert System

El Amazon Alert System es una aplicación que te permite rastrear el precio de productos en Amazon y recibir alertas por correo electrónico cuando el precio de un producto baja por debajo de un umbral específico.

## Requisitos

- Python 3.6 o superior
- Bibliotecas requeridas (instalables mediante `pip`):
  - `beautifulsoup4`
  - `smtplib`
  - `requests`

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/AdolfMtz92/Proyecto_Sistema_Alertas_Amazon
   cd Proyecto_Amazon_Alert_Tracker```

## Uso

1. Dirigete a la ruta donde descargaste el repositorio:

cd Proyecto_Amazon_Alert_Tracker

2. Ejecuta el script principal:

python main.py

3. Sigue las instrucciones en la consola para agregar productos y definir alertas. El sistema consultará automáticamente los precios y enviará alertas por correo electrónico cuando sea necesario.

## Estructura del Código

El código se organiza en varios módulos para una mayor claridad y reutilización:

- `alert_service.py`: Define la clase `AlertService` que maneja las alertas y notificaciones por correo electrónico.
- `alert.py`: Contiene la clase `Alert` que representa una alerta con información sobre el usuario, el producto y el umbral de precio.
- `amazon_api.py`: Contiene la clase `AmazonAPI` que interactúa con la API de Amazon para obtener precios de productos.
- `decorators.py`: Proporciona un decorador para medir el tiempo de ejecución de funciones.
- `product.py`: Define la clase `Product` que representa un producto y su información.
- `user.py`: Define la clase `User` que almacena los datos del usuario.
- `main.py`: El script principal donde se ejecuta la lógica principal del programa.

## Funcionamiento

1. Abre una terminal y navega hasta la carpeta del proyecto:

   ```bash
   cd ruta/a/tu/carpeta/amazon-alert-system
   ```
2. Ejecuta el archivo principal:

	python .\main.py

3. El programa mostrará un menú de opciones donde puedes realizar diversas acciones:

Opción 1: Agregar producto y alerta:

Ingresa el nombre del producto.
Pega la URL del producto en Amazon.
Define el umbral de precio deseado.
Proporciona tu nombre para la notificación.
Ingresa tu correo electrónico para recibir alertas.

Opción 2: Verificar alertas:

Verifica las alertas establecidas.
Si el precio del producto está dentro del umbral, se enviará una notificación por correo electrónico.
Si el precio no cumple con la condición, se mostrará un mensaje correspondiente.

Opción 3: Salir:

Selecciona esta opción para salir del programa.
Ten en cuenta que si estableces una nueva alerta para el mismo producto, el programa mostrará tanto la alerta anterior como la nueva.