# 1) შექმენით tuple, კომენტარებით დაწერეთ მისი თვისებები და მოახდინეთ მისი გადმობარგება
#  (unpacking)
# tuple  არის მრავალმნიშვნელობიანი ცვლადი რომელსაც ვერ შევუცვლით მნიშვნელობებს
student=["takalandze","giorgi" , 13]


lastname,name,age= student
print(lastname)
print(name)
print(age)

#2) შექმენით 2 რიცხვითი set, შემდეგ ჩამოწერეთ set-ის თვისებები,
#  შეცვალეთ თითოეული set .add და .remove მეთდების მეთოდების გამოყენებით 
# და საბოლოოდ შეასრულეთ ორ set-ს შორის ოპერაციები და ახსენით თითოეული კომენტარებით

#set-ის თვისებებია მაგალითად ის არ უშვებს ერთსადაიმავე ციფრებს,მაგრამ მისი შეცვლა შეგვიძლია,
# არ ექცევა დიდი ყურადღება განლაგებას.
nam1={2,4,6,8,10,12,14,3,7,15}
nam2={1,3,5,7,9,11,13,15,17,19}
nam1.add(7)
nam2.remove(1)
#გაერთიანება უმატებს ერთმანეთს განსხვავებულებს ხოლო რაც საერთოა ერთხელ იღებს
print(nam1.union(nam2))
#თანაკვეთა მხოლოდ ის გამოაქვს რაც საერთო აქვთ
print(nam1.intersection(nam2))
#სხვაობა მხოლოდ ის გამოაქვს რაც საერთო არ აქვთ
print(nam1.difference(nam2))


# 3) შექმენით person dictionary რომელშიც გექნებათ 5 გასაღები/მნიშვნელობის წყვილი.
# ახსენით კომენტაებით როგორი მონაცემთა ტიპია dictionary, შემდეგ კი დაბეჭდეთ 
# ერთ-ერთი გასაღების მნიშვნელობა, შემდეგ შეცვალეთ ერთი და დაამატეთ ერთი წყვილი.
# საბოლოოდ გატესტეთ ყველა ნასწავლი მეთოდი

# Dictionary არის გასაღები-მნიშვნელობის წყვილების ერთგვარი სია
person = {
    "Class": "8v",
    "Age": 12,
    "First_name": "Ninu",
    "Last_name": "Todea",
    "Annual_marks": 10
}
print(person["First_name"])
person["Age"] = 13
person["Hobby"] = "Drawing"


print("Values:", person.values())

print("Keys:", person.keys())

print("Items:", person.items())

person_copy = person.copy()
print("Copied dict:", person_copy)

person.update({"Favorite_color": "Blue"})
print("Updated with new key:", person)

removed_value = person.pop("Annual_marks")
print("Removed Annual_marks:", removed_value)

last_item = person.popitem()
print("Removed last item:", last_item)

first_name = person.get("First_name")
print("Get First_name:", first_name)

   
    
   
    