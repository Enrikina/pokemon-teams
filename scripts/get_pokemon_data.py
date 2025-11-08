#from scripts.get_pokemon_data import PokemonData
from bs4 import BeautifulSoup
from typing import Dict, Tuple, Optional
import requests
import re

import yaml
from tqdm import  tqdm

from scripts.pokemon_data import PokemonData
from scripts.type import Type
import time
import random

def get_types(subtext: str) -> Tuple[Type, Optional[Type]]:
    split = subtext.split('/')
    #print(split)
    type_1 = Type(re.sub(r'[^a-zA-Z0-9]', '',split[0]).lower())
    type_2 = Type(re.sub(r'[^a-zA-Z0-9]', '',split[1]).lower()) if len(split) > 1 else None
    return (type_1, type_2)

def build_local_pokedex(subtext: str) -> Dict[str, int]:
    local_dict: Dict[str, int] = {}

    split_up = subtext.split(')')
    for local_data in split_up:
        if '(' not in local_data:
            continue
        number, game = local_data.split('(')
        number = int(re.sub(r'[^a-zA-Z0-9]', '', number))
        local_dict[game] = number

    return local_dict

def get_pokemon_data(start_num: int, stop_num: int) -> Dict[int, int]:
    # Maps pokemon name to PokemonData construct.
    pokemon_dict: Dict[int, PokemonData] = {}

    base_url = 'https://pokemondb.net/pokedex/'

    for natdex_num in tqdm(range(start_num, stop_num+1)):
        # Get the HTML context for this Pokemon.
        query_url = base_url + str(natdex_num)
        response = requests.get(query_url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)

        # Get Pokemon Name
        # Find the first space. The pokemon's name is everything before that.
        space_idx = text.find(' ')
        pokemon_name = text[:space_idx]

        # Get Pokemon Type(s)
        preceding_idx = text.find('is a') + len('is a')
        succeeding_idx = text.find('type Pokémon')
        enveloping_text = text[preceding_idx:succeeding_idx]
        if enveloping_text[0].islower():
            enveloping_text = enveloping_text[1:]
        type_1, type_2 = get_types(enveloping_text)

        # Build local pokedex.
        # Get nat-dex nums
        preceding_idx = text.find('National №') + len('National №')
        natdex_num = int(text[preceding_idx: preceding_idx + 5])

        preceding_idx = text.find('Local №') + len('Local №')
        succeeding_idx = text.find('Training')
        local_pokedex = build_local_pokedex(text[preceding_idx:succeeding_idx])

        #Construct PokemonData and add to dict.
        pokemon_data = PokemonData(name = pokemon_name, nat_dex_num= natdex_num, dex_num=local_pokedex, type_1=type_1, type_2=type_2)
        pokemon_dict[natdex_num] = pokemon_data.to_dict()

        # Sleep for a respectful amount of time.
        time.sleep(random.uniform(2.1, 3))

    return pokemon_dict


if __name__ == '__main__': 
    pokemon_dat = get_pokemon_data(1, 1025)

    dump_path = 'assets\pokemon_data\pokemon.yaml'
    with open(dump_path, 'w') as file:
        yaml.dump(pokemon_dat, file, default_flow_style=False)
