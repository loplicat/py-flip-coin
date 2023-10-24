import random


def flip_coin() -> dict:
    flips = 10
    flipping_cases = 10000
    result = {i: 0 for i in range(11)}
    for _ in range(flipping_cases):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        result[heads] += 1
    results = {k: (v / flipping_cases * 100) for k, v in result.items()}
    return results
