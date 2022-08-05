def print_vowel_in_b_language(letter):
    print(bet_language[i], end="")
    print('b', end="")
    print(bet_language[i].lower(), end="")


exercise = 'Hello, my name is Inigo Montoya'
print(exercise[0:5])
print(exercise[7:14])
print(exercise[::2])
print(exercise[2:19:2])

bet_language = input("please type a sentence \n")
for i in range(0, len(bet_language), 1):
    lower_letter = bet_language[i].lower()
    if lower_letter == 'a' or lower_letter == 'e' or lower_letter == 'i' or lower_letter == 'o' or lower_letter == 'u':
        print_vowel_in_b_language(bet_language[i])

    elif bet_language[i] == ' ':
        print(' ', end="")

    else:
        print(bet_language[i], end="")


