from django.urls import path
from . import views

#
urlpatterns = [
path('', views.home, name = 'home'),
path('d7d01950-d4fb-4190-bef8-2465736065ca', views.whatsAppWebhook, name = 'whatsapp-webhook'),
path('upload_media', views.upload_image, name = 'whatsapp-webhook-media-upload'),
path('upload_media_document', views.upload_document, name = 'whatsapp-webhook-media-upload-document'),
path('update_msg_seen', views.mark_msg_seen_by_admin, name = 'whatsapp-webhook-msg-seen-update'),


]