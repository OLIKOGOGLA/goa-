# 1. უდიდესი რიცხვის პოვნა max() გამოყენების გარეშე
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# 2. ხმოვნების რაოდენობის დათვლა სიტყვაში
def count_vowels(word):
    vowels = "აეიოუAEIOU"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

# 3. პალინდრომის შემმოწმებელი ფუნქცია
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

# 4. სტრიქონის დაბრუნება
def return_string(s):
    return s

# 5. წინადადებაში ყველაზე გრძელი სიტყვის პოვნა
def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

#მოიძიეთ ინფრომაცია split()-ზე.

# split() არის სტრიქონის (string) მეთოდი, 
# რომელიც ყოფს სტრიქონს სიტყვებად (ან სხვა ნაწილებად)
# კონკრეტული გამყოფის (delimiter-ის) გამოყენებით და აბრუნებს სიას (list).