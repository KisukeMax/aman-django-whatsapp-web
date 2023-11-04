import requests

# Define the URL of your Django REST API endpoint
url = 'https://django.lightshoes.in/upload_media'  # Replace with the actual URL of your API

# Define the path to the image file you want to upload
image_file_path = r'C:\Users\ASUS\Pictures\Screenshots\Screenshot (68).png'  # Replace with the actual path to your image file

# Create a dictionary with the image file to send as a multipart/form-data request
files = {'image': open(image_file_path, 'rb')}

# Send a POST request to the API endpoint with the image file
response = requests.post(url, files=files)

# Check the response
if response.status_code == 200:
    print('Image uploaded successfully')
    print(response.json())
elif response.status_code == 400:
    print('Bad request - No image data received')
    print(response.json())
else:
    print('Error uploading image')
    print(response.text)
