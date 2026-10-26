def product(f, lo, hi):
    """
    f:  a function taking a single integer and returning a number
    lo: the starting index (inclusive)
    hi: the ending index (inclusive)

    Returns:
        Prod_{i=lo}^{hi} f(i), the product of f(i) for every integer i
        from lo to hi, both ends included. If hi < lo, the product is
        empty (1).
    """
    product = 1
    if hi < lo:
        return product
    else:
        for i in range(lo, hi + 1):
            product *= f(i)
        return product
