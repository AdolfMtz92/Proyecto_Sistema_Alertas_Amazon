import smtplib
from email.mime.text import MIMEText

class AlertService:
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        self.alerts.append(alert)

    def notify_user(self, alert):
        message = f"El precio del producto {alert.product.name} ha disminuido. ¡Aprovecha la oferta!"
        send_email(alert.user.email, "Alerta de Precio", message)

def send_email(user_email, subject, message):
    # Datos de autenticación del correo
    sender_email = "correon@gmail.com"
    sender_password = "password"

    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Crear objeto MIMEText para el mensaje
    msg = MIMEText(message)
    msg["From"] = sender_email
    msg["To"] = user_email
    msg["Subject"] = subject

    try:
        # Iniciar conexión SMTP
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(sender_email, sender_password)

        # Enviar correo
        smtp.sendmail(sender_email, user_email, msg.as_string())
        print("Correo enviado exitosamente!")

        # Cerrar conexión SMTP
        smtp.quit()
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
