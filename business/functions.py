from django.conf import settings
import requests
from .models import WhatsAppMessage
from heyoo import WhatsApp
import time
import os
from datetime import datetime

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

# def save_whatsapp_message(phoneId, profileName, whatsAppId, fromId, messageId, timestamp, text, phoneNumber, message, message_text_sent_by, msg_status_code, upload_media_path):
def save_whatsapp_message(phoneId=None, profileName=None, whatsAppId=None, fromId=None, messageId=None, timestamp=None, text=None, phoneNumber=None, message=None, message_text_sent_by=None, msg_status_code=None, upload_media_path=None):

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
        upload_media_path = upload_media_path,
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
        recipient_id=phone_number,
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


def send_and_upload_document(file_path, profile_name, phone_number):
    token =  settings.WHATSAPP_TOKEN.replace("Bearer ", "")
    # Default primary key field type
    messenger = WhatsApp(token , "128538200341271")
    # status_label.config(text=f"Uploading file")
    try:
        media_id = messenger.upload_media(media=file_path).get("id")
        wp_msg_id = messenger.send_document(
        document=media_id,
        recipient_id=phone_number,
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


def send_and_upload_video(file_path, profile_name, phone_number):
    token =  settings.WHATSAPP_TOKEN.replace("Bearer ", "")
    # Default primary key field type
    messenger = WhatsApp(token , "128538200341271")
    # status_label.config(text=f"Uploading file")
    try:
        media_id = messenger.upload_media(media=file_path).get("id")
        wp_msg_id = messenger.send_video(
        video=media_id,
        recipient_id=phone_number,
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






def process_msg_rec(data):
    try:
        for entry in data['entry']:
            if 'changes' in entry:
                changes = entry['changes']
                if changes:
                    first_change = changes[0]
                    phoneId = first_change['value']['metadata']['phone_number_id']
                    profileName = first_change['value']['contacts'][0]['profile']['name']
                    whatsAppId = first_change['value']['contacts'][0]['wa_id']
                    if 'messages' in first_change['value']:
                        messages = first_change['value']['messages']
                        if messages:
                            first_message = messages[0]
                            phoneNumber = first_message['from']
                            fromId = first_message['from']
                            messageId = first_message['id']
                            timestamp = first_message['timestamp']
                            text = first_message['text']['body']
                            message_text_sent_by = profileName
                            msg_status_code = "READ"
                            message = f'RE: {text} was received'
                            print("msg sent")
                            # sendWhatsAppMessage(phoneNumber, message)
                            # Save WhatsApp message to the database
                            save_whatsapp_message(
                                phoneId,
                                profileName,
                                whatsAppId,
                                fromId,
                                messageId,
                                timestamp,
                                text,
                                phoneNumber,
                                message,
                                message_text_sent_by,
                                msg_status_code,
                                
                            )
                            
                            print("data saved")
    except Exception as e:
        print(e)
        pass


def process_msg_status(json_data):
    for entry in json_data.get("entry"):
        error_msg = ''
        status_json = entry.get("changes")[0].get("value").get("statuses")[0]
        wp_msg_id = status_json.get("id")
        wp_msg_status = status_json.get("status")
        print(wp_msg_id,wp_msg_status)
        if status_json.get("errors"):
            error_msg = status_json.get("errors")[0].get("error_data").get("details")
            print(error_msg)
        elif wp_msg_status == "read":
            current_datetime = datetime.now()
            date_format = "%m/%d/%Y %I:%M %p"
            error_msg = current_datetime.strftime(date_format)
        
        try:
            message = WhatsAppMessage.objects.get(message_id=wp_msg_id)
            message.msg_status_code = wp_msg_status
            message.msg_status_comment = error_msg
            message.save()

        except Exception as e:
            print(e)
        
    pass


# def parse_recd_media_msgs(data):
#     token =  settings.WHATSAPP_TOKEN.replace("Bearer ", "")
#     messenger = WhatsApp(token , "128538200341271")
#     message_type = messenger.get_message_type(data)
#     upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'dowmloads', 'images')
#     profile_name = messenger.get_name(data)
#     wp_id = messenger.get_mobile(data)
#     message_id = messenger.get_message_id(data)
#     timestamp = messenger.get_message_timestamp(data)


#     if message_type == "location":
#         message_location = messenger.get_location(data)
#         message_latitude = message_location["latitude"]
#         message_longitude = message_location["longitude"]

#     elif message_type == "image":
#         image = messenger.get_image(data)
#         image_id, mime_type = image["id"], image["mime_type"]
#         image_url = messenger.query_media_url(image_id)
#         upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'dowmloads', 'image')
#         os.makedirs(upload_dir, exist_ok=True)
#         image_path = f"{upload_dir}/{image_id}"
#         image_filename = messenger.download_media(image_url, mime_type, str(image_path))
#         print(image_filename)
#         save_whatsapp_message(phoneId= "128538200341271",
#                               profileName=profile_name,
#                               whatsAppId= wp_id,
#                               fromId=  wp_id,
#                               messageId=message_id,
#                               timestamp=timestamp,
#                               text= "",
#                               phoneNumber= wp_id,
#                               message= "",
#                               message_text_sent_by= profile_name,
#                               msg_status_code= "read",
#                               upload_media_path = image_filename
#                               )


#     elif message_type == "video":
#         video = messenger.get_video(data)
#         video_id, mime_type = video["id"], video["mime_type"]
#         video_url = messenger.query_media_url(video_id)
#         upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'dowmloads', 'video')
#         video_path = os.path.join(upload_dir, video_id)
#         print(video_path)
#         video_filename = messenger.download_media(video_url, mime_type, video_path)

#     elif message_type == "audio":
#         audio = messenger.get_audio(data)
#         audio_id, mime_type = audio["id"], audio["mime_type"]
#         audio_url = messenger.query_media_url(audio_id)
#         upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'dowmloads', 'audio')

#         audio_filename = messenger.download_media(audio_url, mime_type)

#     elif message_type == "document":
#         file = messenger.get_document(data)
#         file_id, mime_type = file["id"], file["mime_type"]
#         file_url = messenger.query_media_url(file_id)
#         upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'dowmloads', 'documents')

#         file_filename = messenger.download_media(file_url, mime_type)




def parse_recd_media_msgs(data):
    token = settings.WHATSAPP_TOKEN.replace("Bearer ", "")
    messenger = WhatsApp(token, "128538200341271")
    message_type = messenger.get_message_type(data)
    
    static_root = settings.STATIC_ROOT
    business_downloads = os.path.join(static_root, 'business', 'dowmloads')
    
    upload_dir = None
    filename = None

    profile_name = messenger.get_name(data)
    wp_id = messenger.get_mobile(data)
    message_id = messenger.get_message_id(data)
    timestamp = messenger.get_message_timestamp(data)

    if message_type == "location":
        message_location = messenger.get_location(data)
        message_latitude = message_location["latitude"]
        message_longitude = message_location["longitude"]
    elif message_type == "image":
        image = messenger.get_image(data)
        image_id, mime_type = image["id"], image["mime_type"]
        image_url = messenger.query_media_url(image_id)
        upload_dir = os.path.join(business_downloads, 'image')
        os.makedirs(upload_dir, exist_ok=True)
        filename = messenger.download_media(image_url, mime_type, os.path.join(upload_dir, image_id))
    elif message_type == "video":
        video = messenger.get_video(data)
        video_id, mime_type = video["id"], video["mime_type"]
        video_url = messenger.query_media_url(video_id)
        upload_dir = os.path.join(business_downloads, 'video')
        os.makedirs(upload_dir, exist_ok=True)
        filename = messenger.download_media(video_url, mime_type, os.path.join(upload_dir, video_id))
    elif message_type == "audio":
        audio = messenger.get_audio(data)
        audio_id, mime_type = audio["id"], audio["mime_type"]
        audio_url = messenger.query_media_url(audio_id)
        upload_dir = os.path.join(business_downloads, 'audio')
        os.makedirs(upload_dir, exist_ok=True)
        filename = messenger.download_media(audio_url, mime_type, os.path.join(upload_dir, audio_id))
    elif message_type == "document":
        file = messenger.get_document(data)
        file_id, mime_type = file["id"], file["mime_type"]
        file_url = messenger.query_media_url(file_id)
        upload_dir = os.path.join(business_downloads, 'documents')
        os.makedirs(upload_dir, exist_ok=True)
        filename = messenger.download_media(file_url, mime_type, os.path.join(upload_dir, file_id))

    if upload_dir and filename:
        save_whatsapp_message(phoneId="128538200341271",
                              profileName=profile_name,
                              whatsAppId=wp_id,
                              fromId=wp_id,
                              messageId=message_id,
                              timestamp=timestamp,
                              text="",
                              phoneNumber=wp_id,
                              message="",
                              message_text_sent_by=profile_name,
                              msg_status_code="read",
                              upload_media_path=filename)


def mark_msg_seen_by_admin_func(data):
        msg_id = data.get("whatsapp_id")
        try:
            message = WhatsAppMessage.objects.get(message_id=msg_id)
            message.admin_seen_count = 1
            message.save()

        except Exception as e:
            print(e)


def upload_media_on_wp(file_path):
    token =  settings.WHATSAPP_TOKEN.replace
    messenger = WhatsApp(token , "128538200341271")
    # status_label.config(text=f"Uploading file")
    try:
        media_id = messenger.upload_media(
        media=file_path,
    )['id']

        return media_id
    except:
        print(f"Error cant upload")
        return None


def send_abandoned_checkout_template(data):
    messenger = WhatsApp(settings.WHATSAPP_TOKEN.replace("Bearer ", ""),  "128538200341271")
    res = messenger.send_template("abandoned_checkout", "9956929372", components=[
    {
            "type": "body",
            "parameters": [
            {
                "type": "text",
                "text": data.get("components")[0]
            },
            {
                "type": "text",
                "text": data.get("components")[1]
            },
            {
                "type": "text",
                "text": data.get("components")[2]
            },
            {
                "type": "text",
                "text": data.get("components")[3]
            },
            ]
    }
    ])
    print(res)

def send_cancelled_template(file_path):
    messenger = WhatsApp(settings.WHATSAPP_TOKEN.replace("Bearer ", ""),  "128538200341271")
    res = messenger.send_template("cancelled", "9956929372", components=[
    {
        "type": "header",
        "parameters": [
            {
            "type": "video",
            "video": {
                "id": upload_media_on_wp(file_path)
            }
            }
        ]
    },
    {

        "type": "BODY",
        "parameters": [
            {
            "type": "text",
            "text": "COD"
            },
            {
            "type": "text",
            "text": "https://www.ledshoes.in/led-multicolor-top-lace"
            },
            {
            "type": "text",
            "text": "https://www.ledshoes.in/"
            }
            ]
    }
    ])
    print(res)




def send_send_business_chat_start_normaltext(data):
    messenger = WhatsApp(settings.WHATSAPP_TOKEN.replace("Bearer ", ""),  "128538200341271")
    res = messenger.send_template("send_business_chat_start_normaltext", "9956929372", components=[
    {
            "type": "body",
            "parameters": [
            {
                "type": "text",
                "text": data.get("components")[0]
            },
            ]
    }
    ])
    print(res)