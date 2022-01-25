import os
import sys
from django.core.mail import send_mail
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

#res = subprocess.run(['echo', message, '|' , 'mailx','-s','"Admin mutalip message"','-r','"likegeeks<likegeeks@example.com>"',self.to], True)
#return res.stdout;
send_mail(
    'OPT Code',
    "Hello World!!!",
    'jokermt<joker1988_88@mail.ru>',
    ['jokemt2357@gmail.com'],
    fail_silently=False,
)
