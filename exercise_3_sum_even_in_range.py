#Write your code below this row 👇
totaleven = 0
for number in range(1,101):
    if number % 2 == 0:
        totaleven +=number
print(totaleven)


totaleven = 0
for number in range(2,101, 2):
    totaleven += number
print(totaleven)

