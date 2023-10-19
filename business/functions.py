from django.conf import settings
import requests
from .models import WhatsAppMessage

def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization" : settings.WHATSAPP_TOKEN}
    payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to" : phoneNumber,
            "type": "text",
            "text" : {"body" : message}    
            }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()

 # Import the WhatsAppMessage model

def save_whatsapp_message(phoneId, profileName, whatsAppId, fromId, messageId, timestamp, text, phoneNumber, message):
    # Create a new WhatsAppMessage instance and save it to the database
    whatsapp_message = WhatsAppMessage(
        phone_id=phoneId,
        profile_name=profileName,
        whatsapp_id=whatsAppId,
        from_id=fromId,
        message_id=messageId,
        timestamp=timestamp,
        text=text,
        phone_number=phoneNumber,
        message_content=message,
    )
    whatsapp_message.save()


