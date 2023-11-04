import requests

# Define the URL of your Django REST API endpoint
url = 'https://django.lightshoes.in/upload_media'  # Replace with the actual URL of your API

# Define the path to the image file you want to upload
image_file_path = r'C:\Users\ASUS\Pictures\Screenshots\Screenshot (68).png'  # Replace with the actual path to your image file

# Create a dictionary with the image file and additional data to send as a multipart/form-data request
data = {
    'author': 'John Doe',  # Replace with the actual author name
    'place': 'Some Place',  # Replace with the actual place
    'comments': 'A beautiful landscape',  # Replace with the actual comments
}
files = {'image': (image_file_path, open(image_file_path, 'rb'))}

# Send a POST request to the API endpoint with the image and additional data
response = requests.post(url, data=data, files=files)

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
