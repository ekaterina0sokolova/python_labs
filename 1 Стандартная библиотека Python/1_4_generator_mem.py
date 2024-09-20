from string import ascii_letters
from random import choice
from sys import getsizeof


def random_string_generator(n):
    for _ in range(n):
        yield ''.join(choice(ascii_letters) for _ in range(5))

def check_generator():
    mas_gen = []
    for _ in range(1000):
        mas_gen.append(choice(ascii_letters) for _ in range(5))

    mem1 = getsizeof(mas_gen)

    gen = random_string_generator(1000)

    first_el = next(gen)
    second_el = next(gen)

    mem2 = getsizeof(second_el)

    return mem1 - mem2


def main():
    print(check_generator())


if __name__ == '__main__':
    main()
