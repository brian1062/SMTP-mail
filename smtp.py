import smtplib # library for smtp protocol
from email.message import EmailMessage
import getpass as gps

# Configurar campos de encabezado del correo electrónico
msg = EmailMessage()
subject= input("Ingrese el asunto del correo: ")
from_mail = input("Ingrese el correo del remitente: ")
to_mail = input("Ingrese el correo del destinatario: ")
msg['Subject'] = subject
msg['From'] = from_mail
msg['To'] = to_mail

# Establecemos el contenido del correo electrónico
msg_content = input("Ingrese el cuerpo del mensaje a enviar: ")
msg.set_content(msg_content)

# Creamos un objeto SMTP y lo conectamos al servidor SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    contrasenia = gps.getpass("Ingrese su contraseña: ")
    smtp.login(from_mail, contrasenia)

    # Envio el correo electrónico
    smtp.send_message(msg)

    # Cierre la conexión con el servidor SMTP
    smtp.quit()