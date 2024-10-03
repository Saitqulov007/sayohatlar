from django.core.management.base import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Send CI notification'

    def handle(self, *args, **options):
        send_mail('Test mail', 'this is a test email', 'aslbeksaitqulov0124@gmail.com',
                  ['aslbeksaitqulov0124@gmail.com'], fail_silently=False)
        self.stdout.write(self.style.SUCCESS("Email jonatildi"))
