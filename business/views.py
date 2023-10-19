from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .functions import *
from django.conf import settings
import requests
import os
from django.conf import settings




# Create your views here.

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
        # data = json.loads(request.body)
        target_directory = os.path.join(settings.BASE_DIR, 'static', 'your_target_directory')

        # Ensure the target directory exists, creating it if necessary
        os.makedirs(target_directory, exist_ok=True)

        # Define the target file path
        target_file_path = os.path.join(target_directory, 'your_filename.txt')

        # Copy or move the source data to the target file
        with open(target_file_path, 'wb') as target_file:
            target_file.write(request.body)

        sendWhatsAppMessage("9956929372", "aushu")
        # with open("business/test.txt" , "w" , encoding="utf8") as f:
        #     f.write(request.body)
        # sendWhatsAppMessage("9956929372", data_str = str(request.body, 'utf-8'))

        return HttpResponse('success', status=200)
