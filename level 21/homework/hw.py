##1. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი indexing-ის მეშვეობით გამოიტანეთ მეორე ელემენტი.
name=["nika " "lika " "nino " "lasha"]
print(name[1])
#2. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი შეცვალეთ მეორე ინდექსი სხვა მნიშვნელობით.
name[1:2]='melano'
#3. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (positive indexing).
__name__=["gorgi" "mariami" "guliko" "nikolozi" "aleqsandre"]
print(__name__[0:2])
#4. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (negative indexing).
print(__name__[-5:-3])
#5. შექმენით სია, სადაც გექნებათ 6 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეოთხე ელემენტი (negative indexing & positive indexing).
name=["nika""beqa""lika""barbare""temo""tata"]
print(name[-6][4])