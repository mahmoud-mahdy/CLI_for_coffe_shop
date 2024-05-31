import json
import csv
import requests
import matplotlib.pyplot as plt
import base64
import os

with open('ebay_config.json', 'r') as file:
    credentials = json.load(file)

def get_fresh_token():
    # Placeholder values
    refresh_token = 'credentials[token]'
    client_id = 'credentials[App_ID]'
    client_secret = 'credentials[Cert_ID]'

    # Prepare the request for refreshing the token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'scope': 'https://api.ebay.com/oauth/api_scope'  # Adjust scope as needed
    }
    
    response = requests.post('https://api.ebay.com/identity/v1/oauth2/token', headers=headers, data=data)

    # Handle the response
    if response.status_code == 200:
        new_token = response.json()['access_token']
        # Save the new token securely and update its expiry time
        return new_token
    else:
        # Handle error (e.g., logging, retrying, alerting)
        error_message = response.json().get('error_description', 'Unknown error')
        raise Exception(f"Failed to refresh token: {error_message}")



def fetch_iphone_14_list():
    headers = {
    'Authorization': f"Bearer {credentials['token']}",
    'Content-Type': 'application/json',
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'  # Adjust this depending on the marketplace you're targeting
}
    # Construct the API endpoint
    query = 'iphone 14'  # Search query
    limit = 100  #? ebay only allow maximum of 200
    url = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit={limit}' # item_summary/search only look for buy now items no auctions

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        dict = {}
        json_list = response.json()
        
        
        fieldnames=['itemId', 'title', 'price', 'shipping cost', 'seller', 'seller feedback Percentage', 'seller feedback Score', 'seller', 'condition', 'URL']
        with open('iphone_14_list.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
                       
        for item in json_list['itemSummaries']:
            dict['itemId'] = item['itemId']
            dict['title'] = item['title']
            dict['price'] = item['price']['value']
            dict['shipping cost'] = item['shippingOptions'][0]['shippingCost']['value']
            # dict['location'] = item['itemLocation']['postalCode']
            dict['seller'] = item['seller']['username']
            dict['seller feedback Percentage'] = item['seller']['feedbackPercentage']
            dict['seller feedback Score'] = item['seller']['feedbackScore']
            dict['seller'] = item['seller']['sellerAccountType']
            dict['condition'] = item['condition']
            dict['URL'] = item['itemWebUrl']
            
            with open('iphone_14_list.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=dict.keys())
                writer.writerow(dict)
            
        
        
        
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")


if __name__ == "__main__":
    # try:
    #     fresh_token = get_fresh_token()
    #     print(f"New Access Token: {fresh_token}")
    # except Exception as e:
    #     print(str(e))
    fetch_iphone_14_list()
    # plot_boxplot(price_list)