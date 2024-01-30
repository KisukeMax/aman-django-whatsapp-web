# import requests

# def send_location_template(access_token, recipient_id):
#     api_endpoint = f'https://graph.facebook.com/v15.0/me/messages?access_token={access_token}'

#     location_template = {
#         "recipient": {"id": recipient_id},
#         "message": {
#             "attachment": {
#                 "type": "template",
#                 "payload": {
#                     "template_type": "business_start_chat_location",
#                     "elements": [
#                         {
#                             "type": "HEADER",
#                             "format": "LOCATION"
#                         },
#                         {
#                             "type": "BODY",
#                             "text": "Hi,\n\nPlease check the attachment for your reference\n\nTeam {{1}}",
#                             "example": {
#                                 "body_text": [["LEDSHOES"]]
#                             }
#                         },
#                         {
#                             "type": "FOOTER",
#                             "text": "Please reply with \"STOP\" to unsubscribe"
#                         },
#                         {
#                             "type": "BUTTONS",
#                             "buttons": [
#                                 {
#                                     "type": "URL",
#                                     "text": "Follow Instagram",
#                                     "url": "https://www.instagram.com/ledshoes.in/"
#                                 },
#                                 {
#                                     "type": "QUICK_REPLY",
#                                     "text": "Chat Support"
#                                 }
#                             ]
#                         }
#                     ]
#                 }
#             }
#         }
#     }

#     response = requests.post(api_endpoint, json=location_template)
#     print(response.json())

# # Replace with your access token and recipient ID
# access_token = 'EAAUovSpndZBABO6m0npKSC9M9cGGWwZCD1Rlc1OZAWaiLnvldsq1nOM7TLogU4ZBZCZBZBdZAIFSGKIAWIJesotLXQ88P5yZB5P1fTFrZAZCnodPfXfTusY5iH6Hz7WjBDuzZBmLDvZAdPIyWZAmAZCM1HUD5Ky6fwnBkqJcPlI6GwTJbgyMN6NX95bSNQCFSwZA6vWEQsZBX'
# recipient_id = '919956929372'

# # send_location_template(access_token, recipient_id)



# import requests
# import json

# url = "https://django.casualfootwears.com/wp-send-template-api-for-website/"

# payload = {'name': 'max',
# 'template_name': 'business_chat_start_normaltext',
# 'media_type': 'jg',
# 'to_number': '9956929372',
# 'components': ["est", 'ash']}

# headers = {
# 'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
