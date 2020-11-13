def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    return binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1) if k != 0 and n != 0 else (1 if k == 0 else 0)
