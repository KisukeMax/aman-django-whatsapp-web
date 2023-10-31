from django.db import models

#
class WhatsAppMessage(models.Model):
    phone_id = models.CharField(max_length=255)
    profile_name = models.CharField(max_length=255)
    whatsapp_id = models.CharField(max_length=255)
    from_id = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255)
    timestamp = models.CharField(max_length=255)
    text = models.TextField()
    phone_number = models.CharField(max_length=255)
    message_text = models.TextField()
    message_status = models.CharField(max_length=255)