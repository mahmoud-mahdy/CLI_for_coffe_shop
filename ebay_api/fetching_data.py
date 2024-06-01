from datetime import datetime
import json
import csv
import requests
import matplotlib.pyplot as plt
import base64
import os

#! To do list
#! [ ] post date filter


with open('ebay_config.json', 'r') as file:
    credentials = json.load(file)

def refresh_token():
    """Refreshes the access token using the refresh token."""
    if 'token' not in credentials or 'App_ID' not in credentials or 'Cert_ID' not in credentials:
        raise ValueError("Invalid credentials dictionary")

    refresh_token = credentials['token']
    client_id = credentials['App_ID']
    client_secret = credentials['Cert_ID']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(
            f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'scope': 'https://api.ebay.com/oauth/api_scope'
    }

    response = requests.post('https://api.ebay.com/identity/v1/oauth2/token', headers=headers, data=data)
    response.raise_for_status()

    response_json = response.json()

    if 'access_token' in response_json:
        return response_json['access_token']
    else:
        error_message = response_json.get('error_description', 'Unknown error')
        raise Exception(f"Failed to refresh token: {error_message}")


def fetch_iphone_14_list():
    headers = {
    'Authorization': f"Bearer {credentials['token']}",
    'Content-Type': 'application/json',
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'  # Adjust this depending on the marketplace you're targeting
}
    # Construct the API endpoint
    query = 'iphone 14'  # Search query
    limit = 200  #? ebay only allow maximum of 200
    offset = 0

    ## to delete after testing
    count = 0
    
    fieldnames=['itemId', 'title', 'price', 'shipping cost','post date','location', 
                'seller', 'seller feedback Percentage', 'seller feedback Score', 'seller', 
                'condition', 'URL']
    
    today = datetime.now().date()
    filename = f'{today}_{query}_list.csv'       
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
    
    while True:
        
        url = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit={limit}&offset={offset}' # item_summary/search only look for buy now items no auctions
        response = requests.get(url, headers=headers)
        
        if not response:
                break
            
        if response.status_code == 200:
            dict = {}
            response_json = response.json()
            
                                              
            for item in response_json['itemSummaries']:
                dict['itemId'] = item.get('itemId', '')
                dict['title'] = item.get('title', '')
                dict['price'] = item.get('price', {}).get('value', '')
                dict['post date'] = item.get('itemCreationDate', '')
                dict['shipping cost'] = item.get('shippingOptions', [{}])[0].get('shippingCost', {}).get('value', '')
                dict['location'] = item.get('itemLocation', {}).get('postalCode', '')
                dict['seller'] = item.get('seller', {}).get('username', '')
                dict['seller feedback Percentage'] = item.get('seller', {}).get('feedbackPercentage', '')
                dict['seller feedback Score'] = item.get('seller', {}).get('feedbackScore', '')
                dict['seller'] = item.get('seller', {}).get('sellerAccountType', '')
                dict['condition'] = item.get('condition', '')
                dict['URL'] = item.get('itemWebUrl', '')
                
                
                
                with open(filename, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow(dict)
                
            print("Successfully retrieved data: ", response.status_code)
            print("offset: ", response_json['offset'])
            
                     
        else:
            print(f"Failed to retrieve data: {response.status_code} - {response.text}")
        
        print(json.dumps(response_json, indent=4))   
        offset += limit



if __name__ == "__main__":
    # try:
    #     fresh_token = refresh_token()
    #     print(f"New Access Token: {fresh_token}")
    # except Exception as e:
    #     print(str(e))
    fetch_iphone_14_list()