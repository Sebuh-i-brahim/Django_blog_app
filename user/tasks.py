from celery import shared_task

from time import sleep

from django.core.mail import send_mail

@shared_task
def sleepy(second):
	sleep(second)
	return None


@shared_task
def send_email(data):
	sleepy(5)
	send_mail(data['header'], data['body'], data['sender'], data['recivers'])
	return None
