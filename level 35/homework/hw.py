# 1. მაქსიმალური რიცხვის პრინტირება თითოეული list-იდან
list1 = [12, 34, 56, 78, 90]
list2 = [3, 45, 67, 89, 21]
list3 = [9, 12, 45, 76, 100]

print("Max of list1:", max(list1))  
print("Max of list2:", max(list2))  
print("Max of list3:", max(list3))  

# 2. მინიმალური რიცხვის პრინტირება თითოეული list-იდან
print("Min of list1:", min(list1))  
print("Min of list2:", min(list2))  
print("Min of list3:", min(list3))  

# 3. List-ის სიგრძის პრინტირება
print("Length of list1:", len(list1))  
print("Length of list2:", len(list2))  
print("Length of list3:", len(list3)) 

# 4. List-დან რიცხვების ჯამი
print("Sum of list1:", sum(list1))  
print("Sum of list2:", sum(list2))  
print("Sum of list3:", sum(list3))  

# 5. List-ის ელემენტების ქმედებები:

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First to Fourth elements of list1:", list1[0:4]) 

list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("4th to 7th elements of list2:")
for i in range(3, 7):
    print(list2[i])  # 14, 15, 16, 17

list3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print("9th to 6th elements of list3 (negative indices):", list3[8:5:-1])  # [29, 28, 27]

list4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print("All elements of list4 using while loop:")
index = 0
while index < len(list4):
    print(list4[index])
    index += 1

# Boss Level: 6. Def ფუნქციის შექმნა

def list_stats(user_list):
    """ფუნქცია, რომელიც არგუმენტად იღებს list-ს და ასრულებს აუცილებელ ოპერაციებს"""
    print("Max value:", max(user_list))
    print("Min value:", min(user_list))
    print("Sum of values:", sum(user_list))
    print("Length of list:", len(user_list))


user_input = [int(input(f"Enter number {i+1}: ")) for i in range(5)] 
print("\nStatistics for the user's list:")
list_stats(user_input)  
