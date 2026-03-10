import requests

ticket_id = input("Enter ticket ID: ")

url = f"https://loftyoutfits.pythonanywhere.com/ticket/{ticket_id}"

# Sample data to be sent in the PUT request
data = {
    "title": "title-33",
    "content": "title-33"
}

# Send PUT request with the data
response = requests.put(url, json=data)

if response.status_code == 200:
    # If the request was successful (status code 200), you can access the response content
    data = response.json()  # Assuming the response is JSON data
    print(data)
else:
    print("Failed to update data. Status code:", response.status_code)
