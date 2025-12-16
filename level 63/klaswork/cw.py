# 1) შექმენით სია, რომელშიც ჩაამატებთ რიცხვებს 1-იდან 20-მდე.
# შემდეგ შექმენით მეორე სია რომელშიც ჩაამატებთ მხოლოდ ლუწ რიცხვებს 10-იდან 40-მდე.
# საბოლოოდ შექმენით სია რომელშიც ჩაამტებთ 1-იდან 8-მდე რიცხვების კვადრატებს.
# ეს დავალებები ჯერ შეასრულეთ ვრცელი აქამდე ნაცნობი გზით,
# შემდეგ კი გამოიყენეთ list comperhenions და ჩაწერეთ მოკლედ.
# უკანასკნელად კიდევ ერთი სია აიღეთ  რომელშიც მოკლე გზით დამატებთ კენტ რიცხვებს 5-იდან 15-მდე და გაამრავლებთ ორზე

numbers = []
for i in range(1, 21):
    numbers.append(i)

even_numbers = []
for i in range(10, 41):
    if i % 2 == 0:
        even_numbers.append(i)

squares = []
for i in range(1, 9):
    squares.append(i ** 2)

numbers_short = [i for i in range(1, 21)]

even_numbers_short = [i for i in range(10, 41) if i % 2 == 0]

squares_short = [i ** 2 for i in range(1, 9)]

odd_times_two = [i * 2 for i in range(5, 16) if i % 2 != 0]


print(numbers,even_numbers,squares,numbers_short,even_numbers,even_numbers_short,squares_short,odd_times_two)
