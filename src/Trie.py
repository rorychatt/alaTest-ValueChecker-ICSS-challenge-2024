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
        longest_prefix_length = 0
        for i, digit in enumerate(phone_number):
            if digit in node.children:
                node = node.children[digit]
                if node.price < float('inf'):
                    current_price = node.price
                    longest_prefix_length = i + 1
            else:
                break
        return current_price if longest_prefix_length > 0 else float('inf')
