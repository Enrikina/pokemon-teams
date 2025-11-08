function toggleBlock(color, button, gen_val) {
    // Set-up section and div names.
    let section_name = 'gen' + gen_val + '_teams_section';

    let div_name = section_name + "_" + button.innerText;

    const section = document.getElementById(section_name);
    const divExists = section.querySelector("." + div_name);

    if (!divExists) {

    [yaml, dir] = getYamlAndDir(button.innerText);

    boy_option_only = boy_only_game(button.innerText);

    // Create a new block.
    const block = document.createElement('div');
    block.style.marginRight = '20px';
    block.classList.add('row');

    const trainer_square = document.createElement('div');
    trainer_square.classList.add('trainer_square');
    makeTrainerDropdown(dir + "\\Trainer\\", trainer_square, boy_option_only);

    block.appendChild(trainer_square);
    trainer_square.style.backgroundColor = color;

    // TODO: Generalize for other games

    const bar = document.createElement('div');
    bar.classList.add('bar');
    block.appendChild(bar);    

    for (let i = 0; i < 6; i++) {
        const square = document.createElement('div');
        square.classList.add('square');
        block.appendChild(square);
        square.style.backgroundColor = color;
    }

    // --- Add a dropdown to every square ---
    block.querySelectorAll('.square').forEach(sq => {
        if (yaml != -1) {
            dropdown = makeDropdown(yaml, dir, sq);
            // Add dropdown inside the square
            }

    });


    block.classList.add(div_name);
    section.appendChild(block);
    }

    else {
        divExists.remove();
    }

}

async function makeTrainerDropdown(dir, sq, boy_option_only) {
    const dropdown = document.createElement('select');
    
    const option = document.createElement('option');
    option.value = "undefined";
    option.textContent = "--";
    dropdown.appendChild(option);

    if (boy_option_only) {
        trainer_options = ["boy"];
    }
    else {
        trainer_options = ["boy", "girl"];
    }

    for (const key in trainer_options) {
        const option = document.createElement('option');
        option.value = trainer_options[key];
        option.textContent = trainer_options[key].charAt(0).toUpperCase() + trainer_options[key].slice(1);;
        dropdown.appendChild(option);
    }
    
    // Style dropdown to fit inside square
    dropdown.style.width = '100%';
    dropdown.style.height = '100%';
    dropdown.style.boxSizing = 'border-box';
    dropdown.style.background = 'transparent';
    dropdown.style.color = 'black';
    dropdown.style.border = 'none';
    dropdown.style.fontSize = '14px';
    dropdown.style.textAlign = 'center';

    // Create <img> element to display selected PNG
    const img = document.createElement('img');
    img.style.width = '100%';
    img.style.height = '100%';
    img.style.display = 'block';
    img.style.margin = '0px auto 0 auto';
    img.src = `${dir}/${dropdown.value}.png`; // initial image
    sq.appendChild(img);
    sq.appendChild(dropdown);

    // Update image whenever dropdown selection changes
    dropdown.addEventListener('change', () => {
        img.src = `${dir}/${dropdown.value}.png`;
    });

    return dropdown;
}


async function makeDropdown(yaml, dir, sq) {
    const actual_yaml = await loadYaml(yaml);
    if (!actual_yaml) return;

    const dropdown = document.createElement('select');
    
    const option = document.createElement('option');
    option.value = "undefined";
    option.textContent = "--";
    dropdown.appendChild(option);

    for (const key in actual_yaml) {
        actual_yaml[key] = actual_yaml[key].toLowerCase();

        const option = document.createElement('option');
        option.value = key;
        option.textContent = actual_yaml[key].charAt(0).toUpperCase() + actual_yaml[key].slice(1);
        dropdown.appendChild(option);
    }
    
    // Style dropdown to fit inside square
    dropdown.style.width = '100%';
    dropdown.style.height = '100%';
    dropdown.style.boxSizing = 'border-box';
    dropdown.style.background = 'transparent';
    dropdown.style.color = 'black';
    dropdown.style.border = 'none';
    dropdown.style.fontSize = '14px';
    dropdown.style.textAlign = 'center';

    // Create <img> element to display selected PNG
    const img = document.createElement('img');
    img.style.width = '100%';
    img.style.height = '100%';
    img.style.display = 'block';
    img.style.margin = '0px auto 0 auto';
    img.src = `${dir}/${actual_yaml[dropdown.value]}.png`; // initial image
    sq.appendChild(img);
    sq.appendChild(dropdown);

    // Update image whenever dropdown selection changes
    dropdown.addEventListener('change', () => {
        img.src = `${dir}/${actual_yaml[dropdown.value]}.png`;
    });

    return dropdown;
}

async function loadYaml(path) {
    try {
        const response = await fetch(path); // fetch the YAML file from server
        if (!response.ok) throw new Error('Failed to load YAML');
        const text = await response.text(); // get YAML as string
        const data = jsyaml.load(text);     // parse YAML into JS object
        return data;
    } catch (err) {
        console.error(err);
        return null;
    }
}


function getYamlAndDir(game) {
      // Get the yaml and directory associated with this game.
      switch (game) {
        case 'Firered':
            return ['assets\\pokemon_data\\local_dexes\\frlg.yaml', 'assets\\pokemon_data\\sprites\\frlg']
        case 'Leafgreen':
            return ['assets\\pokemon_data\\local_dexes\\frlg.yaml', 'assets\\pokemon_data\\sprites\\frlg']     
            
        default:
            return [-1, -1];
      }
}

function boy_only_game(game) {
    // These games only have a boy character option.
    const boy_only_games = ['Red', 'Blue', 'Yellow', 'Gold', 'Silver'];

    return boy_only_games.includes(game);
}

function toggleSection() {
    const buttons = document.getElementById('buttons');
    buttons.classList.toggle('hidden');
}

window.toggleBlock = toggleBlock;
window.toggleSection = toggleSection;