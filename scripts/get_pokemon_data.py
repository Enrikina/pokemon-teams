#from scripts.get_pokemon_data import PokemonData
from bs4 import BeautifulSoup
from typing import Dict, Tuple, Optional
import requests
import re

import os

from scripts.pokemon_data import PokemonData
from scripts.type import Type

def get_types(subtext: str) -> Tuple[Type, Optional[Type]]:
    split = subtext.split('/')
    type_1 = Type(re.sub(r'[^a-zA-Z0-9]', '',split[0]).lower())
    type_2 = Type(re.sub(r'[^a-zA-Z0-9]', '',split[1]).lower()) if len(split) > 1 else None
    return (type_1, type_2)


def get_pokemon_data(start_num: int, stop_num: int) -> Dict[str, int]:
    # Maps pokemon name to PokemonData construct.
    pokemon_dict: Dict[str, PokemonData] = {}

    base_url = 'https://pokemondb.net/pokedex/'

    for natdex_num in range(start_num, stop_num+1):
        # Get the HTML context for this Pokemon.
        query_url = base_url + str(natdex_num)
        response = requests.get(query_url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator="\n", strip=True)
        print(text)
        print(type(text))


        # Get Pokemon Name
        # Find the first space. The pokemon's name is everything before that.
        space_idx = text.find(' ')
        pokemon_name = text[:space_idx]

        # Get Pokemon Type(s)
        preceding_idx = text.find('is a') + 4
        succeeding_idx = text.find('type Pokémon')
        enveloping_text = text[preceding_idx:succeeding_idx]
        type_1, type_2 = get_types(enveloping_text)

        print(pokemon_name)
        print([type_1, type_2])

        #TODO: Build local pokedex.


        #TODO: Construct PokemonData and add to dict.


    return pokemon_dict


if __name__ == '__main__': 
    print(os.getcwd())
    pokemon_dat = get_pokemon_data(1, 1)