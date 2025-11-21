from typing import Callable


def main() -> None:
    n: int = int(input("n: "))
    s: str = input("k values (comma-separated): ")
    mul_k = list(map(int, s.split(",")))

    if n < 0 or any(k < 0 for k in mul_k):
        raise ValueError("n and all k values must be non-negative")

    cases: list[Callable[[int, int], str]] = [
        with_repetition_ordered_sentence,
        without_repetition_ordered_sentence,
        without_repetition_unordered_sentence,
        with_repetition_unordered_sentence,
    ]

    for k in mul_k:
        print(f"\nn={n}, k={k}")
        for func in cases:
            print(func(n, k))


def with_repetition_ordered_sentence(n: int, k: int) -> str:
    problem_statement: str = f"A program executes {k} function{'s' if k > 1 else ''} from {n} possible function{'s' if n > 1 else ''}"
    count: int = n ** k
    
    return f"{problem_statement} has {count} possible execution sequence{'s' if count > 1 else ''}."


def without_repetition_ordered_sentence(n: int, k: int) -> str:
    problem_statement: str = f"Seating {k} out of {n} guests at a wedding"

    if k > n:
        return f"{problem_statement} is undefined when k > n."
    
    count: int = factorial(n) // factorial(n - k)
    
    return f"{problem_statement} can result in {count} different seating arrangement{'s' if count > 1 else ''}."


def without_repetition_unordered_sentence(n: int, k: int) -> str:
    problem_statement: str = f"Choosing {k} title{'s' if k > 1 else ''} from a library of {n} book{'s' if n > 1 else ''}"

    if k > n:
        return f"{problem_statement} is undefined when k > n."
    
    count: int = factorial(n) // (factorial(n - k) * factorial(k))
    
    return f"{problem_statement} can be done in {count} way{'s' if count > 1 else ''}."


def with_repetition_unordered_sentence(n: int, k: int) -> str:
    problem_statement: str = f"Distributing {k} identical item{'s' if k > 1 else ''} among {n} recipient{'s' if n > 1 else ''}"
    
    if n == 0 and k > 0:
        return f"{problem_statement} is undefined when n=0."
    
    count: int = factorial(n + k - 1) // (factorial(n - 1) * factorial(k)) if n > 0 else 1
    
    return f"{problem_statement} can be done in {count} way{'s' if count > 1 else ''}."


def factorial(n: int) -> int: 
    return 1 if n < 2 else n * factorial(n - 1) 


if __name__ == "__main__":
    main()