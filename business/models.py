from django.db import models
from django.contrib.auth.models import AbstractUser


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
    message_text_sent_by = models.TextField()
    msg_status_code = models.TextField()
    upload_media_path = models.TextField(default=None, null=True)
    fb_media_id = models.TextField(default=None, null=True)
    msg_status_comment = models.TextField(default=None, null=True)
    admin_seen_count = models.IntegerField(default=0, null=True)
    is_template = models.IntegerField(default=0, null=True)
    template_name = models.TextField(default=None, null=True)
    template_json = models.TextField(default=None, null=True)
    wp_template_json = models.TextField(default=None, null=True)



class User(AbstractUser):
    pass

# Add or change the related_name for groups and user_permissions
User.groups.field.related_query_name = 'business_user'
User.user_permissions.field.related_query_name = 'business_user_permissions'