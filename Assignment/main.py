def main()->None: 
    n: int = int(input("n: \n"))
    k: int = int(input("k: \n"))
    
    print(repetitionAllowedOrderMatters(n=n, k=k))
    print(repetitionAllowedOrderMattersNot(n=n, k=k))
    print(repetitionDisallowedOrderMatters(n=n, k=k))
    print(repetitionDisallowedOrderMattersNot(n=n, k=k))
    
def repetitionAllowedOrderMatters(n: int, k: int) -> int:
    return n**k

    
def repetitionAllowedOrderMattersNot(n: int, k: int) -> int:
    return 1

    
def repetitionDisallowedOrderMatters(n: int, k: int) -> int:
     return factorial(n=n) // factorial(n=(n-k))

    
def repetitionDisallowedOrderMattersNot(n: int, k: int) -> int:
    return 1

def factorial(n: int) -> int: 
    product: int = 1
    
    for i in range(1, n+1): 
        product*=i
    
    return product
        

    
if __name__ == "__main__": 
    main()