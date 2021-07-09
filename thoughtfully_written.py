def recursive_loop(a: float, v: int) -> float:
    """
    recursively loops down to v=0 by v-1. equivalent to a**v
    :param a: floating point base to be recursively exponentiated
    :param v: amount of loops to run through
    :return: float a ** v
    """

    return a if v <= 1 else a * recursive_loop(a, v - 1)


def calculate_compound_interest(amt: float, term: int, apy: float) -> float:
    """
    uses recursion
    calculate compound interest of initial investment amt for term years term vested at apy interest
    :param amt: initial principal for investment
    :param term: int years of investment
    :param apy: float apy of investment
    :return: float accumulated amount at end of term
    """
    return amt * recursive_loop(a=(1 + apy), v=term)
