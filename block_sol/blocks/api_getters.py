import requests


def get_height():
    """Function to get current blockchain height"""

    url = "https://bcschain.info/api/info"
    response = requests.get(url)
    height = response.json()["height"]
    return height


def get_blocks():
    height = get_height()
    url = "https://bcschain.info/api/blocks"
    response = requests.get(url)
    json = response.json()

    return json

def get_block(height):
    height = height
    url = "https://bcschain.info/api/block" + f"/{height}"
    response = requests.get(url)
    json = response.json()
    print(json)

    return json

if __name__ == "__main__":
    get_block(218565)
