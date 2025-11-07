from dataclasses import dataclass 
from typing import Dict, Optional
from scripts.type import Type


@dataclass
class PokemonData: 
    """
    name: Pokemon's name.
    dex_num: Dict mapping Pokemon to its dex number.
    type_1: Pokemon's first type
    type_2: Pokemon's second type, if it has one.
    """
    name: str
    dex_num: Dict[str, int]
    
    type_1: Type
    type_2: Optional[Type]
