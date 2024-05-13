import requests
import json

# Load credentials from a JSON file
with open('ebay_config.json', 'r') as file:
    credentials = json.load(file)

# Set up headers using the user token
headers = {
    'Authorization': f"Bearer {credentials['token']}",
    'Content-Type': 'application/json',
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'  # Adjust this depending on the marketplace you're targeting
}

# Example endpoint for the Finding API to search for items
# url = "https://svcs.ebay.com/services/search/FindingService/v1"
url = 'https://api.ebay.com/buy/browse/v1/item_summary/search?q="iphone 14"&limit=3'
params = {
    'OPERATION-NAME': 'findItemsByKeywords',
    'SERVICE-VERSION': '1.0.0',
    'SECURITY-APPNAME': credentials['App ID (Client ID)'],
    'RESPONSE-DATA-FORMAT': 'JSON',
    'filter': 'conditions:{3000}',  # filter for used items
    'keywords': ''
}

response = requests.get(url, headers=headers, params=params)

data = response.json()

print(json.dumps(data, indent=4))