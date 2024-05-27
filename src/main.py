from operator import Operator
from sample_data import price_lists

def find_cheapest_operator(phone_number: str, operators: Dict[str, Operator]) -> str:
    cheapest_operator = None
    lowest_price = float('inf')
    
    for operator in operators.values():
        price = operator.trie.search(phone_number)
        if price < lowest_price:
            lowest_price = price
            cheapest_operator = operator.name
            
    return cheapest_operator

def main():
    operators = {name: Operator(name, prices) for name, prices in price_lists.items()}
    
    phone_number = "46732412345"
    cheapest_operator = find_cheapest_operator(phone_number, operators)
    print(f"The cheapest operator for {phone_number} is {cheapest_operator}")

if __name__ == "__main__":
    main()
