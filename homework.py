def fibonacci_of(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci_of(num-1) + fibonacci_of(num-2)


def main():
    for i in range(200):
        print(fibonacci_of(i+1))

if __name__ == '__main__':
    main()