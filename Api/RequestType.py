import requests

def requestType(name: str) -> dict:
    url = f"https://pokeapi.co/api/v2/type/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error:', response.status_code)
