#from scripts.get_pokemon_data import PokemonData
from bs4 import BeautifulSoup
from typing import Dict, Tuple, Optional
import requests

import os

from scripts.pokemon_data import PokemonData
from scripts.type import Type

def get_types(subtext: str) -> Tuple[Type, Optional[Type]]:
    ...

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


        #TODO: Get Pokemon Name
        # Find the first space. The pokemon's name is everything before that.
        space_idx = text.find(' ')
        pokemon_name = text[:space_idx]

        #TODO: Get Pokemon Type(s)

        #TODO: Build local 

        #TODO: Construct PokemonData and add to dict.


    return pokemon_dict


if __name__ == '__main__': 
    print(os.getcwd())
    pokemon_dat = get_pokemon_data(1, 1)