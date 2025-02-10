#შექმენით 3 ცვლადი, პირველში და მეორეში მომხმარებელმა უნდა შემოიტანოს რიცხვი ხოლო მესამეში რაიმე ოპერატორი 
# (-, +, /, *) გააკეთეთ კალკულატორის სადაც პირველ რიცხვს გამრავლდება, გაიყოფა, მიემატება ან გამოაკლდება მეორე რიცხვი

age=int(input("Enter one number"))
age_=int(input("Enter one number"))
Signs_of_action=input("Signs of action (-,+,/,*)")

if Signs_of_action == "-":
    print(age - age_ )
elif Signs_of_action == "+":
    print(age + age_ )
elif Signs_of_action == "*":
    print(age * age_ )
elif Signs_of_action == "/":
    print(age / age_ )
elif age_ =="0":
    print("error")
#3) დაწერეთ while ციკლი სადაც მომხმარებელს შემოატანინებს სიტყვას მანამდე სანამ მისი სიტყვა არ დაემთხვევა password - ს 

mane=input("Enter your password ")
password="New Year"

if mane == password:
    print("You are right")
elif mane != password:
    print("you are Wrong")
    mane=input("Enter your password ")





























