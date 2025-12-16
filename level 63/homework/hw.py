numbers = [1, 4, 7, 10, 13, 16, 19]
new_list = []
for num in numbers:
    if num % 2 != 0:
        new_list.append(num * 2)
print("2) for-ით:", new_list)
new_list2 = [num * 2 for num in numbers if num % 2 != 0]
print("2) comprehension-ით:", new_list2)
squares = [n**2 for n in [1, 2, 3, 4, 5]]
print("მხოლოდ მოქმედება:", squares)
evens = [n for n in range(1, 11) if n % 2 == 0]
print("მხოლოდ პირობა:", evens)

words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
print("\n3) for-ით:", long_words)
long_words2 = [word for word in words if len(word) > 5]
print("3) comprehension-ით:", long_words2)

nums = list(range(1, 21))
squares = []
for n in nums:
    squares.append(n**2)
print("\n4) კვადრატები for-ით:", squares)
squares2 = [n**2 for n in nums]
print("4) comprehension-ით:", squares2)
cubes = [n**3 for n in nums]
print("კუბები:", cubes)

mixed = [2, 5, 8, 11, 14, 17, 20]
evens = [n for n in mixed if n % 2 == 0]
odds = [n for n in mixed if n % 2 != 0]
print("\n5) ლუწები:", evens)
print("5) კენტები:", odds)

animals = ['tiger', 'lion', 'zebra', 'elephant', 'giraffe']
first_letters = []
for animal in animals:
    first_letters.append(animal[0])
print("\n6) პირველი ასოები for-ით:", first_letters)
first_letters2 = [animal[0] for animal in animals]
print("6) პირველი ასოები comprehension-ით:", first_letters2)
starts_with_e = [animal for animal in animals if animal.startswith('e')]
print("6) e-ზე დაწყებულები:", starts_with_e)
