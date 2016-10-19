def alternating_coin_game(coins):
    """
        which coin should we pick for optimal win sum?

    :param coins: list of coin values from left to right
    :return: coin_value, optimal_payoff
    """

    cache = {}

    def rec(a, b, is_max):
        """
            Returns the optimal choice for a slice of values

        :param is_max: either maximising (our move) or minimising (opponents move)
        :param a: left index
        :param b: right index
        :return: coin_value, optimal_payoff
        """

        cache_key = (a, b, is_max)
        if cache.has_key(cache_key):
            return cache[cache_key]

        if a == b:
            ret = (coins[a], coins[a]) if is_max else (None, 0)
        else:
            left = rec(a + 1, b, not is_max)[1]
            right = rec(a, b - 1, not is_max)[1]

            if is_max:
                left = left + coins[a]
                right = right + coins[b]
                ret = (coins[a], left) if left >= right else (coins[b], right)
            else:
                ret = (coins[a], left) if left <= right else (coins[b], right)

        cache[cache_key] = ret
        return ret

    if not coins:
        return None, 0

    return rec(0, len(coins) - 1, True)
