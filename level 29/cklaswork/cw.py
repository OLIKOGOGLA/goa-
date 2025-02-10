##1. შექმენით ფუნქცია რომელიც 2 რიცხვს ყოფს ერთმანეთზე და პრინტავს შედეგს.
def Mathematical_operations (nam1 , nam2) :
    print(nam1 // nam2)
Mathematical_operations(19,5)

# 2. შექმენით ფუნქცია, რომელიც 3 რიცხვს კრიბასვს და პრინტავს შედეგს.
def Mathematical_operations (nam1 , nam2 , nam3) :
    print(nam1 + nam2 + nam3)
Mathematical_operations(19,20,7)

# 3. შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სტრინგი (ადამიანის სახელი), შემდეგ კი პრინტავს მისალმების მესიჯს.
def hello (name):
    print( "hello"+ name)
name=(input("enter your name")) 
hello(name)