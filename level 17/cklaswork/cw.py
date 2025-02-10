#1. შექმენით პროგრამა, სადა მომხმარებეს შემოატანინებთ ასაკს, თუ მისი ასაკი იქნება 18-ის ტოლი ან მეტი, გამოუტანეთ რომ ის ზრდასრულია, თუ იქნება ნაკლები, გამოუტანეთ, რომ ჯერ პატარაა.

age=input("enter your age" )
if age >= 18:
    print("you are perfect ")
elif age < 18:
    print("you are litel")

#2. შექმენით პროგრამა, სადაც გექნებათ ცვლადი საიდუმლო პაროლით, შემდეგ მომხმარებელს გამაოცნობინეთ სიტყვა, თუ მისი გამოცნობილი სიტყვა უდრის თქვენს საიდუმლო პაროლს, დაუპრინტეთ, რომ გაიმარჯვა.
pasword="goa"
pasword_=input("enter secret password" )
if pasword == pasword_ :
    print("you are writ")
elif pasword != pasword_ :
    print("you are wrong")