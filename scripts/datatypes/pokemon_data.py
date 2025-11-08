from dataclasses import dataclass 
from typing import Dict, Optional, Union
from scripts.datatypes.type import Type


@dataclass
class PokemonData: 
    """
    name: Pokemon's name.
    nat_dex_num: Pokemon's national pokedex number.
    dex_num: Dict mapping Pokemon to its dex number.
    type_1: Pokemon's first type
    type_2: Pokemon's second type, if it has one.
    """
    name: str
    nat_dex_num: int

    dex_num: Dict[str, int]
    
    type_1: Type
    type_2: Optional[Type]

    def to_dict(self) -> Dict[str, Union[str, Dict[str, int], int]]:
        return {
            'name': self.name,
            'nat_dex_num': self.nat_dex_num,
            'dex_num': self.dex_num,
            'type_1': self.type_1.value,
            'type_2': self.type_2.value if self.type_2 is not None else None,
        }
