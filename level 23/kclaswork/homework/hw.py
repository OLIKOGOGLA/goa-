#1. შექმენი ცვლადი, სადაც შეინახავ სტრინგს, შემდეგ გამოიტანე იმ სტრინგის მეორე ასო.
name="მეშვიდე_ა_კლასი"
print(name[1])
#2. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
age=12
klas=7
print(age + klas)
#3. შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია (ასევე კომენტარის სახით აღწერეთ რა არის კონკატენაცია).
name=" nino "
namee= "hello"
print(namee + name)
#4. შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)
# იმიტომ გამოიტანა floatი რო მარ დავწერეთ ორი გაყოფის ნიშნით
age=19
age1=3
print(age/age1)
#5. გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი
print(1==2)
print(2!=5)
print(5<=5)
print(6>=7)
print(6>7)
print(7<5)
#6. შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2)
print(1+1==2-0)
print(5/2!=5/15)
print(4+5<=5*2-1)
print(3/6>=7-5)
print(6*6>7*5)
print(8-7<5-4)
#7. გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა (სულ უნდა იყოს რვა, გაიხსენეთ ნასწავლიდან)
print(True or False)
print(False or True)
print(True or True)
print(False or False)
print(False and False )
print(True and True)
print(True and False)
print(False and True)
#8. შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი
print(True < False)
print(False > True)
print(True == True)
print(False != False)
print(False <= False )
#9. შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
for i in range(10,1):
    print(i)
#10. შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
age2=[1,2,5,4,8,9,11]
for age2 in range(1):
    print(age2 + age2)
#11. შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
for i in range(10):
    print("Hello, World!")
#12. შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
i = 1
while i <= 10:
    print(i)
    i += 1
#13. შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1
#14. შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.
sum = 0
i = 1
while sum < 50:
    sum += i
    i += 1
print("ჯამი:", sum)