# 1. შექმენით ფუნქცია, რომელიც იღებს რიცხვების ჩამონათვალს და აბრუნებს ახალ სიას, სადაც თითოეული რიცხვი მრავლდება 2-ზე, for loop და .append()-ის გამოყენებით.

def double(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

# 2. შექმენით პროგრამა, სადაც მომხმარებელს შეატანინებთ რიცხვს 5-ჯერ, დაამატებთ მათ სიაში და დაბეჭდავთ შებრუნებულ სიას.

numbers = []

for i in range(5):
    number = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(number)

reversed_numbers = list(reversed(numbers))
print("შებრუნებული სია:", reversed_numbers)

# 3. შექმენით ფუნქცია, რომელიც მიიღებს სიტყვების ჩამონათვალს და დააბრუნებს მათი სიგრძის სიას.

def word_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

# 4. შექმენით პროგრამა, რომელიც ახდენს მარტივი სკოლის ჟურნალის სიმულაციას, მიიღეთ სტუდენტების სახელები და ქულები input()-ით, დაამატეთ ისინი სიაში და აჩვენეთ თითოეული მოსწავლის სახელი მის გვერდზე საშუალო ქულით.

students = []

num_students = int(input("მოსწავლეების რაოდენობა: "))

for i in range(num_students):
    name = input(f"{i+1}. შეიყვანეთ მოსწავლის სახელი: ")
    grades_input = input("შეიყვანეთ ქულები მძიმით გამოყოფილი (მაგ: 10,9,8): ")
    grades = [int(g) for g in grades_input.split(",")]
    average = sum(grades) / len(grades)
    students.append((name, average))

print(" სკოლის ჟურნალი:")
for student in students:
    print(f"{student[0]} - საშუალო ქულა: {student[1]:.2f}")

# 5. შექმენით ფუნქცია, რომელიც მიიღებს სტრინგების სიას და დააბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ 3 სიმბოლოზე მეტ სტრინგებს.

def filter_long_strings(strings):
    result = []
    for s in strings:
        if len(s) > 3:
            result.append(s)
    return result
