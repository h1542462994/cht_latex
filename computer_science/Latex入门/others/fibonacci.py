def fibonacci_loop(x):
    if x < 0:
        return -1
    if x == 1 or x == 2:
        return 1
    else:
        x1 = 1
        x2 = 1
        x3 = 0
        for i in range(3, x + 1):  # iter [2..x]
            x3 = x2 + x1
            x1 = x2
            x2 = x3
        return x3


if __name__ == '__main__':
    print(fibonacci_loop(10000))
