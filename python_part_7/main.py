def is_number(s):
    for i in s:
        if not s.isdigit():
            return False
    return True


def is_5_length(s):
    if len(s) == 5:
        return True
    return False


def main():
    msg_from_user = input("Please type a number that his length is 5 digits: \n")

    while not is_number(msg_from_user) or not is_5_length(msg_from_user):
        print("Problem!!! - You didn't listen to the instructions :(")
        msg_from_user = input("Please type a number that his length is 5 digits: \n")

    print("\n" f"The number is: {msg_from_user}")
    sum_digits = 0
    number_from_user = int(msg_from_user)

    for i in range(5):
        digit = number_from_user % 10

        if i < 4:
            print(msg_from_user[i], end=", ")
        else:
            print(msg_from_user[i])

        sum_digits += digit
        number_from_user //= 10
    print(f"The sum of the digits of the number is: {sum_digits}")


if __name__ == '__main__':
    main()


