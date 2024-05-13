import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    import requests
    import json
    import pandas as pd

    # Load credentials from a JSON file
    with open('ebay_config.json', 'r') as file:
        credentials = json.load(file)

    # Set up headers using the user token
    headers = {
        'Authorization': f"Bearer {credentials['token']}",
        'Content-Type': 'application/json',
        'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'  # Adjust this depending on the marketplace you're targeting
    }

    # Construct the API endpoint
    query = 'iphone 14'  # Search query
    limit = 300  # Limit the number of results

    url = f'https://api.ebay.com/buy/browse/v1/item_summary/search?q={query}&limit={limit}' # item_summary/search only look for buy now items no auctions


    # Make the API request
    response = requests.get(url, headers=headers)

    # Check response status and print formatted JSON data if successful
    if response.status_code == 200:
        data = response.json()
        
        price_list = []
        count = 1
        # print(json.dumps(data, indent=4))
        for item in data['itemSummaries']:
            print(f"{count}: {item['title']} --> {item['price']['value']} {item['price']['currency']}")
            price_list.append(float(item['price']['value']))
            count += 1
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")


    import matplotlib.pyplot as plt

    plt.boxplot(price_list)

    # Adding titles and labels
    plt.title('Price Distribution for the Item')
    plt.ylabel('Price')

    # Show the plot
    plt.show()

    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
