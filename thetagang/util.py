import math

from ib_insync.contract import Option


def to_camel_case(snake_str):
    components = snake_str.split("_")
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + "".join(x.title() for x in components[1:])


def account_summary_to_dict(account_summary):
    d = dict()
    for s in account_summary:
        d[s.tag] = s
    return d


def portfolio_positions_to_dict(portfolio_positions):
    d = dict()
    for p in portfolio_positions:
        symbol = p.contract.symbol
        if symbol not in d:
            d[symbol] = []
        d[symbol].append(p)
    return d


def justify(s):
    return s.rjust(12)


def position_pnl(position):
    return position.unrealizedPNL / abs(position.averageCost * position.position)


def count_option_positions(symbol, portfolio_positions, right):
    if symbol in portfolio_positions:
        return math.floor(
            -sum(
                [
                    p.position
                    for p in portfolio_positions[symbol]
                    if isinstance(p.contract, Option)
                    and p.contract.right.startswith(right)
                ]
            )
        )

    return 0
