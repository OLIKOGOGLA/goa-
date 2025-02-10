# # Random Functions:
# 1. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მის კვადრატს.

number = input("Enter a number: ")

number = float(number)

def square(number):
    return number ** 2

print(square(number))
# 2. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.

number1 = input("Enter a number1: ")
number2 = input("Enter a number2: ")

number1 = int(number1)
number2 = int(number2)

def namber(number1, number2):
    return number1 + number2

print(namber(number1, number2))

# 3. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს ყველაზე პატარას.

def find_smallest(numbers):
    return min(numbers)

numbers1 = [3, 1, 4, 1, 5, 9]
smallest_number = find_smallest(numbers1)
print("The smallest number is:", smallest_number) 

# 4. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და ამოწმებს, არის თუ არა ის დადებითი.

def is_positive(number):
    return number > 0

numbers2 = 5
is_positive_number = is_positive(numbers2)
print("Is the number", numbers2, "positive?", is_positive_number) 

# 5. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს მათ ჯამს.

def sum_of_numbers(numbers):
    return sum(numbers)

numbers3 = [3, 1, 4, 1, 5, 9]
total_sum = sum_of_numbers(numbers3)
print("The sum of numbers is:", total_sum) 
