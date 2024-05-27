from dataclasses import dataclass, field
from typing import Dict
from trie import Trie

@dataclass
class Operator:
    name: str
    price_list: Dict[str, float]
    trie: Trie = field(default_factory=Trie)

    def __post_init__(self) -> None:
        for prefix, price in self.price_list.items():
            self.trie.insert(prefix, price)
