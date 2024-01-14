import requests

url = "https://django.casualfootwears.com/wp-send-template-api-for-website/"
payload = {'template_name': 'test', 'media_type': 'test'}

files = {
    'media': ('Screenshot 2023-07-16 210502.png', open('Screenshot 2023-07-16 210502.png', 'rb'), 'image/png')
}

response = requests.post(url, data=payload, files=files)

print(response.text)
