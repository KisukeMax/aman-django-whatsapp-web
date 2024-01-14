# import requests

# # Define the URL of your Django REST API endpoint
# url = 'https://django.casualfootwears.com/wp-send-template-api-for-website/'  # Replace with the actual URL of your API

# # Define the path to the image file you want to upload
# image_file_path = "12.mp4"  # Replace with the actual path to your image file

# # Create a dictionary with the image file and additional data to send as a multipart/form-data request
# data = {"template_name" : "cancelled",
#     'profile_name': 'max',  # Replace with the actual author name
#     'phone_number': '919956929372',  # Replace with the actual place
#     # 'comments': 'A beautiful landscape',  # Replace with the actual comments
#     "components" : [1,2,3]
# }
# files = {'video': (image_file_path, open(image_file_path, 'rb'))}

# # Send a POST request to the API endpoint with the image and additional data
# response = requests.post(url, data=data, files=files)

# # Check the response
# if response.status_code == 200:
#     print('Image uploaded successfully')
#     print(response.json())
# elif response.status_code == 400:
#     print('Bad request - No image data received')
#     print(response.json())
# else:
#     print('Error uploading')
#     print(response.text)



# # import requests

# # # Define the URL of your Django REST API endpoint
# # url = 'https://django.lightshoes.in/update_msg_seen'  # Replace with the actual URL of your API


# # data = {"whatsapp_id": "wamid.HBgMOTE5OTU2OTI5MzcyFQIAERgSMDRCQkM0OTM0NzgyNjE1OEZBAA=="}

# # response = requests.post(url, json=data)

# # # Check the response from the API
# # if response.status_code == 200:
# #     print("Message marked as seen by admin successfully.")
# # else:
# #     print("Error:", response.status_code, response.text)

from heyoo import WhatsApp

# def upload_media(WHATSAPP_TOKEN,file_path):
#     token =  WHATSAPP_TOKEN
#     messenger = WhatsApp(token , "128538200341271")
#     # status_label.config(text=f"Uploading file")
#     try:
#         media_id = messenger.upload_media(
#         media=file_path,
#     )['id']

#         return media_id
#     except:
#         print(f"Error cant upload")
#         return None



WHATSAPP_TOKEN =  "EAAUovSpndZBABO6m0npKSC9M9cGGWwZCD1Rlc1OZAWaiLnvldsq1nOM7TLogU4ZBZCZBZBdZAIFSGKIAWIJesotLXQ88P5yZB5P1fTFrZAZCnodPfXfTusY5iH6Hz7WjBDuzZBmLDvZAdPIyWZAmAZCM1HUD5Ky6fwnBkqJcPlI6GwTJbgyMN6NX95bSNQCFSwZA6vWEQsZBX"
messenger = WhatsApp(WHATSAPP_TOKEN,  "128538200341271")



res = messenger.send_template("business_start_chat_realtext", "9956929372", components=[
    {
            "type": "HEADER",
            "parameters": [
            {
                "type": "text",
                "text": "maax"
    }]
            }
            ]
  
    )
print(res)






# # media_id = upload_media(WHATSAPP_TOKEN,"testvideo.mp4")
# n = messenger.send_template("cancelled", "9956929372", components=[
# {
#   "type": "header",
#   "parameters": [
#     {
#       "type": "video",
#       "video": {
#         "id": 2560395534123713
#       }
#     }
#   ]
# },
# {

#   "type": "BODY",
#   "parameters": [
#     {
#       "type": "text",
#       "text": "COD"
#     },
#     {
#       "type": "text",
#       "text": "https://www.ledshoes.in/led-multicolor-top-lace"
#     },
#     {
#       "type": "text",
#       "text": "https://www.ledshoes.in/"
#     }
#     ]
# }
# ])

# print(n)