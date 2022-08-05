def summer(list1):
    sum = list1[0]
    for i in range(1, len(list1), 1):
        sum += list1[i]
    return sum


def last_letter(str):
    return str[len(str) - 1]


stam = [5, 3, 2, 5, 7]
print(id(stam))
stam[:] = stam[1::2]
print(id(stam))
print(stam)

lst = [2, 54, 13]
lst[1] = 12
print(lst)

print(summer([10, 11, 12, 0.75]))

print(summer([True, False, True]))

print(summer(['aa', 'bb', "cc"]))

print(summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]))


family = ['Ido', 'Tom', 'Stav', 'Galit', 'Eyal']
family.sort(key=last_letter)
print(family)

print("\n \n \n")
tup = (4, 2, 7)
print(tup)
print(id(tup))
tup = (5, 3, 8, 9)
print(tup)
print(id(tup))
