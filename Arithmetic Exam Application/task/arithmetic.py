def main():
    res = 0
    a, sign, b = input().split()
    a, b = int(a), int(b)
    match sign:
        case '+':
            res = a + b
        case '-':
            res = a - b
        case '*':
            res = a * b
    print(res)


main()
