import requests

if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon/charmander"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Error:', response.status_code)
