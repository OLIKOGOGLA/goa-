# 2) დაწერეთ ფუნქცია, რომელიც იღებს ასაკს და თუ ის უარყოფითია, გამოიყენეთ 'raise' რათა გამოაგდოს 'ValueError' შეტყობინებით "ასაკი არ შეიძლება იყოს უარყოფითი"
def check_age(age):
    if age < 0:
        raise ValueError("ასაკი არ შეიძლება იყოს უარყოფითი")
    return age

try:
    print(check_age(-3))
except ValueError as e:
    print(e)

# 3) დაწერეთ ფუნქცია, რომელიც იღებს სიტყვას და თუ ის ცარიელია, გამოიყენეთ 'raise' რათა გამოაგდოს 'ValueError' შეტყობინებით "სიტყვა არ უნდა იყოს ცარიელი"
def check_word(word):
    if word == "":
        raise ValueError("სიტყვა არ უნდა იყოს ცარიელი")
    return word

try:
    print(check_word(""))
except ValueError as e:
    print(e)

# 4) შექმენით 'lambda' ფუნქცია, რომელიც მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს
sum_numbers = lambda a, b: a + b

print(sum_numbers(5, 7))

# 5) შექმენით 'lambda' ფუნქცია, რომელიც გადაყავს ცელსიუსი ფარენჰეიტში და გამოიყენეთ 'for' ციკლში
celsius_to_fahrenheit = lambda c: c * 9 / 5 + 32

temps = [0, 10, 20, 30]

for c in temps:
    print(celsius_to_fahrenheit(c))

# 6) რიცხვების სიაზე "nums = [3, 6, 9, 12, 15]" გამოიყენეთ 'map', რათა ყველა რიცხვი გაიზარდოს 5-ით
nums = [3, 6, 9, 12, 15]

result = list(map(lambda x: x + 5, nums))
print(result)

# 7) სიტყვების სიაზე "words = ['hello', 'world', 'python']" გამოიყენეთ 'map', რათა ყველა სიტყვა გადაიქცეს დიდ ასოებად
words = ['hello', 'world', 'python']

result = list(map(lambda w: w.upper(), words))
print(result)

# 8) რიცხვების სიაზე "nums = [5, 8, 11, 14, 17]" გამოიყენეთ 'filter', რათა დატოვოთ მხოლოდ რიცხვები რომლებიც მეტია 10-ზე
nums = [5, 8, 11, 14, 17]

result = list(filter(lambda x: x > 10, nums))
print(result)

# 9) სიტყვების სიაზე "words = ['ant', 'elephant', 'dog', 'giraffe']" გამოიყენეთ 'filter', რათა დატოვოთ მხოლოდ ის სიტყვები, რომლების სიგრძეა მეტი ან ტოლია 5-ის
words = ['ant', 'elephant', 'dog', 'giraffe']

result = list(filter(lambda w: len(w) >= 5, words))
print(result)

# 10) რიცხვების სიაზე "nums = [2, 4, 6, 8]" გამოიყენეთ 'map' და 'lambda', რათა ყველა რიცხვი გაორმაგდეს
nums = [2, 4, 6, 8]

result = list(map(lambda x: x * 2, nums))
print(result)

# 11) რიცხვების სიაზე "nums = [1, 2, 3, 4, 5, 6]" გამოიყენეთ 'filter' და 'map' ერთად 'lambda'-თან, რათა გაფილტრდეს ლუწები და შემდეგ ყველა ლუწი გაიზარდოს 10-ით
nums = [1, 2, 3, 4, 5, 6]

result = list(
    map(lambda x: x + 10,
        filter(lambda x: x % 2 == 0, nums))
)

print(result)
