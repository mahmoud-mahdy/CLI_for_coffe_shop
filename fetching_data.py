import json
import requests
import matplotlib.pyplot as plt


with open('ebay_config.json', 'r') as file:
    credentials = json.load(file)
    
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
    fetch_iphone_14_list()
    plot_boxplot(price_list)