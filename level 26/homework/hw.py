# 1. შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა.
list1 = [1, 2, 3]
list2 = ['apple', 'banana', 'cherry']
list3 = [True, False]
list4 = [10.5, 20.5, 30.5, 40.5]

print(len(list1))  # 3
print(len(list2))  # 3
print(len(list3))  # 2
print(len(list4))  # 4
# 2. შექმენთ 3 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 2-2 ცვლადი.
list1 = []
list2 = []
list3 = []

list1.append(5)
list1.append(10)

list2.append('apple')
list2.append('orange')

list3.append(3.14)
list3.append(2.71)

print(list1)  # [5, 10]
print(list2)  # ['apple', 'orange']
print(list3)  # [3.14, 2.71]
# 3. შექმენით 2 ლისტი. პირველს მე3ე და მე0ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე4ე და მე2ე ადგილას.
list1 = [1, 2, 3]
list2 = ['apple', 'banana', 'cherry']

# list1 - დაამატეთ მე3ე და მე0ე ადგილას
list1.insert(3, 4)
list1.insert(0, 0)

# list2 - დაამატეთ მე4ე და მე2ე ადგილას
list2.insert(4, 'grape')
list2.insert(2, 'kiwi')

print(list1)  # [0, 1, 2, 3, 4]
print(list2)  # ['apple', 'banana', 'kiwi', 'cherry', 'grape']
# 4. შექმენით 1 ლისტი და ორივედან ამოშალეთ 2 ცვლადი pop ფუნქციის გამოყენებით.
list1 = [1, 2, 3, 4, 5]

# ამოიღეთ პირველი ცვლადი
list1.pop()

# ამოიღეთ მეორე ცვლადი
list1.pop()

print(list1)  # [1, 2, 3]
# 5. შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში.
str1 = "Hello"
str2 = "Python"
str3 = "World"

print(len(str1))  # 5
print(len(str2))  # 6
print(len(str3))  # 5