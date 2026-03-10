import requests

url = "https://loftyoutfits.pythonanywhere.com/"


# Sample data to be sent in the POST request
data = {
    "title": "title-4",
    "content": "title-4"
}

# Send POST request with the data
response = requests.post(url, json=data)

if response.status_code == 201:
    data = response.json()  # Assuming the response is JSON data
    print(data)
else:
    print("Failed to fetch data. Status code:", response.status_code)