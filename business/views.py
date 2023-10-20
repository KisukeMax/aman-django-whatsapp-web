from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .functions import *
from django.conf import settings
import requests
import os

# Create your views here.
def home(request):
    # return HttpResponse("Hellaao Worldasas2")
    return render(request, "business/index.html")

@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        print(request.GET)  # Debugging line to check request.GET contents
        VERIFY_TOKEN = "a36563b3-800a-43ec-ad4a-7043005b488c"
        mode = request.GET.get('hub.mode', '')
        token = request.GET.get('hub.verify_token', '')
        challenge = request.GET.get('hub.challenge', '')
        sendWhatsAppMessage("9956929372", "get auisas")

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:   
            return HttpResponse('error', status=403)

    if request.method == 'POST':
        print("data recvd")
        # data = json.loads(request.body)
        target_directory = os.path.join(settings.BASE_DIR, 'static', 'your_target_directory')

        # Ensure the target directory exists, creating it if necessary
        os.makedirs(target_directory, exist_ok=True)

        # Define the target file path
        target_file_path = os.path.join(target_directory, 'your_filename.txt')

        # Copy or move the source data to the target file
        with open(target_file_path, 'ab') as target_file:
            target_file.write(request.body)

        data = json.loads(request.body)

    #    if 'object' in data and 'entry' in data:
        if data['object'] == 'whatsapp_business_account':
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

                                    # phoneNumber = "9956929372"
                                    message = f'RE: {text} was received'
                                    print("msg sent")
                                    sendWhatsAppMessage(phoneNumber, message)
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
                                        message
                                    )
                                    print("data saved")
            except Exception as e:
                print(e)
                # Handle exceptions here

        return HttpResponse('success', status=200)
