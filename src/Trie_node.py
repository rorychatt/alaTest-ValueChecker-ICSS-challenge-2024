from dataclasses import dataclass, field
from typing import Dict

@dataclass
class TrieNode:
    children: Dict[str, 'TrieNode'] = field(default_factory=dict)
    price: float = float('inf')
