from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from functions import *



# Create your views here.

# Create your views here.
def home(request):
    # return HttpResponse("Hellaao Worldasas2")
    return render(request, "business/index.html")

@csrf_exempt
def whatsappWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN ="a36563b3-800a-43ec-ad4a-7043005b488c"
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify.token']
        challenge = request.GET['hub.challenge']

        if mode == 'suscribe' and token ==  VERIFY_TOKEN:
            return HttpResponse(challenge,status = 200)
        else:
            return HttpResponse('error',ststus =403)
        

    if request.method == 'POST':
        data = json.loads(request.body)

        return HttpResponse('success',status=200)