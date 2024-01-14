from django.db.models import Max, OuterRef, Subquery
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
import json
from .functions import *
from django.conf import settings
import requests
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import *
import sys
from datetime import datetime
import time
from urllib.parse import unquote
from django.db.models import Count , Q
import traceback




def upload_parser_media(request):
    try:
        media = request.FILES.get('media')  # Access file data using request.FILES
        upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'uploads', request.data.get("media_type"))

        # Ensure the directory exists
        os.makedirs(upload_dir, exist_ok=True)

        media_path = os.path.join(upload_dir, media.name)
        
        with open(media_path, 'wb') as file:
            file.write(media.read())

        return media_path  # Return the path to the uploaded file
    except Exception as e:
        print(e)
        return None




# class ReactView_rooms(APIView):
#     def get(self, request):
#         # An 'id' is provided, fetch and display the specific item
#         try:
#             unique_phone_numbers = WhatsAppMessage.objects.values('phone_number').distinct().order_by('-timestamp')
#             print(len(unique_phone_numbers))
#             return Response(unique_phone_numbers)
#         except WhatsAppMessage.DoesNotExist:
#             return Response({"error": "Item not found"}, status=404)

#

class ReactView_rooms(APIView):
    def get(self, request):
        try:
            # Get the most recent timestamp for each phone number
            subquery = WhatsAppMessage.objects.filter(
                phone_number=OuterRef('phone_number')
            ).values('phone_number').annotate(
                max_timestamp=Max('timestamp')
            ).values('max_timestamp')
            # recent_messages = subquery.order_by('-max_timestamp')
            # Query to get the most recent messages
            recent_messages = WhatsAppMessage.objects.filter(
                timestamp=Subquery(subquery)
            ).values('profile_name','text', "phone_number", "timestamp", "admin_seen_count")
            message_counts = WhatsAppMessage.objects.values('phone_number').annotate(message_count=Count('id'))
            recent_messages_with_count = []
            admin_unseen_message_counts = WhatsAppMessage.objects.values('phone_number').annotate(admin_unseen_count=Count('id', filter=Q(admin_seen_count=False) | Q(admin_seen_count=0)))


            # Combine the message counts with the recent messages
            recent_messages_with_count = []
            for message in recent_messages:
                phone_number = message['phone_number']
                total_message_count = next((item['message_count'] for item in message_counts if item['phone_number'] == phone_number), 0)
                admin_unseen_count = next((item['admin_unseen_count'] for item in admin_unseen_message_counts if item['phone_number'] == phone_number), 0)
                message['message_count'] = total_message_count
                message['admin_unseen_count'] = admin_unseen_count
                recent_messages_with_count.append(message)


            # print(recent_messages)
             # Encode text and handle non-ASCII characters
            for message in recent_messages:
                message['text'] = message['text'].encode(sys.stdout.encoding, errors='replace').decode()

            # Use the subquery to retrieve the corresponding rows with the most recent timestamps
            # unique_phone_numbers = WhatsAppMessage.objects.filter(
            #     phone_number=OuterRef('phone_number'),
            #     timestamp=OuterRef('timestamp')
            # ).values('phone_number').order_by('-timestamp')

            return Response(recent_messages)
        except WhatsAppMessage.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)

class ReactView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # print(id)
            # An 'id' is provided, fetch and display the specific item
            try:
                items = WhatsAppMessage.objects.filter(phone_number=id).order_by('-timestamp')
                fields = ["phone_id", "whatsapp_id", "from_id", "timestamp", "profile_name", "phone_number", "text","message_text_sent_by", "msg_status_code", "upload_media_path" , "fb_media_id", "msg_status_comment", "admin_seen_count", "message_id"]
                data = [
                    {field: getattr(item, field) for field in fields}
                    for item in items
                ]
                return Response(data)
            except WhatsAppMessage.DoesNotExist:
                return Response({"error": "Item not found"}, status=404)
        else:
            # No 'id' is provided, display all items
            queryset = WhatsAppMessage.objects.all()
            output = [{"profile_name": item.profile_name, "phone_number": item.phone_number} for item in queryset]
            return Response(output)

    # def post(self, request):
    #     serializer = ReactSerializer(data=request.data)
    #     print(serializer)
    #     return Response(serializer.data)

# Create your views here.
def home(request):
    # return HttpResponse("Hellaao Worldasas2")
    return render(request, "business/index.html")

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        # Get data from the request and load it as JSON
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        
        # Extract the data from the JSON
        phone_id = ""
        profile_name = data.get("profile_name", "no name")
        whatsapp_id = ""
        from_id = ""
        timestamp = time.time()
        text = data.get("message_text")
        phone_number = data.get("phone_number")
        message_text = data.get("message_text")
        message_status = "sent"
        msg_sent_by = "DJANGO ADMIN"

        
        # Send the message using your sendWhatsAppMessage function
        res_wp_msg_id = sendWhatsAppMessage(phone_number,message_text)  # Assuming sendWhatsAppMessage returns a message ID
        message_id = res_wp_msg_id
        
        # Create a WhatsAppMessage instance and save it to the database
        WhatsAppMessage.objects.create(
            phone_id=phone_id,
            profile_name=profile_name,
            whatsapp_id=whatsapp_id,
            from_id=from_id,
            message_id=message_id,
            timestamp=timestamp,
            text=text,
            phone_number=phone_number,
            message_text=message_text,
            message_text_sent_by = msg_sent_by,
            msg_status_code = message_status,
            admin_seen_count =  1
        )
        
        # Return a success response or handle any errors as needed
        return HttpResponse("Message sent and saved successfully")
        
    else:
        return JsonResponse({'message': 'Invalid data received.'}, status=200)


@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        # print(request.GET)  # Debugging line to check request.GET contents
        VERIFY_TOKEN = "a36563b3-800a-43ec-ad4a-7043005b488c"
        mode = request.GET.get('hub.mode', '')
        token = request.GET.get('hub.verify_token', '')
        challenge = request.GET.get('hub.challenge', '')
        # sendWhatsAppMessage("9956929372", "get auisas")

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
                token =  settings.WHATSAPP_TOKEN.replace("Bearer ", "")
                # Default primary key field type
                messenger = WhatsApp(token , "128538200341271")
                message_type = messenger.get_message_type(data)
                print(message_type)
                if message_type:
                    if not message_type == "text":
                        print("porocess it")
                        parse_recd_media_msgs(data)
                contacts = data.get("entry", [])[0].get("changes", [])[0].get("value", {}).get("contacts")
                if contacts:
                    process_msg_rec(data)
                else:
                    process_msg_status(data)

            except Exception as e:
                print(e)
                pass
                # Handle exceptions here

        return HttpResponse('success', status=200)



@api_view(['POST'])
def upload_image(request):
    image = request.data.get('image')
    profile_name = request.data.get('profile_name')
    phone_number = request.data.get('phone_number')
    print(image)
    print(request.data)
    
    if not image:
        return Response({'error': 'No image data received'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Define the directory where you want to save the uploaded images within the static folder
    upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'uploads', 'images')

    # Ensure the directory exists
    print(upload_dir)
    os.makedirs(upload_dir, exist_ok=True)

    try:
        image_path = os.path.join(upload_dir, image.name)

        with open(image_path, 'wb') as file:
            file.write(image.read())
        
        send_and_upload_image(image_path,profile_name,phone_number)
        # You can now process the uploaded image, e.g., save the path to a database or perform other operations

        return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def upload_document(request):
    document = request.data.get('document')
    profile_name = request.data.get('profile_name')
    phone_number = request.data.get('phone_number')
    # print(document)
    print(request.data)
    
    if not document:
        return Response({'error': 'No document data received'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Define the directory where you want to save the uploaded documents within the static folder
    upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'uploads', 'document')

    # Ensure the directory exists
    print(upload_dir)
    os.makedirs(upload_dir, exist_ok=True)

    try:
        doc_path = os.path.join(upload_dir, document.name)

        with open(doc_path, 'wb') as file:
            file.write(document.read())
        
        send_and_upload_document(doc_path,profile_name,phone_number)
        # You can now process the uploaded image, e.g., save the path to a database or perform other operations

        return Response({'message': 'document uploaded successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def upload_video(request):
    document = request.data.get('video')
    profile_name = request.data.get('profile_name')
    phone_number = request.data.get('phone_number')
    # print(document)
    print(request.data)
    
    if not document:
        return Response({'error': 'No document data received'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Define the directory where you want to save the uploaded documents within the static folder
    upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'uploads', 'video')

    # Ensure the directory exists
    print(upload_dir)
    os.makedirs(upload_dir, exist_ok=True)

    try:
        doc_path = os.path.join(upload_dir, document.name)

        with open(doc_path, 'wb') as file:
            file.write(document.read())
        
        send_and_upload_video(doc_path,profile_name,phone_number)
        # You can now process the uploaded image, e.g., save the path to a database or perform other operations

        return Response({'message': 'document uploaded successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
def mark_msg_seen_by_admin(request):
    try:
        data = json.loads(request.body)
        mark_msg_seen_by_admin_func(data)
        return  Response({'message': 'msg updated'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def send_rest_template(request):
    try:
        content_type = request.content_type
        print(content_type)
        data = request.POST.dict()
        print(data)
        # data = json.loads(request.body)
        print(request.data)
        if data.get("template_name") ==  "abandoned_checkout":
            if len(data.get("components")) == 4:
                send_abandoned_checkout_template(data)
                return  Response({'message': 'msg updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Please pass all 4 parameters"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if data.get("template_name") ==  "cancelled":
            if len(data.get("components")) == 3:
                document = request.data.get('video')    
                if not document:
                    return Response({'error': 'No document data received'}, status=status.HTTP_400_BAD_REQUEST)
    
                # Define the directory where you want to save the uploaded documents within the static folder
                upload_dir = os.path.join(settings.STATIC_ROOT, 'business', 'uploads', 'video')

                # Ensure the directory exists
                print(upload_dir)
                os.makedirs(upload_dir, exist_ok=True)

                try:
                    doc_path = os.path.join(upload_dir, document.name)

                    with open(doc_path, 'wb') as file:
                        file.write(document.read())
                    
                    send_cancelled_template(doc_path)
                    # You can now process the uploaded image, e.g., save the path to a database or perform other operations

                    return Response({'message': 'document uploaded successfully'}, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'error': str(e), "data" : data}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                Response({'error': "Please pass all 3 parameters"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if data.get("template_name") ==  "business_chat_start_normaltext":
            if len(data.get("components")) == 1:
                send_business_chat_start_normaltext(data)
                return Response({'message': 'msg updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Please pass all  parameters"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if data.get("template_name") ==  "business_start_chat_realtext":
            if len(data.get("components")) == 1:
                send_business_start_chat_realtext(data)
                return Response({'message': 'msg updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Please pass all  parameters"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if data.get("template_name") == "test":
            media_path = upload_parser_media(request)
            if media_path:
                # You can use media_path as needed, e.g., pass it to another function or save it to a database
                return Response({'message': 'document uploaded successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Error uploading media'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    except Exception as e:
        error_traceback = traceback.format_exc()
        return Response({'error': f'{str(e)}\n{error_traceback}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   