
def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def work(n):
    first_list = [i for i in range(3, n) if is_prime(i)]
    second_list = [i for i in range(200, 501) if is_prime(i)]

    first_list.extend(second_list)
    first_list.pop(20)

    return first_list[14] + first_list[30]


def main():
    print(work(7))
    print(work(17))


if __name__ == '__main__':
    main()
