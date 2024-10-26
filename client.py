import base64
import requests

# Path to the image file
image_path = "testingImages\\testing.jpg"

# Read the image file and convert it to Base64
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    base64_image = f"data:image/jpeg;base64,{encoded_string}"  # Adjust MIME type as needed
    # print(base64_image)

# Send the Base64 image to the FastAPI endpoint
response = requests.post("http://127.0.0.1:8000/query/", json={"base64_image": base64_image})

# Print the response from the server
print(response.json())
