#1.* შექმენი ფუნქცია სახელად max_of_two, რომელიც არგუმენტად იღებს ორ რიცხვს. 
# * ფუნქციამ უნდა დააბრუნოს და დაპრინტოს ამ ორი რიცხვიდან უფრო დიდი. 
a=input("enter namber a")
b=input("enter namber b")
def max_of_two(a, b):
    if a > b:
        print(a)
    else:
        print(b)
max_of_two(a,b)
# 2. შექმენით ფუნქცია, რომელიც გადაუვლის სახელების სიას,
#  და დაპრინტავს თითოეულ სახელს, წინ დამატებული hello-თი.
name=["oliko","nino","lika"]
def greet_names(names):
    for name in names:
        print(f"Hello, {name}!")
greet_names(name)