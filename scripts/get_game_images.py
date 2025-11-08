import yaml
import requests
import time
import random
from tqdm import tqdm

def get_game_images() -> None:
    with open('assets\pokemon_data\local_dexes\\gsc.yaml', 'r') as file:
        local_dex = yaml.safe_load(file)  # Returns a dict

    site_prefix ='https://img.pokemondb.net/sprites/crystal/normal/'
    site_suffix = '.png'

    for dex_num, name in local_dex.items():
        print(dex_num)
        # Weird cases. Skip for manual download.
        if dex_num in (95, 98, 156):
            continue
        site_to_query = site_prefix + name.lower() + site_suffix

        response = requests.get(site_to_query)
        print(site_to_query)
        if response.status_code == 200:
            # Open a local file in binary write mode
            with open('assets\pokemon_data\sprites\\crystal\\' + name.lower() + '.png', "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)
        # Sleep for a respectful amount of time.
        time.sleep(random.uniform(2.1, 3))

if __name__ == '__main__':
    get_game_images()