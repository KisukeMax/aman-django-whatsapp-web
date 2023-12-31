# import requests

# # Define the URL of your Django REST API endpoint
# url = 'https://django.lightshoes.in/upload_media_video'  # Replace with the actual URL of your API

# # Define the path to the image file you want to upload
# image_file_path = r'C:\Users\ASUS\Videos\Captures\record screen windows 11 - Google Search - Google Chrome 2023-02-11 23-21-55.mp4'  # Replace with the actual path to your image file

# # Create a dictionary with the image file and additional data to send as a multipart/form-data request
# data = {
#     'profile_name': 'max',  # Replace with the actual author name
#     'phone_number': '919956929372',  # Replace with the actual place
#     # 'comments': 'A beautiful landscape',  # Replace with the actual comments
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
#     print('Error uploading image')
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
WHATSAPP_TOKEN =  "EAAUovSpndZBABO6m0npKSC9M9cGGWwZCD1Rlc1OZAWaiLnvldsq1nOM7TLogU4ZBZCZBZBdZAIFSGKIAWIJesotLXQ88P5yZB5P1fTFrZAZCnodPfXfTusY5iH6Hz7WjBDuzZBmLDvZAdPIyWZAmAZCM1HUD5Ky6fwnBkqJcPlI6GwTJbgyMN6NX95bSNQCFSwZA6vWEQsZBX"
messenger = WhatsApp(WHATSAPP_TOKEN,  "128538200341271")
n = messenger.send_template("abandoned_checkout", "9956929372", components=[
 {
        "type": "body",
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
          },
          {
            "type": "text",
            "text": "LEDSHOES"
          },
          ]
 }
])

print(n)