from django.core.mail import send_mail
class Sender:
   def send(message):
        pass

class EmailSender(Sender):
    def __init__(self, to):
        self.to = to
    def send(self, message) :
        self.message = message
        #res = subprocess.run(['echo', message, '|' , 'mailx','-s','"Admin mutalip message"','-r','"likegeeks<likegeeks@example.com>"',self.to], True)
        #return res.stdout;
        return send_mail(
            'OPT Code',
            message,
            'likegeeks<likegeeks@example.com>',
            [self.to],
            fail_silently=False,
        )
        
