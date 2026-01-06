#2. Cree un programa que permita agregar un Pokémon nuevo al archivo 
# de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
#    1. Debe leer el archivo para importar los Pokémones existentes.
#    2. Luego debe pedir la información del Pokémon a agregar.
#    3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

#function to read the file
def read_pokemons(file):
    with open(file, "r", encoding='utf-8') as f:
        pokemons = json.load(f)
    print("Existing Pokemons: ")
    print(pokemons)
    return pokemons

#Function to create pokemons
def create_pokemon(): 
    pokemon_list = []
    
    start = input("Do you want to create a Pokemon? y/n: ").strip().lower()
    if start == "n":
            return [] # Exit of loop with an empty list
    
    while True:
        name = input ("Pokemon name: ").strip()
        pok_type = input("Type: ").strip()
        hp = input("HP: ").strip()
        attack = input("Attack: ").strip()
        defense = input("Defense: ").strip()
        spattack = input("SP Attack: ").strip()
        spdefense = input("SP Defense: ").strip()
        speed = input("Speed: ").strip()

        pokemon = {
            "name": {"english": name},
            "type": [pok_type],
            "base": {
                "HP": hp,
                "Attack": attack,
                "Defense": defense,
                "Sp. Attack": spattack,
                "Sp. Defense": spdefense,
                "Speed": speed
            }
        }
        pokemon_list.append(pokemon)

        more = input("Do you want to enter another Pokemon? y/n: ").strip().lower()
        if more == 'n':
            print(pokemon_list)
            break
        
    return pokemon_list

#Function to write to pokemon.jason
def write_pokemons(file, data):
    with open(file, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# MAIN PROGRAM -----
file_path = "pokemon.json"
#Read pokemons
existing_pokemons = read_pokemons(file_path)
#Create new pokemons
new_pokemons = create_pokemon()
#Write list of pokemons including old list
all_pokemons = existing_pokemons + new_pokemons
# Write list back to file
write_pokemons(file_path, all_pokemons)

