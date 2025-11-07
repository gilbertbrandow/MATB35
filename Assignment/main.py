from typing import Callable

def main()->None: 
    n: int = int(input("n: "))
    s: str = input("k's: ")
    mul_k = list(map(int, s.split(", ")))
    
    if n < 0 or any(k < 0 for k in mul_k):
        raise ValueError("n and all k values must be non-negative")
    
    combinatorics_functions: dict[str, Callable[[int, int], int]] = {
        "Repetition allowed & order relevant": repetitionAllowedOrderRelevant, 
        "Repetition allowed & order irrelevant": repetitionAllowedOrderIrrelevant, 
        "Repetition disallowed & order relevant": repetitionDisallowedOrderRelevant, 
        "Repetition disallowed & order irrelevant": repetitionDisallowedOrderIrrelevant, 
    }    
    
    for k in mul_k: 
        print(f"n={n}, k={k}")
        for desc, func in combinatorics_functions.items():
            try:
                print(f"  {desc}: {func(n, k)}")
            except ValueError as e:
                print(f"  {desc}: undefined ({e})")


def repetitionAllowedOrderRelevant(n: int, k: int) -> int:
    return n**k

    
def repetitionAllowedOrderIrrelevant(n: int, k: int) -> int:
    return factorial(n=n+k-1) // (factorial(n-1)*factorial(k))

    
def repetitionDisallowedOrderRelevant(n: int, k: int) -> int:
    if k > n:
        raise ValueError("k must be <= n when repetition is disallowed")  
      
    return factorial(n=n) // factorial(n=(n-k))

    
def repetitionDisallowedOrderIrrelevant(n: int, k: int) -> int:
    """Binomial theorem"""
    
    if k > n:
        raise ValueError("k must be <= n when repetition is disallowed") 
    
    return factorial(n)//(factorial(n-k)*factorial(k))

def factorial(n: int) -> int: 
    product: int = 1
    
    for i in range(1, n+1): 
        product*=i
    
    return product
        

    
if __name__ == "__main__": 
    main()