from django.conf import settings
import requests

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

# phoneNumber = "9956929372"
# msg = "hello \n uahuahsh " 
# sendWhatsAppMessage(phoneNumber,msg)
# a36563b3-800a-43ec-ad4a-7043005b488c