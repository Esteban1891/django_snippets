from celery import shared_task
from time import sleep
from django.core.mail import EmailMessage

@shared_task
def send_email_task(subject, body, dest):
    email_message = EmailMessage(
        subject = subject,
        body= body,
        to=[dest],
    )
    email_message.send()
    return None

@shared_task
def sleepy(duration):
    sleep(duration)
    return None