# 1) შექმნით ფუნქცია add_numbers რომელიც იღებს 2 რიცხვს და აბრუნებს მათ ჯამს,
#  შემდეგ შექმენით ფუნქცია full_name რომელიც ღებულობს სახელსა და გვარს და 
# აბრუნებს სრულ სახელს. თითოეული ფუნქცია 2-ჯერგამოიძახეთ სხვადასხვა მაგალითით
# და შემდეგ იგივე ფუნქციბი დაწერეთ lambda გამოსახულებით

def add_numbers(a, b):
    return a + b

print(add_numbers(5, 7))

def full_name(first, last):
    return first + " " + last

print(full_name("გიორგი", "პეტრიშვილი"))


add_numbers_lambda = lambda a, b: a + b
full_name_lambda = lambda first, last: first + " " + last


print(add_numbers_lambda(15, 25))
print(full_name_lambda("ლაშა", "ბერიძე"))


#2) შექმენით manual_map და manual_filter ფუნქციები თქვენი ხელით რომლებიც
#  იქნება map და filter ფუნქციების ანალოგი, თითოეულზე მოიყვანეთ 2 მაგალითი
#  და ახსენით როგორ მუშაობს

def manual_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


def manual_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


numbers = [1, 2, 3, 4, 5]

print(manual_map(lambda x: x * 2, numbers))
print(manual_map(lambda x: x ** 2, numbers))

print(manual_filter(lambda x: x % 2 == 0, numbers))
print(manual_filter(lambda x: x > 3, numbers))