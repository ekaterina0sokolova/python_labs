
def my_pow(num):
    return num ** 2


def div_by_seven(num):
    return True if num % 7 == 0 else False


def function(n):
    def_list = [i for i in range(n+1)]
    list_1 = list(filter(div_by_seven, def_list))
    list_2 = list(map(my_pow, list_1))

    list_3 = []
    for i, j in zip(list_1, list_2):
        list_3.append((i, j))

    return sum(x for tup in list_3 for x in tup)


def main():
    print(function(1000))


if __name__ == '__main__':
    main()
