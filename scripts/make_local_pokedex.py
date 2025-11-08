import yaml
from typing import Dict

def make_local_pokedex(game: str) -> None:
    with open('assets\pokemon_data\pokemon.yaml', 'r') as file:
        national_dex = yaml.safe_load(file)  # Returns a dict

    local_pokedex: Dict[int, str] = {}
    counter = 0

    for val in national_dex.values():
        local_dex_nums = val['dex_num']
        if (local_dex:= local_dex_nums.get(game)) is not None:
            local_pokedex[local_dex] = val['name']
        elif (local_dex_2:= local_dex_nums.get('Crystal/Gold/Silver')) is not None:
            local_pokedex[local_dex_2] = val['name']

    
    dump_path = 'assets\pokemon_data\local_dexes\\gsc.yaml' 
    with open(dump_path, 'w') as file:
        yaml.dump(local_pokedex, file, default_flow_style=False)



if __name__ == '__main__':
    make_local_pokedex('Gold/Silver/Crystal')