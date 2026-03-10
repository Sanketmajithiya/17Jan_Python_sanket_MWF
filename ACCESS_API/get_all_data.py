import requests

url = "https://loftyoutfits.pythonanywhere.com/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is JSON data
    print(data)
else:
    print("Failed to fetch data. Status code:", response.status_code)