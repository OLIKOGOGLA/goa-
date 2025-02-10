user = input("enter your name: ")
def speller(user):
    print("\nyour name spelled:")
    for i in user:
        print(i)
speller(user)
#1. ფუნქცია უნდა პრინტავდეს დამარცვლილ სახელს, შებრუნებულად.
user = input("Enter your name: ")

def speller(user):
    print("\nYour name spelled backwards:")
  
    reversed_name = user[::-1]  
    for i in reversed_name:
        print(i)

speller(user)


#2. შექმენით ფუნქცია, რომელსაც გადაეცემა 5 არგუმენტი, 5 ინფუთით მომხარებელს აარჩევინეთ ნებისმიერი რიცხვი, ბოლოს კი დაუპრინტეთ ამ რიცხვებისაგან შემდგარი სია.
def number_picker(a, b, c, d, e):
    numbers = []  # ცარიელი სია, რომელშიც რიცხვებს დავამატებთ
    numbers.append(a)  # პირველი რიცხვის დამატება
    numbers.append(b)  # მეორე რიცხვის დამატება
    numbers.append(c)  # მესამე რიცხვის დამატება
    numbers.append(d)  # მეოთხე რიცხვის დამატება
    numbers.append(e)  # მეხუთე რიცხვის დამატება
    print("\nThe list of numbers:", numbers)

# თითოეული input ცალ ცალკე
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

# ფუნქციის გამოწვევა
number_picker(num1, num2, num3, num4, num5)
def number_picker(a, b, c, d, e):
    numbers = []  # ცარიელი სია, რომელშიც რიცხვებს დავამატებთ
    numbers.append(a)  # პირველი რიცხვის დამატება
    numbers.append(b)  # მეორე რიცხვის დამატება
    numbers.append(c)  # მესამე რიცხვის დამატება
    numbers.append(d)  # მეოთხე რიცხვის დამატება
    numbers.append(e)  # მეხუთე რიცხვის დამატება
    print("\nThe list of numbers:", numbers)

# თითოეული input ცალ ცალკე
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))

# ფუნქციის გამოწვევა
number_picker(num1, num2, num3, num4, num5)


#3. შექმენით ფუნქცია რომელიც არგუმენტად აიღებს თქვენს შექმნილ სიას, რომელშიც იქნება მინიმუმ 5 რიცხვი და დაპრინტავს ამ სიისის მაქსიმალურ რიცხვს, მინიმალურ რიცხვს, რიცხვების ჯამს და სიის სიგრძეს.
def analyze_numbers(numbers):
    max_number = max(numbers)  # მაქსიმალური რიცხვი
    min_number = min(numbers)  # მინიმალური რიცხვი
    sum_of_numbers = sum(numbers)  # რიცხვების ჯამი
    length_of_list = len(numbers)  # სიის სიგრძე

    print(f"\nMax number: {max_number}")
    print(f"Min number: {min_number}")
    print(f"Sum of numbers: {sum_of_numbers}")
    print(f"Length of the list: {length_of_list}")

# აქ 5 რიცხვის სია ვაგზავნოთ
numbers_list = [10, 20, 30, 40, 50]  # მაგალითად, ეს სია
analyze_numbers(numbers_list)
