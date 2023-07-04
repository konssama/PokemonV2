import requests

def requestPokemon(name: str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error:', response.status_code)
