from random import randint, choice
from typing import Dict, Callable

SIGNS = ['+', '-', '*']
OPS: Dict[str, Callable[[int, int], int]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


def random_int() -> int:
    return randint(2, 9)


def solve(task: str):
    a, sign, b = task.split()
    return OPS[sign](int(a), int(b))


def main():
    task = ' '.join(str(x) for x in (random_int(), choice(SIGNS), random_int()))
    print(task)
    print('Right!' if str(solve(task)) == input() else 'Wrong!')


main()
