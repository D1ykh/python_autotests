import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c580c5cec103a7cea17685681757932f'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN} 
body_create = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response.text)

pokemon_id = response.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)



response_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)