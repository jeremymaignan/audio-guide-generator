import requests

def download_page(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Could not download the HTML page Status code: {}".format(response.status_code))
        return None
    return response
