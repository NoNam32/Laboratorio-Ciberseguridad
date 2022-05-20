from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def correo(remitente, destinatario, titulo, mensaje, contra):
    msg = MIMEMultipart()
    message = mensaje

    password = contra
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = titulo

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print ("successfully sent email to %s:" % (msg['To']))

remitente = str(input('Escribe tu correo: '))
contra = str(input('Escribe la contraseña de tu correo: '))
destinatario = str(input('Escribe el correo al que deseas enviar el mensaje: '))
titulo = str(input('Escribe el titulo: '))
mensaje = str(input('Escribe el mensaje a enviar: '))
correo(remitente, destinatario, titulo, mensaje, contra)
