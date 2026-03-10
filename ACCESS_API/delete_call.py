import requests

ticket_id = input("Enter ticket ID: ")

url = f"https://loftyoutfits.pythonanywhere.com/ticket/{ticket_id}"


# Send DELETE request
response = requests.delete(url)

if response.status_code == 204:
    print("Data deleted successfully.")
else:
    print("Failed to delete data. Status code:", response.status_code)
