from random import randint, choice
from typing import Dict, Callable

OPS: Dict[str, Callable[[int, int], int]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}
TASK_NUM = 5


def random_int() -> int:
    return randint(2, 9)


def solve(task: str) -> int:
    a, sign, b = task.split()
    return OPS[sign](int(a), int(b))


def user_input() -> int:
    while True:
        try:
            return int(input())
        except ValueError:
            print('Incorrect format.')


def main():
    correct_answers = 0
    for _ in range(TASK_NUM):
        task = ' '.join(str(x) for x in (random_int(), choice(list(OPS.keys())), random_int()))
        print(task)
        is_correct = solve(task) == user_input()
        correct_answers += is_correct
        print('Right!' if is_correct else 'Wrong!')
    print(f'Your mark is {correct_answers}/{TASK_NUM}.')


main()
