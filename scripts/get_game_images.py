import yaml
import requests
import time
import random
from tqdm import tqdm

def get_game_images() -> None:
    with open('assets\pokemon_data\pokemon.yaml', 'r') as file:
        local_dex = yaml.safe_load(file)  # Returns a dict

    site_prefix ='https://limitlessvgc.com/wp-content/media/icons/gen9/'
    site_suffix = '.png'

    for dex_num, dict in local_dex.items():
        print(dex_num)
        # Weird cases. Skip for manual download.
        if dex_num in (95, 98, 158):
            continue
        site_to_query = site_prefix + dict['name'].lower() + site_suffix

        response = requests.get(site_to_query)
        print(site_to_query)
        if response.status_code == 200:
            # Open a local file in binary write mode
            with open('assets\pokemon_data\sprites\\icons\\' + dict['name'].lower() + '.png', "wb") as f:
                f.write(response.content)
        else:
            print(response.status_code)
        # Sleep for a respectful amount of time.
        time.sleep(random.uniform(0.1, 0.2))

if __name__ == '__main__':
    get_game_images()