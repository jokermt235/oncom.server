import smtplib, ssl
from email.message import EmailMessage
from django.conf import settings

class Sender:
   def send(message):
        pass

class EmailSender(Sender):
    def __init__(self, to):
        self.to = to
    #Sends an email to client with the specific message
    def send(self, message) :    
        port = settings.EMAIL_PORT  # For SSL
        password = settings.EMAIL_PASSWORD
        context = ssl.create_default_context()

        msg = EmailMessage()
        msg['Subject'] = 'Код подтвеждения личности'
        msg['From'] = settings.EMAIL_LOGIN
        msg['To'] = self.to

        msg.set_content(message)

        with smtplib.SMTP_SSL(settings.EMAIL_SMTP, port, context=context) as server:
            server.login(settings.EMAIL_LOGIN, password)
            return server.send_message(msg)
