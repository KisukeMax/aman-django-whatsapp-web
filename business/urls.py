from django.urls import path
from . import views

#
urlpatterns = [
path('', views.home, name = 'home'),
path('d7d01950-d4fb-4190-bef8-2465736065ca', views.whatsAppWebhook, name = 'whatsapp-webhook'),
path('upload_media', views.upload_image, name = 'whatsapp-webhook-media-upload'),

]