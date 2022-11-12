from random import randint, choice
from typing import Dict, Callable

OPS: Dict[str, Callable[[int, int], int]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}
TASK_NUM = 5
YES_ANSWERS = ['yes', 'YES', 'y', 'Yes']
LEVEL_DESC = {1: 'simple operations with numbers 2-9',
              2: 'integral squares of 11-29'}


def random_int(level: int) -> int:
    match level:
        case 1: return randint(2, 9)
        case 2: return randint(11, 29)


def solve(task: int | str) -> int:
    match task:
        case int(): return task ** 2
        case str():
            a, op, b = task.split()
            return OPS[op](int(a), int(b))


def user_input(prompt: str = '', range_start: int = None, range_end: int = None) -> int:
    while True:
        try:
            answer = int(input(prompt))
            if None not in (range_start, range_end) \
                    and not range_start <= answer <= range_end:
                print('Incorrect format.')
                continue
            return answer
        except ValueError:
            print('Incorrect format.')


def choose_level() -> int:
    return user_input(f'''\
Which level do you want? Enter a number:
1 - {LEVEL_DESC[1]}
2 - {LEVEL_DESC[2]}
''',
                      1, 2)


def get_task(level: int) -> str | int:
    match level:
        case 1: return ' '.join(str(x) for x in (random_int(1), choice(list(OPS.keys())), random_int(1)))
        case 2: return random_int(level)


def print_mark_and_save(correct_answers: int, level: int):
    answer = input(f'Your mark is {correct_answers}/{TASK_NUM}. '
                   'Would you like to save the result? Enter yes or no.\n')
    if answer in YES_ANSWERS:
        name = input('What is your name?\n')
        with open('results.txt', 'a') as f:
            f.write(f'{name}: {correct_answers}/{TASK_NUM} in level {level} ({LEVEL_DESC[level]}).')
        print('The results are saved in "results.txt".')


def main():
    level = choose_level()
    correct_answers = 0
    for _ in range(TASK_NUM):
        task = get_task(level)
        print(task)
        is_correct = solve(task) == user_input()
        correct_answers += is_correct
        print('Right!' if is_correct else 'Wrong!')

    print_mark_and_save(correct_answers, level)


main()
