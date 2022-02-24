import smtplib, ssl
from email.message import EmailMessage

class Sender:
   def send(message):
        pass

class EmailSender(Sender):
    def __init__(self, to):
        self.to = to
    def send(self, message) :
        port = 465  # For SSL
        password = 'Jkpro2357FT'
        context = ssl.create_default_context()

        msg = EmailMessage()
        msg['Subject'] = 'Код подтвеждения для входа в систему'
        msg['From'] = 'foresdata.t@gmail.com'
        msg['To'] = self.to

        msg.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("foresdata.t@gmail.com", password)
            return server.send_message(msg)

        """self.message = message
        #res = subprocess.run(['echo', message, '|' , 'mailx','-s','"Admin mutalip message"','-r','"likegeeks<likegeeks@example.com>"',self.to], True)
        #return res.stdout;
        return send_mail(
            'OPT Code',
            message,
            'likegeeks<likegeeks@example.com>',
            [self.to],
            fail_silently=False,
        )"""        
