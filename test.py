# import requests

# # Define the URL of your Django REST API endpoint
# url = 'https://django.casualfootwears.com/wp-send-template-api-for-website/'  # Replace with the actual URL of your API

# # Define the path to the image file you want to upload
# image_file_path = "22121.mp4"  # Replace with the actual path to your image file

# # Create a dictionary with the image file and additional data to send as a multipart/form-data request
# data = {"template_name" : "business_chat_start_normaltext",
#     'profile_name': 'max',  # Replace with the actual author name
#     'to_number': '918090882360',  # Replace with the actual place
#     # 'comments': 'A beautiful landscape',  # Replace with the actual comments
#     "components" : ["test1", "test21", "test31", "as", "test1", "test21", "test31", "as", "test1", "test21", "test31", "as", "test1", "test21", "test31", "as"],
#     "media_type" :"test"
# }
# files = {'media': (image_file_path, open(image_file_path, 'rb'))}

# # Send a POST request to the API endpoint with the image and additional data
# response = requests.post(url, data=data, files=files)

# with open("404.html", "w", encoding="utf8") as f:
#     f.write(response.text)
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



# # # # import requests

# # # # # Define the URL of your Django REST API endpoint
# # # # url = 'https://django.lightshoes.in/update_msg_seen'  # Replace with the actual URL of your API


# # # # data = {"whatsapp_id": "wamid.HBgMOTE5OTU2OTI5MzcyFQIAERgSMDRCQkM0OTM0NzgyNjE1OEZBAA=="}

# # # # response = requests.post(url, json=data)

# # # # # Check the response from the API
# # # # if response.status_code == 200:
# # # #     print("Message marked as seen by admin successfully.")
# # # # else:
# # # #     print("Error:", response.status_code, response.text)

# # from heyoo import WhatsApp

# # def upload_media(WHATSAPP_TOKEN,file_path):
# #     token =  WHATSAPP_TOKEN
# #     messenger = WhatsApp(token , "128538200341271")
# #     # status_label.config(text=f"Uploading file")
# #     try:
# #         media_id = messenger.upload_media(
# #         media=file_path,
# #     )['id']

# #         return media_id
# #     except:
# #         print(f"Error cant upload")
# #         return None


# # WHATSAPP_TOKEN =  "EAAUovSpndZBABO6m0npKSC9M9cGGWwZCD1Rlc1OZAWaiLnvldsq1nOM7TLogU4ZBZCZBZBdZAIFSGKIAWIJesotLXQ88P5yZB5P1fTFrZAZCnodPfXfTusY5iH6Hz7WjBDuzZBmLDvZAdPIyWZAmAZCM1HUD5Ky6fwnBkqJcPlI6GwTJbgyMN6NX95bSNQCFSwZA6vWEQsZBX"
# # media_id = upload_media(WHATSAPP_TOKEN,r"C:\Users\ASUS\Videos\Recording 2023-12-02 114610.mp4")
# # print(media_id)
# # messenger = WhatsApp(WHATSAPP_TOKEN,  "128538200341271")



# # res = messenger.send_template("busines_start_chat_text", "9956929372", components=[
# #     {
# #                         "type": "HEADER",
# #                         "parameters": [{
# #                             "type": "video",
# #                             "video": {
# #                             "id": media_id
# #                             }}]
# #                             },
# #     {
        
# #             "type": "body",
# #             "parameters": [
# #             {
# #                 "type": "text",
# #                 "text": "maax"
    
# #     },
# #      {
# #             "type": "text",
# #             "text": "COD"
# #             }]
# #             }
# #             ]
  
# #     )
# # print(res.get("messages", [{}])[0].get("message_status"))



# # import requests

# # url = "https://graph.facebook.com/v18.0/120126377855203/message_templates?name=abandoned_checkout"

# # payload = {}
# # headers = {
# #   'Authorization': 'Bearer EAAUovSpndZBABO6m0npKSC9M9cGGWwZCD1Rlc1OZAWaiLnvldsq1nOM7TLogU4ZBZCZBZBdZAIFSGKIAWIJesotLXQ88P5yZB5P1fTFrZAZCnodPfXfTusY5iH6Hz7WjBDuzZBmLDvZAdPIyWZAmAZCM1HUD5Ky6fwnBkqJcPlI6GwTJbgyMN6NX95bSNQCFSwZA6vWEQsZBX',
# #   'Cookie': 'ps_l=0; ps_n=0'
# # }

# # response = requests.request("GET", url, headers=headers, data=payload)

# # print(response.text)



# # # # # # media_id = upload_media(WHATSAPP_TOKEN,"testvideo.mp4")
# # # # # n = messenger.send_template("cancelled", "9956929372", components=[
# # # # # {
# # # # #   "type": "header",
# # # # #   "parameters": [
# # # # #     {
# # # # #       "type": "video",
# # # # #       "video": {
# # # # #         "id": 2560395534123713
# # # # #       }
# # # # #     }
# # # # #   ]
# # # # # },
# # # # # {

# # # # #   "type": "BODY",
# # # # #   "parameters": [
# # # # #     {
# # # # #       "type": "text",
# # # # #       "text": "COD"
# # # # #     },
# # # # #     {
# # # # #       "type": "text",
# # # # #       "text": "https://www.ledshoes.in/led-multicolor-top-lace"
# # # # #     },
# # # # #     {
# # # # #       "type": "text",
# # # # #       "text": "https://www.ledshoes.in/"
# # # # #     }
# # # # #     ]
# # # # # }
# # # # # ])

# # # # # print(n)


import requests
import json

url = "https://django.casualfootwears.com/wp-send-template-api-for-website/"

payload = json.dumps({
  "name": "max",
  "template_name": "business_start_chat_realtext",
  "to_number": "919956929372",
  "from_number": "1212121",
  "components": [
    "est"
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)