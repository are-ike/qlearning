import requests
API_Key = 'LulFPTQGLAGIyNI5WvIIbcAmFL7O85Dp'

def get_traffic(lat, lon):
    # The URL you want to send the GET request to
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/18/json?key={API_Key}&point={lat},{lon}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print(data)
    except Exception as err:
        print(f"An error occurred: {err}")



def get_traffic2():
    base_url = "https://data.traffic.hereapi.com/v7/flow"

    # Parameters for the request
    params = {
        "in": "circle:6.557263,3.377638;r=10000",  # SW and NE corners of the bounding box
        "apiKey": "ItxAtLMnZ04ZXNRFUDPSfhOvF_hxusSU6igjOqWmz1U", 
        "locationReferencing": "olr"                                    # Your API key
        #"units": "metric",                          # Units for speed (optional)
       # "responseattributes": "sh,fc,cf"            # Response attributes (optional)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print(data)
    except Exception as err:
        print(f"An error occurred: {err}")
    
get_traffic2()