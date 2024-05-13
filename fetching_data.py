import json
import requests
import matplotlib.pyplot as plt
import base64

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

# Example usage:
try:
    fresh_token = get_fresh_token()
    print(f"New Access Token: {fresh_token}")
except Exception as e:
    print(str(e))

def fetch_iphone_14_list():
    headers = {
    'Authorization': f"Bearer {credentials['token']}",
    'Content-Type': 'application/json',
    'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'  # Adjust this depending on the marketplace you're targeting
}
    # Construct the API endpoint
    query = 'iphone 14'  # Search query
    limit = 100  # Limit the number of results
    url = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit={limit}&filter=condition:{{"used"}}' # item_summary/search only look for buy now items no auctions

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        global price_list
        price_list = []
        
        count = 1
        print(json.dumps(data, indent=4))
        for item in data['itemSummaries']:
            # print(f"{count}: {item['title']} --> {item['price']['value']} {item['price']['currency']}")
            price_list.append(float(item['price']['value']))
            count += 1
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")



def plot_boxplot(x):
    
    plt.boxplot(x)

    plt.title('Price Distribution for the Item')
    plt.ylabel('Price')

    plt.show()

if __name__ == "__main__":
    get_fresh_token()
    # fetch_iphone_14_list()
    # plot_boxplot(price_list)