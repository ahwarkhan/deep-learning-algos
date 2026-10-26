def factorial(n):
    """
    n: a non-negative integer

    Returns:
        n! = n * (n-1) * ... * 1, the product of every integer from 1 to
        n. factorial(0) is 1 (the empty-product convention).
    """
    fact = 1
    
    if n < 0:
        return "n should be a positive integer."
    elif n == 0:
        return fact
    else:
        while n >= 1:
            fact *= n
            n -= 1
        return fact


def n_choose_k(n, k):
    """
    n, k: non-negative integers, 0 <= k <= n

    Returns:
        C(n, k) = n! / (k! * (n - k)!), the number of size-k subsets of
        an n-element set, as an integer.
    """
    return int(factorial(n) / (factorial(k) * factorial(n-k)))
