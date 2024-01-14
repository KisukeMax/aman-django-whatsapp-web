# import requests
# from requests_toolbelt.multipart.encoder import MultipartEncoder

# # Define the URL of your Django REST API endpoint
# url = 'https://django.casualfootwears.com/wp-send-template-api-for-website/'  # Replace with the actual URL of your API

# # Define the path to the image file you want to upload
# image_file_path = "Screenshot 2023-07-16 210502.png"  # Replace with the actual path to your image file

# # Create a dictionary with the additional data to send as a multipart/form-data request
# data = {
#     "template_name": "test",
#     'profile_name': 'max',  # Replace with the actual author name
#     'phone_number': '919956929372',  # Replace with the actual phone number
#     "media_type": "test",
#     "components": [1, 2, 3],
# }

# # Create a MultipartEncoder object for the files and data
# multipart_data = MultipartEncoder(
#     fields={'media': (image_file_path, open(image_file_path, 'rb'))},
#     boundary='your_boundary_here',  # Use a unique boundary
# )

# # Set the Content-Type header to include the boundary
# headers = {'Content-Type': multipart_data.content_type}

# # Send a POST request to the API endpoint with the image and additional data
# response = requests.post(url, data=data, headers=headers, files={'media': (image_file_path, open(image_file_path, 'rb'))})

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
