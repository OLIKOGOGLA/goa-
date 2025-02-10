# 1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.
def add_five(num):
    return num + 5

# 2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს
def multiply(a, b):
    return a * b

# 3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len(), ახალი მასალაა).
def string_length(s):
    return len(s)

# 4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).
def string_lengths_list(strings):
    return [len(s) for s in strings]

# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.
def is_palindrome(s):
    return s == s[::-1]

# 6. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
# (მაგალითად: input: "Hello World". output: "HELLO WORLD"
def to_uppercase(s):
    return s.upper()
