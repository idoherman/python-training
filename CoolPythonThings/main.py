import module


def learn_for():
    x = [1, 6, 4, 3]
    for value in x:
        print(value, end=' ')
    print()

    for value in [0, 1, 2, 3]:
        print(value, end=' ')
    print()

    x = range(10)
    for value in x:
        print(value, end=' ')
    print()

    for value in [1, 'Hello', [], 7, -5.3]:
        print(value, end=' ')
    print()


def learn_modules():
    # because of the if __name__ in modules.py, True is not printed here.
    print(module.add(8, 9))
    print(module.add(10, 11))


def learn_dictionary():
    d = {1: 'hello', 7.65: 13, 'IDO': 'Herman'}
    print(d[1])
    print(d[7.65])
    print(d['IDO'])

    for key in d:
        print(key, end=' ')
    print()

    for key in d:
        print(f'{key} -> {d[key]}', end='   ')
    print()

    for key, value in d.items():
        print(f'{key} -> {value}', end='   ')
    print()

    for value in d.values():
        print(value, end=' ')
    print()

    for my_tuple in d.keys(), d.values():
        print(my_tuple, end=', ')
    print()

    for my_tuple in zip(d.keys(), d.values()):
        print(my_tuple, end=', ')
    print()

    found8 = 8 in d
    print(found8)


def list_comprehension():
    l1 = [1, 2, 3]

    l2 = []
    for i in range(20):
        l2.append(i)

    l3 = [i*3+5 for i in range(20)]
    print(l3)

    t1 = tuple(i*4+3 for i in range(20))
    print(t1)

    d1 = {i: str(2*i) for i in range(20)}
    print(d1)


def learn_files():
    with open('a.txt', 'w') as f:
        f.write('Hello this is the content of the file')

    with open('b.txt', 'w') as h:
        h.write("I am Ido the coolest person in the entire world :) \n")
        s = f"hellooooooooooooooooo{6*7}ooo"
        h.write(s)

    with open('b.txt', 'a') as f:
        f.write('\n\nappended line!!!!!')

    with open('a.txt', 'r') as f:
        a_txt = f.read()

    with open('a.txt', 'w') as g:
        g.write(a_txt[::-1])


def learn_classes():
    pass
    # TODO learn on my own


def main():
    # learn_modules()
    # learn_for()
    # learn_dictionary()
    # list_comprehension()
    # searched isinstance online - https://www.programiz.com/python-programming/methods/built-in/isinstance
    learn_files()
    # learn_classes()
    # TODO learn sys.argv
    # TODO learn try: except:
    pass


if __name__ == '__main__':
    main()
