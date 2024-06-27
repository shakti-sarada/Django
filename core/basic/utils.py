from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client():
    subject = "Email Server Test"
    message = "Django server email test."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["shaktisahoo65@gmail.com"]

    send_mail(subject,message,from_email,recipient_list)
