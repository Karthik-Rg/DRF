from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Query
from django.core.mail import mail_admins



@receiver(post_save, sender=Query)
def send_mail_admins(sender, instance, created, **kwargs):
    if created:
        mail_admins(instance.subject, instance.content)

