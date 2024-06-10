import requests

# Define the base URL of the Flask API
base_url = 'http://127.0.0.1:5555'

# Make a GET request to the root endpoint
response = requests.get(base_url)
if response.status_code == 200:
    print("Root Endpoint Response:")
    print(response.json())
else:
    print("Failed to retrieve data from the root endpoint")

# Make a GET request to retrieve all newsletters
response = requests.get(f'{base_url}/newsletters')
if response.status_code == 200:
    print("\nAll Newsletters:")
    print(response.json())
else:
    print("Failed to retrieve all newsletters")

# Make a POST request to create a new newsletter
new_newsletter_data = {
    'title': 'New Newsletter Title',
    'body': 'New Newsletter Body'
}
response = requests.post(f'{base_url}/newsletters', data=new_newsletter_data)
if response.status_code == 201:
    print("\nNew Newsletter Created:")
    print(response.json())
else:
    print("Failed to create a new newsletter")

# Make a GET request to retrieve details of a specific newsletter by its ID
newsletter_id = 1  # Example newsletter ID
response = requests.get(f'{base_url}/newsletters/{newsletter_id}')
if response.status_code == 200:
    print("\nNewsletter Details:")
    print(response.json())
elif response.status_code == 404:
    print("Newsletter not found")
else:
    print("Failed to retrieve newsletter details")
