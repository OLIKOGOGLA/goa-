my_string = "გამარჯობა"
print(my_string[1])

num1 = 5
num2 = 7
print(num1 + num2)

str1 = "გამარჯობა"
str2 = "მსოფლიო"
print(str1 + " " + str2)

num3 = 10
num4 = 4
print(num3 / num4)

print(5 == 5)

print(5 + 5 == 8 + 2)

print(True and False)
print(True or False)
print(not True)
print(True and True)
print(False and True)
print(False or False)
print(True or True)

print(5 > 3 and 2 < 3)
print(7 == 7 or 4 > 5)
print(10 != 10 and 5 == 5)
print(8 > 6 or 2 == 3)

for i in range(1, 11):
    print(i)

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

for char in "Hello, World!":
    print(char)

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

sum = 0
i = 1
while sum < 50:
    sum += i
    i += 1
print(sum)
