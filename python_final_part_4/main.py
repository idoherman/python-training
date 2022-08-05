st_num = input("please enter a number: \n")
print('you entered the number: ' + st_num)

print("The digits of your number are: ", end="")
sum = 0
for i in range(0, len(st_num), 1):
    if i == len(st_num):
        print(st_num[i])
    else:
        print(st_num[i], end=", ")
        sum += int(st_num[i])

print(f'the sum of the digits is: {sum}')


