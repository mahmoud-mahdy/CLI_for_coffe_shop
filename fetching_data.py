import json
import requests
import matplotlib.pyplot as plt

with open('ebay_config.json', 'r') as file:
    credentials = json.load(file)

def get_fresh_token():
    # Placeholder values
    refresh_token = 'your_refresh_token_here'
    client_id = 'your_client_id_here'
    client_secret = 'your_client_secret_here'

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
        raise Exception("Failed to refresh token")

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
    fetch_iphone_14_list()
    plot_boxplot(price_list)