# 2) შექმენით ფუნქცია, რომელიც მიიღებს ნებისმიერ რაოდენობის რიცხვებს 'args'-ით და დააბრუნებს მათ ჯამს
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))

# 3) შექმენით ფუნქცია, რომელიც მიიღებს ნებისმიერ რაოდენობის სტრინგებს 'args'-ით და დააბრუნებს ყველა სტრინგი გაერთიანებულად
def join_strings(*args):
    return "".join(args)

print(join_strings("Hello", " ", "Python", "!"))

# 4) შექმენით ფუნქცია, რომელიც მიიღებს 'kwargs'-ით ადამიანის მონაცემებს (სახელი, ასაკი) და დაბეჭდავს "სახელი: X, ასაკი: Y"
def print_person(**kwargs):
    print(f"სახელი: {kwargs.get('name')}, ასაკი: {kwargs.get('age')}")

print_person(name="Giorgi", age=15)

# 5) შექმენით ფუნქცია, რომელიც მიიღებს 'kwargs'-ით მანქანის მონაცემებს და დაბეჭდავს თითოეულ გასაღებს და მნიშვნელობას
def print_car_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_car_info(brand="BMW", model="X5", year=2022, color="Black")

# 6) დაწერეთ დეკორატორი, რომელიც ფუნქციის გაშვების წინ დაბეჭდავს "ფუნქცია დაიწყო" და დასრულების შემდეგ "ფუნქცია დასრულდა"
def start_end_decorator(func):
    def wrapper():
        print("ფუნქცია დაიწყო")
        func()
        print("ფუნქცია დასრულდა")
    return wrapper

@start_end_decorator
def say_hello():
    print("Hello!")

say_hello()

# 7) დაწერეთ დეკორატორი, რომელიც ფუნქციის გაშვების დროს დაითვლის რამდენი წამი მუშაობდა ფუნქცია
import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("შესრულების დრო:", end - start, "წამი")
    return wrapper

@timer_decorator
def test_function():
    time.sleep(1)

test_function()

# 8) შექმენით ფუნქცია 'multiply', რომელიც იღებს რიცხვებს 'args'-ით და აბრუნებს მათ ნამრაველს
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))

# 9) შექმენით ფუნქცია, რომელიც იღებს 'args'-ით რიცხვებს და აბრუნებს მათ მაქსიმუმს და მინიმუმს
def min_max(*args):
    return min(args), max(args)

print(min_max(3, 7, 1, 9, 4))

# 10) დაწერეთ დეკორატორი, რომელიც ფუნქციის დაბრუნებულ ტექსტს გადააქცევს დიდ ასოებად
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def get_text():
    return "hello python"

print(get_text())
