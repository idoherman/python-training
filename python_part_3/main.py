#age = 17
#if age == 18:
#    print('Congratulations')
#elif age < 18:
#    print('You are so young')
#else:
#    print('We love old people')


num1 = 0
num2 = 1
temp = 0;
print(num1)
print(num2)
while True:
    temp = num2
    num2 = num1 + num2
    num1 = temp
    if num2 >= 10000:
        break
    print(num2)

print("\n")

for i in range(1, 41, 1):
    print(i, end=" ")

print("\n")

for i in range(1, 101, 1):
    if (i % 7 == 0) or (i % 10 == 7) or (((i / 10) % 10) >= 7 and ((i / 10) % 10) < 8):
        print(i)

print("\n")

temporary = 0
for i in range(5):
    for j in range(10):
        temporary += 1
        if temporary % 10 is not 0:
            print(temporary / 10, end=" ")
    print(i + 1)
