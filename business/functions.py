from django.conf import settings
import requests
from .models import WhatsAppMessage
from heyoo import WhatsApp
import time

#
def sendWhatsAppMessage(phoneNumber, message ):
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
    try:
        message_id = ans['messages'][0]['id']
        return message_id
    except:
        return "Error in sending"

 # Import the WhatsAppMessage model

def save_whatsapp_message(phoneId, profileName, whatsAppId, fromId, messageId, timestamp, text, phoneNumber, message, message_text_sent_by, msg_status_code):
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
        message_text=message,
        message_text_sent_by = message_text_sent_by,
        msg_status_code = msg_status_code,
    )
    whatsapp_message.save()




def send_and_upload_image(file_path, profile_name, phone_number):
    token =  settings.WHATSAPP_TOKEN.replace("Bearer ", "")
    # Default primary key field type
    messenger = WhatsApp(token , "128538200341271")
    # status_label.config(text=f"Uploading file")
    try:
        media_id = messenger.upload_media(media=file_path).get("id")
        wp_msg_id = messenger.send_image(
        image=media_id,
        recipient_id="919956929372",
        link=False
        ).get("messages")[0].get("id")
        phone_id = ""
        profile_name = profile_name
        timestamp = time.time()
        text = ""
        message_text = ""
        message_status = "sent"
        msg_sent_by = "DJANGO ADMIN"

        whatsapp_message = WhatsAppMessage(phone_id="128538200341271",
        profile_name=profile_name,
        whatsapp_id=phone_number,
        from_id=phone_number,
        message_id=wp_msg_id,
        timestamp=timestamp,
        text=text,
        phone_number=phone_number,
        message_text=message_text,
        message_text_sent_by = msg_sent_by,
        msg_status_code = message_status,
        fb_media_id = media_id,
        upload_media_path = file_path
        )
        whatsapp_message.save()

    except Exception as e:
        print(e)

