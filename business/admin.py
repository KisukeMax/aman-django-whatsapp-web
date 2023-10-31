from django.contrib import admin

# Register your models here.
from .models import WhatsAppMessage
# from .models import Room

admin.site.register(WhatsAppMessage)