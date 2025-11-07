from typing import Callable

def main()->None: 
    n: int = int(input("n: \n"))
    k: int = int(input("k: \n"))
    
    if k > n: 
        raise Exception("must have n larger then, or equal to k")    
    
    combinatorics_functions: dict[str, Callable[[int, int], int]] = {
        "Repetition allowed & order relevant": repetitionAllowedOrderRelevant, 
        "Repetition allowed & order irrelevant": repetitionAllowedOrderIrrelevant, 
        "Repetition disallowed & order relevant": repetitionDisallowedOrderRelevant, 
        "Repetition disallowed & order irrelevant": repetitionDisallowedOrderIrrelevant, 
    }    
    
    for desc, func in combinatorics_functions.items():
        print(f"{desc}: {func(n, k)}")
    
def repetitionAllowedOrderRelevant(n: int, k: int) -> int:
    return n**k

    
def repetitionAllowedOrderIrrelevant(n: int, k: int) -> int:
    return 1

    
def repetitionDisallowedOrderRelevant(n: int, k: int) -> int:
     return factorial(n=n) // factorial(n=(n-k))

    
def repetitionDisallowedOrderIrrelevant(n: int, k: int) -> int:
    """Binomial theorem"""
    return factorial(n)//(factorial(n-k)*factorial(k))

def factorial(n: int) -> int: 
    product: int = 1
    
    for i in range(1, n+1): 
        product*=i
    
    return product
        

    
if __name__ == "__main__": 
    main()