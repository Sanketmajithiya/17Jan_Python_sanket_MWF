import requests

ticket_id = input("Enter ticket ID: ")

url = f"https://loftyoutfits.pythonanywhere.com/ticket/{ticket_id}"

response = requests.get(url)

if response.status_code == 200:
    # If the request was successful (status code 200), you can access the response content
    data = response.json()  # Assuming the response is JSON data
    print(data)  # This will print the data for ticket with ID 2
else:
    print("Failed to fetch data. Status code:", response.status_code)
