# Program that concatenate 2 strings and print the concatenated string in reverse (end to start).

st1 = input("Hi, please type something: ")
st2 = input("Hi, please type another thing: ")
my_string = st1 + st2
print(my_string[len(my_string) - 1:: -1])
