import smtplib # library for smtp protocol
from email.message import EmailMessage

# Configurar campos de encabezado del correo electrónico
msg = EmailMessage()
msg['Subject'] = 'Envio SMTP'
msg['From'] = 'bgerard1062@gmail.com'
msg['To'] = 'facundo.olivacuneo@unc.edu.ar'

# Establecemos el contenido del correo electrónico
msg.set_content('Hola, buenas tardes estamos probando envio de mensaje smtp, Grupo peaky Coders')

# Creamos un objeto SMTP y lo conectamos al servidor SMTP
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    contrasenia = input("Ingrese Su contraseña")
    smtp.login('bgerard1062@gmail.com', contrasenia)

    # Envio el correo electrónico
    smtp.send_message(msg)

    # Cierre la conexión con el servidor SMTP
    smtp.quit()