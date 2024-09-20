
def my_set(n):
    my_set = {i for i in range(0, n)}
    set_1 = {i for i in my_set if i % 2 == 0}
    set_2 = {i for i in my_set if i % 4 == 0}
    return sum(set_1 ^ set_2)


def main():
    print(my_set(19))
    print(my_set(63))


if __name__ == '__main__':
    main()
