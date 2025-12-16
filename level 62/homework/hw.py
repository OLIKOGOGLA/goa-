def tuple_info(t):
    print("სიგრძე:", len(t))
    print("პირველი ელემენტი:", t[0])
    print("ბოლო ელემენტი:", t[-1])

my_tuple = (10, 20, 30, 40)
tuple_info(my_tuple)

print("\n" + "-"*40)

person_tuple = ("გიორგი", 25, "საქართველო")
name, age, country = person_tuple
print("სახელი:", name)
print("ასაკი:", age)
print("ქვეყანა:", country)

print("\n" + "-"*40)

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print("საწყისი სია:", my_list)
print("tuple:", my_tuple)
print("უკან list:", back_to_list)

print("\n" + "-"*40)

numbers = {1, 3, 5}
numbers.add(7)
numbers.add(9)
numbers.remove(3)
numbers.remove(1)

even_numbers = {2, 4, 6, 8, 10}
print("union:", numbers.union(even_numbers))
print("intersection:", numbers.intersection(even_numbers))
print("difference:", numbers.difference(even_numbers))

print("\n" + "-"*40)

def modify_set(s):
    s.add(100)
    s.add(200)
    s.add(300)
    s.remove(100)
    return s

print("modify_set შედეგი:", modify_set({10, 20}))

print("\n" + "-"*40)

student = {
    "name": "ნინო",
    "hobby": "ცეკვა",
    "height": 165,
    "weight": 55
}
print("name (get):", student.get("name"))
student.pop("height")
print("student height წაშლის შემდეგ:", student)

print("\n" + "-"*40)

def dict_info(d):
    return d.keys(), d.values()

keys, values = dict_info({"a": 1, "b": 2})
print("keys:", keys)
print("values:", values)

print("\n" + "-"*40)

person = {"name": "გიორგი", "age": 30, "city": "თბილისი"}
for k, v in person.items():
    print(f"Key: {k}, Value: {v}")

print("\n" + "-"*40)

animal = {"type": "dog", "age": 5}
animal_copy = animal.copy()
print("დასაწყისში:", animal, animal_copy)
animal.clear()
animal_copy.clear()
print("clear()-ის შემდეგ:", animal, animal_copy)

print("\n" + "-"*40)

def update_and_remove(d):
    d.update({"age": 14})
    d.popitem()
    print("შეცვლილი ლექსიკონი:", d)

update_and_remove({"name": "გიორგი", "city": "ბათუმი"})
