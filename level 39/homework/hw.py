# 1. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვების ჯამი.
numbers1 = [5, 10, 15, 20, 25]
sum_numbers1 = sum(numbers1)
print(sum_numbers1)
# 2. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უდიდესი.
max_number = max(numbers1)
print(max_number)
# 3. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უმცირესი.
min_number = min(numbers1)
print(min_number)
# 4. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიის სიგრძე.
length_of_list = len(numbers1)
print(length_of_list)
# 5. შექმენით სია, 5 სტრინგით, შემდეგ .append()-ის მეშვეობით სიის ბოლოში დაამატეთ სასურველი სიტყვა.
strings = ["apple", "banana", "cherry", "date", "elderberry"]
strings.append("fig")
print(strings)
# 6. შექმენით სია, 5 სტრინგით, შემდეგ .insert()-ის მეშვეობით სიაში სასურველ ინდექსზე დაამატეთ სასურველი სიტყვა.
strings.insert(2, "grape")
print(strings)
# 7. შექმენით სია, 5 სტრინგით, შემდეგ .pop()-ის მეშვეობით სიიან ამოაგდეთ ინდექსის მეშვეობით რომელიმე სიტყვა.
popped_item = strings.pop(3)
print(popped_item)

# # 1. https://www.codewars.com/kata/544675c6f971f7399a000e79
# 2. https://www.codewars.com/kata/50654ddff44f800200000004
# 3. https://www.codewars.com/kata/53369039d7ab3ac506000467
# 4. https://www.codewars.com/kata/55ca77fa094a2af31f00002a
# 5. https://www.codewars.com/kata/5715eaedb436cf5606000381