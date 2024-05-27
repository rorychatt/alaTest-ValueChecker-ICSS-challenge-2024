from dataclasses import dataclass, field
from Trie_node import TrieNode

@dataclass
class Trie:
    root: TrieNode = field(default_factory=TrieNode)

    def insert(self, prefix: str, price: float) -> None:
        node = self.root
        for digit in prefix:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.price = price

    def search(self, phone_number: str) -> float:
        node = self.root
        current_price = float('inf')
        for digit in phone_number:
            if digit in node.children:
                node = node.children[digit]
                if node.price < current_price:
                    current_price = node.price
            else:
                break
        return current_price
